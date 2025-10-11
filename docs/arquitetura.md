# Arquitetura do Data Lakehouse

## Diagrama de Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAKEHOUSE SBD-2                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   BRONZE         │    │   SILVER        │    │   GOLD          │
│   (Raw Data)     │───▶│   (Processed)   │───▶│   (Analytics)   │
│                  │    │                 │    │                 │
│ • train.csv      │    │ • PostgreSQL    │    │ • Aggregations  │
│ • 2.4 GB        │    │ • Clean data    │    │ • Reports       │
│ • No treatment  │    │ • Validated     │    │ • Insights      │
│ • CSV format    │    │ • Structured    │    │ • Dashboards    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   RAW LAYER     │    │   PROCESSED     │    │   ANALYTICS     │
│                 │    │   LAYER         │    │   LAYER         │
│ • raw/train.csv │    │ • silver schema │    │ • gold schema   │
│ • No schema     │    │ • train_data    │    │ • Aggregations  │
│ • Raw format    │    │ • metadata      │    │ • Reports       │
│ • Large files   │    │ • logs          │    │ • Insights      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Fluxo de Dados (DLD)

```
┌─────────────────────────────────────────────────────────────────┐
│                        FLUXO DE DADOS                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   EXTRACT   │    │  TRANSFORM  │    │    LOAD     │    │  VALIDATE   │
│             │    │             │    │             │    │             │
│ • Read CSV  │───▶│ • Clean     │───▶│ • Insert    │───▶│ • Check     │
│ • Chunks    │    │ • Validate  │    │ • Index     │    │ • Quality    │
│ • Validate  │    │ • Normalize │    │ • Log       │    │ • Metrics   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

## Componentes Técnicos

```
┌─────────────────────────────────────────────────────────────────┐
│                        INFRAESTRUTURA                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   DOCKER        │    │   POSTGRESQL    │    │   JUPYTER       │
│                 │    │                 │    │                 │
│ • Containers    │    │ • Database      │    │ • Notebooks     │
│ • Compose       │    │ • Schema        │    │ • Analysis      │
│ • Networks      │    │ • Tables        │    │ • Visualization│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   AUTOMATION    │    │   MONITORING    │    │   DOCUMENTATION │
│                 │    │                 │    │                 │
│ • Python       │    │ • Logs          │    │ • README        │
│ • Scripts      │    │ • Metrics       │    │ • Dictionaries  │
│ • ETL          │    │ • Alerts        │    │ • Diagrams      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Tecnologias Utilizadas

### Backend
- **Python 3.8+**: Linguagem principal
- **PostgreSQL 15**: Banco de dados
- **Docker**: Containerização
- **SQLAlchemy**: ORM

### Data Processing
- **Pandas**: Manipulação de dados
- **NumPy**: Computação numérica
- **Psycopg2**: Conexão PostgreSQL

### Visualization
- **Jupyter Notebooks**: Análise interativa
- **Matplotlib**: Gráficos
- **Seaborn**: Visualizações estatísticas

### Infrastructure
- **Docker Compose**: Orquestração
- **Git**: Controle de versão
- **Logging**: Monitoramento

## Camadas de Dados

### Bronze (Raw)
- **Propósito**: Armazenamento de dados brutos
- **Formato**: CSV, JSON, etc.
- **Características**: Sem tratamento, formato original
- **Localização**: `raw/`

### Silver (Processed)
- **Propósito**: Dados limpos e estruturados
- **Formato**: PostgreSQL, Parquet
- **Características**: Validados, normalizados, enriquecidos
- **Localização**: `silver/` + PostgreSQL

### Gold (Analytics)
- **Propósito**: Dados agregados para análise
- **Formato**: Parquet, Delta Lake
- **Características**: Otimizados para consultas, agregados
- **Localização**: `gold/`

## Processo ETL

### Extract (Extração)
1. **Leitura**: Arquivo CSV em chunks
2. **Validação**: Verificação de integridade
3. **Logging**: Registro de início

### Transform (Transformação)
1. **Limpeza**: Tratamento de nulos e duplicatas
2. **Normalização**: Padronização de formatos
3. **Enriquecimento**: Criação de campos derivados
4. **Validação**: Regras de qualidade

### Load (Carregamento)
1. **Inserção**: Dados no PostgreSQL
2. **Indexação**: Criação de índices
3. **Logging**: Registro de conclusão
4. **Validação**: Verificação final

## Monitoramento e Logs

### Logs de Processamento
- **Início/Fim**: Timestamps de execução
- **Registros**: Número processado
- **Status**: Sucesso/Erro
- **Erros**: Mensagens detalhadas

### Métricas de Qualidade
- **Completude**: % de valores não nulos
- **Consistência**: Conformidade com regras
- **Precisão**: Exatidão dos dados
- **Unicidade**: Ausência de duplicatas

### Performance
- **Throughput**: Registros/segundo
- **Latência**: Tempo de resposta
- **Recursos**: CPU, Memória, I/O
- **Escalabilidade**: Capacidade de crescimento

## Segurança

### Controle de Acesso
- **Usuários**: Credenciais específicas
- **Permissões**: Níveis de acesso
- **Auditoria**: Logs de acesso

### Proteção de Dados
- **Criptografia**: Dados em trânsito
- **Backup**: Cópias de segurança
- **Recovery**: Recuperação de desastres

## Próximos Passos

1. **Expansão**: Adicionar mais fontes de dados
2. **Otimização**: Melhorar performance
3. **Visualização**: Dashboards interativos
4. **ML**: Integração com machine learning
5. **Real-time**: Processamento em tempo real
