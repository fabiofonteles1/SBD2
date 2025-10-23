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
    last_verdict INT NOT NULL;
);
```
