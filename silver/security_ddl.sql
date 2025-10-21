-- =====================================================
-- DDL - Data Definition Language
-- Microsoft Security Incident Prediction (Silver Layer)
-- =====================================================

-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS security_incident_prediction
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE security_incident_prediction;

-- =====================================================
-- TABELA PRINCIPAL: microsoft_security_incident
-- =====================================================

CREATE TABLE microsoft_security_incident (
    -- Identificadores
    id BIGINT PRIMARY KEY COMMENT 'Identificador único do registro',
    org_id INT NOT NULL COMMENT 'Identificador da organização',
    incident_id INT NOT NULL COMMENT 'Identificador único do incidente',
    alert_id INT NOT NULL COMMENT 'Identificador único do alerta',
    
    -- Informações temporais
    timestamp DATETIME NOT NULL COMMENT 'Timestamp do incidente',
    year INT GENERATED ALWAYS AS (YEAR(timestamp)) STORED COMMENT 'Ano extraído do timestamp',
    month INT GENERATED ALWAYS AS (MONTH(timestamp)) STORED COMMENT 'Mês extraído do timestamp',
    day INT GENERATED ALWAYS AS (DAY(timestamp)) STORED COMMENT 'Dia extraído do timestamp',
    hour INT GENERATED ALWAYS AS (HOUR(timestamp)) STORED COMMENT 'Hora extraída do timestamp',
    day_of_week INT GENERATED ALWAYS AS (WEEKDAY(timestamp)) STORED COMMENT 'Dia da semana (0=Segunda)',
    
    -- Informações de detecção
    detector_id INT NOT NULL COMMENT 'Identificador do detector de segurança',
    alert_title INT NOT NULL COMMENT 'Título do alerta (encoded)',
    
    -- Classificação do incidente
    category INT NOT NULL COMMENT 'Categoria do incidente (encoded)',
    mitre_techniques INT NOT NULL COMMENT 'Técnicas MITRE associadas (encoded)',
    incident_grade INT NOT NULL COMMENT 'Grau do incidente (0=FalsePositive, 1=TruePositive, 2=BenignPositive)',
    
    -- Informações da entidade
    entity_type INT NOT NULL COMMENT 'Tipo de entidade envolvida (encoded)',
    evidence_role INT NOT NULL COMMENT 'Papel da evidência (encoded)',
    device_id BIGINT COMMENT 'Identificador do dispositivo',
    
    -- Identificadores de segurança
    sha256 BIGINT COMMENT 'Hash SHA256 do arquivo (encoded)',
    ip_address BIGINT COMMENT 'Endereço IP (encoded)',
    url BIGINT COMMENT 'URL envolvida (encoded)',
    account_sid BIGINT COMMENT 'SID da conta (encoded)',
    account_upn BIGINT COMMENT 'UPN da conta (encoded)',
    
    -- Informações do sistema
    os_family INT NOT NULL COMMENT 'Família do sistema operacional (encoded)',
    os_version INT NOT NULL COMMENT 'Versão do sistema operacional (encoded)',
    
    -- Informações geográficas
    country_code INT NOT NULL COMMENT 'Código do país (encoded)',
    state INT NOT NULL COMMENT 'Estado/Província (encoded)',
    city INT NOT NULL COMMENT 'Cidade (encoded)',
    
    -- Informações de veredito
    last_verdict INT NOT NULL COMMENT 'Último veredito (encoded)',
    
    -- Campos de auditoria
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Data de criação do registro',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Data de última atualização',
    
    -- Índices
    INDEX idx_incident_grade (incident_grade),
    INDEX idx_category (category),
    INDEX idx_timestamp (timestamp),
    INDEX idx_org_id (org_id),
    INDEX idx_country_code (country_code),
    INDEX idx_detector_id (detector_id),
    INDEX idx_entity_type (entity_type),
    INDEX idx_year_month (year, month),
    INDEX idx_hour (hour),
    INDEX idx_day_of_week (day_of_week),
    
    -- Índices compostos para consultas frequentes
    INDEX idx_incident_category_grade (incident_grade, category),
    INDEX idx_timestamp_org (timestamp, org_id),
    INDEX idx_geo_incident (country_code, incident_grade),
    INDEX idx_temporal_incident (year, month, incident_grade)
    
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci
  COMMENT='Tabela principal de incidentes de segurança processados (Silver Layer)';

-- =====================================================
-- VIEWS PARA ANÁLISE
-- =====================================================

-- View para análise de incidentes por categoria
CREATE VIEW v_incidents_by_category AS
SELECT 
    s.category,
    COUNT(*) as total_incidents,
    SUM(CASE WHEN s.incident_grade = 1 THEN 1 ELSE 0 END) as true_positives,
    SUM(CASE WHEN s.incident_grade = 0 THEN 1 ELSE 0 END) as false_positives,
    SUM(CASE WHEN s.incident_grade = 2 THEN 1 ELSE 0 END) as benign_positives,
    ROUND(AVG(CASE WHEN s.incident_grade = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) as precision_rate
FROM microsoft_security_incident s
GROUP BY s.category
ORDER BY total_incidents DESC;

-- View para análise temporal
CREATE VIEW v_temporal_analysis AS
SELECT 
    year,
    month,
    day_of_week,
    hour,
    COUNT(*) as total_incidents,
    SUM(CASE WHEN incident_grade = 1 THEN 1 ELSE 0 END) as true_positives,
    SUM(CASE WHEN incident_grade = 0 THEN 1 ELSE 0 END) as false_positives,
    ROUND(AVG(CASE WHEN incident_grade = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) as true_positive_rate
FROM microsoft_security_incident
GROUP BY year, month, day_of_week, hour
ORDER BY year, month, day_of_week, hour;

-- View para análise geográfica
CREATE VIEW v_geographic_analysis AS
SELECT 
    s.country_code,
    s.state,
    s.city,
    COUNT(*) as total_incidents,
    SUM(CASE WHEN s.incident_grade = 1 THEN 1 ELSE 0 END) as true_positives,
    SUM(CASE WHEN s.incident_grade = 0 THEN 1 ELSE 0 END) as false_positives,
    ROUND(AVG(CASE WHEN s.incident_grade = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) as precision_rate
FROM microsoft_security_incident s
GROUP BY s.country_code, s.state, s.city
ORDER BY total_incidents DESC;

-- View para análise de organizações
CREATE VIEW v_organization_analysis AS
SELECT 
    s.org_id,
    COUNT(*) as total_incidents,
    COUNT(DISTINCT s.incident_id) as unique_incidents,
    COUNT(DISTINCT s.category) as unique_categories,
    SUM(CASE WHEN s.incident_grade = 1 THEN 1 ELSE 0 END) as true_positives,
    SUM(CASE WHEN s.incident_grade = 0 THEN 1 ELSE 0 END) as false_positives,
    ROUND(AVG(CASE WHEN s.incident_grade = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) as precision_rate
FROM microsoft_security_incident s
GROUP BY s.org_id
ORDER BY total_incidents DESC;

-- =====================================================
-- PROCEDURES PARA MANUTENÇÃO
-- =====================================================

-- Procedure para calcular estatísticas diárias
DELIMITER //
CREATE PROCEDURE CalculateDailyStatistics(IN target_date DATE)
BEGIN
    INSERT INTO daily_statistics (
        stat_date,
        total_incidents,
        true_positives,
        false_positives,
        benign_positives,
        unique_categories,
        unique_countries,
        unique_organizations,
        peak_hour
    )
    SELECT 
        target_date,
        COUNT(*) as total_incidents,
        SUM(CASE WHEN incident_grade = 1 THEN 1 ELSE 0 END) as true_positives,
        SUM(CASE WHEN incident_grade = 0 THEN 1 ELSE 0 END) as false_positives,
        SUM(CASE WHEN incident_grade = 2 THEN 1 ELSE 0 END) as benign_positives,
        COUNT(DISTINCT category) as unique_categories,
        COUNT(DISTINCT country_code) as unique_countries,
        COUNT(DISTINCT org_id) as unique_organizations,
        (SELECT hour FROM microsoft_security_incident 
         WHERE DATE(timestamp) = target_date 
         GROUP BY hour 
         ORDER BY COUNT(*) DESC 
         LIMIT 1) as peak_hour
    FROM microsoft_security_incident
    WHERE DATE(timestamp) = target_date
    ON DUPLICATE KEY UPDATE
        total_incidents = VALUES(total_incidents),
        true_positives = VALUES(true_positives),
        false_positives = VALUES(false_positives),
        benign_positives = VALUES(benign_positives),
        unique_categories = VALUES(unique_categories),
        unique_countries = VALUES(unique_countries),
        unique_organizations = VALUES(unique_organizations),
        peak_hour = VALUES(peak_hour);
END //
DELIMITER ;

-- =====================================================
-- ÍNDICES ADICIONAIS PARA PERFORMANCE
-- =====================================================

-- Índices para consultas de análise temporal
CREATE INDEX idx_timestamp_incident_grade ON security_incidents_silver(timestamp, incident_grade);
CREATE INDEX idx_date_range ON security_incidents_silver(timestamp, org_id, incident_grade);

-- Índices para consultas geográficas
CREATE INDEX idx_geo_incident_grade ON security_incidents_silver(country_code, state, city, incident_grade);
CREATE INDEX idx_country_category ON security_incidents_silver(country_code, category);

-- Índices para consultas por organização
CREATE INDEX idx_org_timestamp ON security_incidents_silver(org_id, timestamp);
CREATE INDEX idx_org_incident_grade ON security_incidents_silver(org_id, incident_grade);

-- =====================================================
-- COMENTÁRIOS FINAIS
-- =====================================================

/*
Este DDL foi criado para suportar o dataset Microsoft Security Incident Prediction
processado na camada Silver. As principais características incluem:

1. ESTRUTURA SIMPLIFICADA:
   - Uma única tabela principal: microsoft_security_incident
   - Todos os dados processados em formato denormalizado
   - Campos encoded para otimização de espaço

2. OTIMIZAÇÕES DE PERFORMANCE:
   - Índices estratégicos para consultas frequentes
   - Índices compostos para queries complexas
   - Campos calculados (generated columns) para análise temporal

3. VIEWS DE ANÁLISE:
   - Views pré-configuradas para análises comuns
   - Agregações otimizadas para relatórios
   - Métricas de precisão e recall

4. ESCALABILIDADE:
   - Índices otimizados para grandes volumes
   - Estrutura preparada para crescimento
   - Campos encoded para economia de espaço

Data de Criação: Janeiro de 2025
Versão: 2.0
*/
