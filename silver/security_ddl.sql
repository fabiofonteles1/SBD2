CREATE SCHEMA IF NOT EXISTS silver AUTHORIZATION postgres;
CREATE TABLE silver.microsoft_security_incident (
    -- Identificadores
    id BIGINT PRIMARY KEY,
    org_id INT NOT NULL,
    incident_id INT NOT NULL,
    alert_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    year INT GENERATED ALWAYS AS (EXTRACT(YEAR FROM timestamp)::INT) STORED,
    month INT GENERATED ALWAYS AS (EXTRACT(MONTH FROM timestamp)::INT) STORED,
    day INT GENERATED ALWAYS AS (EXTRACT(DAY FROM timestamp)::INT) STORED,
    hour INT GENERATED ALWAYS AS (EXTRACT(HOUR FROM timestamp)::INT) STORED,
    day_of_week INT GENERATED ALWAYS AS (EXTRACT(DOW FROM timestamp)::INT) STORED,
    detector_id INT NOT NULL,
    alert_title INT NOT NULL,
    category INT NOT NULL,
    mitre_techniques INT NOT NULL,
    incident_grade INT NOT NULL,
    entity_type INT NOT NULL,
    evidence_role INT NOT NULL,
    device_id BIGINT,
    sha256 BIGINT,
    ip_address BIGINT,
    url BIGINT,
    account_sid BIGINT,
    account_upn BIGINT,
    os_family INT NOT NULL,
    os_version INT NOT NULL,
    country_code INT NOT NULL,
    state INT NOT NULL,
    city INT NOT NULL,
    last_verdict INT NOT NULL
);

COMMENT ON TABLE silver.microsoft_security_incident IS 'Incidentes de segurança da Microsoft (camada silver)';
COMMENT ON COLUMN silver.microsoft_security_incident.id IS 'Identificador único do registro';
COMMENT ON COLUMN silver.microsoft_security_incident.org_id IS 'Identificador da organização';
COMMENT ON COLUMN silver.microsoft_security_incident.incident_id IS 'Identificador único do incidente';
COMMENT ON COLUMN silver.microsoft_security_incident.alert_id IS 'Identificador único do alerta';
COMMENT ON COLUMN silver.microsoft_security_incident.timestamp IS 'Timestamp do incidente';
COMMENT ON COLUMN silver.microsoft_security_incident.year IS 'Ano extraído do timestamp';
COMMENT ON COLUMN silver.microsoft_security_incident.month IS 'Mês extraído do timestamp';
COMMENT ON COLUMN silver.microsoft_security_incident.day IS 'Dia extraído do timestamp';
COMMENT ON COLUMN silver.microsoft_security_incident.hour IS 'Hora extraída do timestamp';
COMMENT ON COLUMN silver.microsoft_security_incident.day_of_week IS 'Dia da semana (0=Domingo)';
COMMENT ON COLUMN silver.microsoft_security_incident.detector_id IS 'Identificador do detector de segurança';
COMMENT ON COLUMN silver.microsoft_security_incident.alert_title IS 'Título do alerta (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.category IS 'Categoria do incidente (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.mitre_techniques IS 'Técnicas MITRE associadas (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.incident_grade IS 'Grau do incidente (0=FalsePositive, 1=TruePositive, 2=BenignPositive)';
COMMENT ON COLUMN silver.microsoft_security_incident.entity_type IS 'Tipo de entidade envolvida (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.evidence_role IS 'Papel da evidência (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.device_id IS 'Identificador do dispositivo';
COMMENT ON COLUMN silver.microsoft_security_incident.sha256 IS 'Hash SHA256 do arquivo (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.ip_address IS 'Endereço IP (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.url IS 'URL envolvida (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.account_sid IS 'SID da conta (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.account_upn IS 'UPN da conta (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.os_family IS 'Família do sistema operacional (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.os_version IS 'Versão do sistema operacional (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.country_code IS 'Código do país (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.state IS 'Estado/Província (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.city IS 'Cidade (encoded)';
COMMENT ON COLUMN silver.microsoft_security_incident.last_verdict IS 'Último veredito (encoded)';
