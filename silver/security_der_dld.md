# Diagramas DER e DLD - Microsoft Security Incident Prediction (Silver Layer)

## 1. Diagrama de Entidade-Relacionamento (DER)

### Descrição do DER
O Diagrama de Entidade-Relacionamento representa a estrutura lógica dos dados do dataset Microsoft Security Incident Prediction na camada Silver. Como foi simplificado para uma única tabela, o DER mostra a entidade principal e seus atributos.

### Entidade Principal: microsoft_security_incident

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           microsoft_security_incident                          │
├─────────────────────────────────────────────────────────────────────────────────┤
│ PRIMARY KEY: id (BIGINT)                                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│ Identificadores:                                                                │
│ • org_id (INT) - Identificador da organização                                  │
│ • incident_id (INT) - Identificador único do incidente                         │
│ • alert_id (INT) - Identificador único do alerta                               │
│                                                                                 │
│ Informações Temporais:                                                          │
│ • timestamp (DATETIME) - Timestamp do incidente                                │
│ • year (INT) - Ano extraído do timestamp (Generated Column)                    │
│ • month (INT) - Mês extraído do timestamp (Generated Column)                   │
│ • day (INT) - Dia extraído do timestamp (Generated Column)                     │
│ • hour (INT) - Hora extraída do timestamp (Generated Column)                   │
│ • day_of_week (INT) - Dia da semana (Generated Column)                         │
│                                                                                 │
│ Informações de Detecção:                                                        │
│ • detector_id (INT) - Identificador do detector de segurança                   │
│ • alert_title (INT) - Título do alerta (encoded)                              │
│                                                                                 │
│ Classificação do Incidente:                                                     │
│ • category (INT) - Categoria do incidente (encoded)                           │
│ • mitre_techniques (INT) - Técnicas MITRE associadas (encoded)                │
│ • incident_grade (INT) - Grau do incidente (0,1,2)                            │
│                                                                                 │
│ Informações da Entidade:                                                        │
│ • entity_type (INT) - Tipo de entidade envolvida (encoded)                    │
│ • evidence_role (INT) - Papel da evidência (encoded)                          │
│ • device_id (BIGINT) - Identificador do dispositivo                            │
│                                                                                 │
│ Identificadores de Segurança:                                                   │
│ • sha256 (BIGINT) - Hash SHA256 do arquivo (encoded)                          │
│ • ip_address (BIGINT) - Endereço IP (encoded)                                 │
│ • url (BIGINT) - URL envolvida (encoded)                                      │
│ • account_sid (BIGINT) - SID da conta (encoded)                               │
│ • account_upn (BIGINT) - UPN da conta (encoded)                               │
│                                                                                 │
│ Informações do Sistema:                                                         │
│ • os_family (INT) - Família do sistema operacional (encoded)                  │
│ • os_version (INT) - Versão do sistema operacional (encoded)                  │
│                                                                                 │
│ Informações Geográficas:                                                        │
│ • country_code (INT) - Código do país (encoded)                               │
│ • state (INT) - Estado/Província (encoded)                                    │
│ • city (INT) - Cidade (encoded)                                               │
│                                                                                 │
│ Informações de Veredito:                                                        │
│ • last_verdict (INT) - Último veredito (encoded)                              │
│                                                                                 │
│ Campos de Auditoria:                                                            │
│ • created_at (TIMESTAMP) - Data de criação do registro                         │
│ • updated_at (TIMESTAMP) - Data de última atualização                          │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Cardinalidades e Relacionamentos
Como o modelo foi simplificado para uma única tabela, não há relacionamentos entre entidades. Todos os dados estão denormalizados na tabela principal.

---

## 2. Diagrama Lógico de Dados (DLD)

### Descrição do DLD
O Diagrama Lógico de Dados representa a estrutura física dos dados, incluindo índices, constraints e otimizações de performance.

### Estrutura da Tabela Principal

```sql
CREATE TABLE microsoft_security_incident (
    -- Chave Primária
    id BIGINT PRIMARY KEY,
    
    -- Identificadores
    org_id INT NOT NULL,
    incident_id INT NOT NULL,
    alert_id INT NOT NULL,
    
    -- Campos Temporais
    timestamp DATETIME NOT NULL,
    year INT GENERATED ALWAYS AS (YEAR(timestamp)) STORED,
    month INT GENERATED ALWAYS AS (MONTH(timestamp)) STORED,
    day INT GENERATED ALWAYS AS (DAY(timestamp)) STORED,
    hour INT GENERATED ALWAYS AS (HOUR(timestamp)) STORED,
    day_of_week INT GENERATED ALWAYS AS (WEEKDAY(timestamp)) STORED,
    
    -- Campos de Detecção
    detector_id INT NOT NULL,
    alert_title INT NOT NULL,
    
    -- Campos de Classificação
    category INT NOT NULL,
    mitre_techniques INT NOT NULL,
    incident_grade INT NOT NULL,
    
    -- Campos de Entidade
    entity_type INT NOT NULL,
    evidence_role INT NOT NULL,
    device_id BIGINT,
    
    -- Campos de Segurança
    sha256 BIGINT,
    ip_address BIGINT,
    url BIGINT,
    account_sid BIGINT,
    account_upn BIGINT,
    
    -- Campos de Sistema
    os_family INT NOT NULL,
    os_version INT NOT NULL,
    
    -- Campos Geográficos
    country_code INT NOT NULL,
    state INT NOT NULL,
    city INT NOT NULL,
    
    -- Campos de Veredito
    last_verdict INT NOT NULL,
    
    -- Campos de Auditoria
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Índices Simples
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
    
    -- Índices Compostos
    INDEX idx_incident_category_grade (incident_grade, category),
    INDEX idx_timestamp_org (timestamp, org_id),
    INDEX idx_geo_incident (country_code, incident_grade),
    INDEX idx_temporal_incident (year, month, incident_grade),
    
    -- Índices Adicionais para Performance
    INDEX idx_timestamp_incident_grade (timestamp, incident_grade),
    INDEX idx_date_range (timestamp, org_id, incident_grade),
    INDEX idx_geo_incident_grade (country_code, state, city, incident_grade),
    INDEX idx_country_category (country_code, category),
    INDEX idx_org_timestamp (org_id, timestamp),
    INDEX idx_org_incident_grade (org_id, incident_grade)
);
```

### Views de Análise

#### 1. View de Incidentes por Categoria
```sql
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
```

#### 2. View de Análise Temporal
```sql
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
```

#### 3. View de Análise Geográfica
```sql
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
```

#### 4. View de Análise de Organizações
```sql
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
```

### Estratégias de Otimização

#### 1. Índices Estratégicos
- **Índices Simples**: Para campos frequentemente consultados
- **Índices Compostos**: Para consultas complexas com múltiplos filtros
- **Índices Gerados**: Para campos calculados automaticamente

#### 2. Particionamento (Futuro)
- **Particionamento Temporal**: Por ano/mês para melhor performance
- **Particionamento por Organização**: Para distribuição de carga

#### 3. Campos Encoded
- **Otimização de Espaço**: Campos categóricos convertidos para INT
- **Performance de Consultas**: Índices mais eficientes em campos numéricos
- **Redução de Memória**: Menor uso de espaço em disco

### Considerações de Performance

#### 1. Consultas Frequentes
- Análise por categoria de incidente
- Análise temporal (ano, mês, hora)
- Análise geográfica (país, estado, cidade)
- Análise por organização

#### 2. Métricas de Qualidade
- Taxa de verdadeiros positivos por categoria
- Distribuição temporal de incidentes
- Concentração geográfica de ameaças
- Performance por organização

#### 3. Escalabilidade
- Estrutura preparada para crescimento
- Índices otimizados para grandes volumes
- Campos encoded para economia de espaço
- Views pré-configuradas para relatórios

---

## 3. Resumo dos Diagramas

### DER (Diagrama de Entidade-Relacionamento)
- **Entidade Única**: microsoft_security_incident
- **Atributos**: 37 campos incluindo identificadores, temporais, de detecção, classificação, entidade, segurança, sistema, geográficos e veredito
- **Relacionamentos**: Nenhum (modelo denormalizado)

### DLD (Diagrama Lógico de Dados)
- **Tabela Principal**: microsoft_security_incident com 37 colunas
- **Índices**: 17 índices otimizados para consultas frequentes
- **Views**: 4 views pré-configuradas para análise
- **Performance**: Estrutura otimizada para grandes volumes de dados

### Características Principais
1. **Simplicidade**: Modelo denormalizado em uma única tabela
2. **Performance**: Índices estratégicos para consultas rápidas
3. **Escalabilidade**: Estrutura preparada para crescimento
4. **Análise**: Views pré-configuradas para relatórios
5. **Otimização**: Campos encoded para economia de espaço

---

**Data de Criação**: Outubro de 2025  
**Versão**: 2.0   
**Dataset**: Microsoft Security Incident Prediction (Silver Layer)