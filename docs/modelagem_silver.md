# Modelagem da Camada Silver

## Visão Geral

A camada Silver representa os dados limpos, validados e estruturados, prontos para análise e consumo. Esta camada aplica regras de qualidade de dados, normalização e transformações necessárias.

## Modelo Entidade-Relacionamento (MER)

### Entidades Principais

#### 1. train_data (Tabela Principal)
- **Descrição**: Dados processados do dataset de treino
- **Chave Primária**: id (auto-incremento)
- **Campos de Auditoria**: created_at, updated_at

#### 2. data_metadata
- **Descrição**: Metadados das colunas e tabelas
- **Chave Primária**: id
- **Relacionamento**: 1:N com train_data (via table_name)

#### 3. processing_logs
- **Descrição**: Logs de processamento ETL
- **Chave Primária**: id
- **Relacionamento**: Independente (tabela de auditoria)

## Diagrama de Fluxo de Dados (DLD)

```
Raw Data (CSV) → Data Quality Checks → Data Transformation → Silver Layer (PostgreSQL)
     ↓                    ↓                      ↓                    ↓
train.csv         Validação de tipos      Normalização         silver.train_data
                  Verificação de nulos    Limpeza de dados     silver.data_metadata
                  Detecção de duplicatas  Enriquecimento      silver.processing_logs
```

## Regras de Transformação

### 1. Validação de Dados
- Verificação de tipos de dados
- Detecção de valores nulos
- Identificação de outliers
- Validação de formatos

### 2. Limpeza de Dados
- Tratamento de valores nulos
- Remoção de duplicatas
- Padronização de formatos
- Correção de inconsistências

### 3. Enriquecimento
- Criação de campos derivados
- Categorização de dados
- Agregações básicas
- Metadados de processamento

## Estrutura das Tabelas

### silver.train_data
```sql
CREATE TABLE silver.train_data (
    id SERIAL PRIMARY KEY,
    -- Colunas do dataset original (serão definidas após análise)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### silver.data_metadata
```sql
CREATE TABLE silver.data_metadata (
    id SERIAL PRIMARY KEY,
    table_name VARCHAR(255) NOT NULL,
    column_name VARCHAR(255) NOT NULL,
    data_type VARCHAR(100),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### silver.processing_logs
```sql
CREATE TABLE silver.processing_logs (
    id SERIAL PRIMARY KEY,
    process_name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    records_processed INTEGER,
    error_message TEXT,
    started_at TIMESTAMP,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Qualidade dos Dados

### Métricas de Qualidade
- **Completude**: % de valores não nulos
- **Consistência**: Conformidade com regras de negócio
- **Precisão**: Exatidão dos dados
- **Unicidade**: Ausência de duplicatas

### Controles de Qualidade
- Validação de integridade referencial
- Verificação de constraints
- Monitoramento de performance
- Alertas de qualidade

## Processo ETL

### Extract (Extração)
1. Leitura do arquivo CSV
2. Carregamento em chunks para arquivos grandes
3. Verificação de integridade do arquivo

### Transform (Transformação)
1. Aplicação de regras de qualidade
2. Limpeza e normalização
3. Enriquecimento com metadados
4. Validação final

### Load (Carregamento)
1. Inserção em lote no PostgreSQL
2. Criação de índices
3. Atualização de estatísticas
4. Log de processamento

## Monitoramento e Logs

### Logs de Processamento
- Timestamp de início/fim
- Número de registros processados
- Status de execução
- Mensagens de erro

### Métricas de Performance
- Tempo de processamento
- Throughput (registros/segundo)
- Uso de memória
- I/O de disco

## Próximos Passos

1. **Análise dos Dados**: Executar notebook de exploração
2. **Definição de Schema**: Criar DDL baseado na análise
3. **Implementação ETL**: Desenvolver transformações
4. **Testes**: Validar qualidade dos dados
5. **Documentação**: Atualizar dicionário de dados
