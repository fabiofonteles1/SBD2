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
    timestamp DATETIME NOT NULL COMMENT 'Timestamp do incidente',
    year INT GENERATED ALWAYS AS (YEAR(timestamp)) STORED COMMENT 'Ano extraído do timestamp',
    month INT GENERATED ALWAYS AS (MONTH(timestamp)) STORED COMMENT 'Mês extraído do timestamp',
    day INT GENERATED ALWAYS AS (DAY(timestamp)) STORED COMMENT 'Dia extraído do timestamp',
    hour INT GENERATED ALWAYS AS (HOUR(timestamp)) STORED COMMENT 'Hora extraída do timestamp',
    day_of_week INT GENERATED ALWAYS AS (WEEKDAY(timestamp)) STORED COMMENT 'Dia da semana (0=Segunda)',
    detector_id INT NOT NULL COMMENT 'Identificador do detector de segurança',
    alert_title INT NOT NULL COMMENT 'Título do alerta (encoded)',
    category INT NOT NULL COMMENT 'Categoria do incidente (encoded)',
    mitre_techniques INT NOT NULL COMMENT 'Técnicas MITRE associadas (encoded)',
    incident_grade INT NOT NULL COMMENT 'Grau do incidente (0=FalsePositive, 1=TruePositive, 2=BenignPositive)',
    entity_type INT NOT NULL COMMENT 'Tipo de entidade envolvida (encoded)',
    evidence_role INT NOT NULL COMMENT 'Papel da evidência (encoded)',
    device_id BIGINT COMMENT 'Identificador do dispositivo',
    sha256 BIGINT COMMENT 'Hash SHA256 do arquivo (encoded)',
    ip_address BIGINT COMMENT 'Endereço IP (encoded)',
    url BIGINT COMMENT 'URL envolvida (encoded)',
    account_sid BIGINT COMMENT 'SID da conta (encoded)',
    account_upn BIGINT COMMENT 'UPN da conta (encoded)',
    os_family INT NOT NULL COMMENT 'Família do sistema operacional (encoded)',
    os_version INT NOT NULL COMMENT 'Versão do sistema operacional (encoded)',
    country_code INT NOT NULL COMMENT 'Código do país (encoded)',
    state INT NOT NULL COMMENT 'Estado/Província (encoded)',
    city INT NOT NULL COMMENT 'Cidade (encoded)',
    last_verdict INT NOT NULL COMMENT 'Último veredito (encoded)';
