-- Script de inicialização do banco de dados
-- Criação das tabelas da camada Silver

-- Schema para dados Silver
CREATE SCHEMA IF NOT EXISTS silver;

-- Tabela principal de dados processados
CREATE TABLE IF NOT EXISTS silver.train_data (
    id SERIAL PRIMARY KEY,
    -- Colunas serão definidas após análise dos dados
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de metadados
CREATE TABLE IF NOT EXISTS silver.data_metadata (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(255) NOT NULL,
    column_name VARCHAR(255) NOT NULL,
    data_type VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de logs de processamento
CREATE TABLE IF NOT EXISTS silver.processing_logs (
    id SERIAL PRIMARY KEY,
    process_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    records_processed INTEGER,
    error_message TEXT,
    started_at TIMESTAMP,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices para performance
CREATE INDEX IF NOT EXISTS idx_train_data_created_at ON silver.train_data(created_at);
CREATE INDEX IF NOT EXISTS idx_processing_logs_status ON silver.processing_logs(status);
CREATE INDEX IF NOT EXISTS idx_processing_logs_started_at ON silver.processing_logs(started_at);

-- Comentários nas tabelas
COMMENT ON SCHEMA silver IS 'Schema para dados processados e limpos (camada Silver)';
COMMENT ON TABLE silver.train_data IS 'Tabela principal com dados processados do dataset de treino';
COMMENT ON TABLE silver.data_metadata IS 'Metadados das colunas e tabelas';
COMMENT ON TABLE silver.processing_logs IS 'Logs de processamento ETL';
