# Projeto Data Lakehouse - SBD-2

Este projeto implementa um Data Lakehouse com arquitetura em camadas (Bronze, Silver, Gold) para processamento e análise de dados.

## Estrutura do Projeto

```
sbd-2/
├── docker/                 # Configurações Docker
├── docs/                   # Documentação
├── notebooks/              # Jupyter Notebooks
├── raw/                    # Dados brutos (Bronze)
├── scripts/                # Scripts de automação
└── silver/                 # Dados processados (Silver)
```

## Camadas de Dados

### Bronze (Raw)
- **Localização**: `raw/`
- **Conteúdo**: Dados brutos sem tratamento
- **Formato**: CSV, JSON, etc.

### Silver (Processed)
- **Localização**: `silver/`
- **Conteúdo**: Dados limpos e estruturados
- **Formato**: Parquet, Delta Lake

### Gold (Analytics)
- **Localização**: `gold/`
- **Conteúdo**: Dados agregados para análise
- **Formato**: Parquet, Delta Lake

## Tecnologias Utilizadas

- **Python**: Pandas, PySpark
- **Banco de Dados**: PostgreSQL
- **Containerização**: Docker, Docker Compose
- **Orquestração**: Apache Airflow (opcional)
- **Visualização**: Jupyter Notebooks

## Como Executar

1. **Configurar ambiente**:
   ```bash
   docker-compose up -d
   ```

2. **Executar ETL**:
   ```bash
   python scripts/run_etl.py
   ```

3. **Acessar notebooks**:
   ```bash
   jupyter notebook notebooks/
   ```

## Documentação

- [Dicionário de Dados Bronze](dicionario_dados_bronze.md)
- [Modelagem Silver](modelagem_silver.md)
- [Diagramas](diagramas/)
