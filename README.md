# Data Lakehouse - SBD-2

Este projeto implementa um Data Lakehouse completo com arquitetura em camadas (Bronze, Silver, Gold) para processamento e análise de dados.

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   BRONZE        │    │   SILVER        │    │   GOLD          │
│   (Raw Data)    │───▶│   (Processed)   │───▶│   (Analytics)   │
│                 │    │                 │    │                 │
│ • train.csv     │    │ • PostgreSQL    │    │ • Aggregations  │
│ • Raw format    │    │ • Clean data    │    │ • Reports       │
│ • No treatment │    │ • Validated     │    │ • Insights      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📁 Estrutura do Projeto

```
sbd-2/
├── 📁 docker/              # Configurações Docker
│   ├── docker-compose.yml   # Orquestração de containers
│   └── init.sql            # Scripts de inicialização
├── 📁 docs/                 # Documentação
│   ├── README.md           # Documentação principal
│   ├── modelagem_silver.md # Modelagem da camada Silver
│   └── dicionario_dados_bronze.md # Dicionário de dados
├── 📁 notebooks/            # Jupyter Notebooks
│   ├── 01_data_exploration.ipynb      # Análise Bronze
│   ├── 02_etl_raw_to_silver.ipynb    # ETL Process
│   └── 03_lakehouse_validation.ipynb  # Validação
├── 📁 raw/                  # Dados brutos (Bronze)
│   └── train.csv           # Dataset principal
├── 📁 scripts/              # Scripts de automação
│   ├── run_etl.py          # ETL principal
│   ├── run_automation.py   # Automação completa
│   └── requirements.txt    # Dependências Python
├── 📁 silver/               # Dados processados (Silver)
├── 📁 gold/                 # Dados analíticos (Gold)
├── setup.py                # Script de configuração
└── README.md               # Este arquivo
```

## 🚀 Início Rápido

### 1. Configuração Inicial

```bash
# Clone o repositório (se aplicável)
git clone <repository-url>
cd sbd-2

# Execute o setup
python setup.py
```

### 2. Executar Automação Completa

```bash
# Inicia Docker, cria banco, executa ETL
python scripts/run_automation.py
```

### 3. Acessar Recursos

- **Jupyter Notebooks**: `jupyter notebook notebooks/`
- **pgAdmin**: http://localhost:8080
- **Banco de Dados**: localhost:5432

## 📊 Camadas de Dados

### Bronze (Raw)
- **Localização**: `raw/`
- **Conteúdo**: Dados brutos sem tratamento
- **Formato**: CSV, JSON, etc.
- **Tamanho**: ~2.4 GB

### Silver (Processed)
- **Localização**: `silver/` + PostgreSQL
- **Conteúdo**: Dados limpos e estruturados
- **Formato**: PostgreSQL, Parquet
- **Qualidade**: Validada e normalizada

### Gold (Analytics)
- **Localização**: `gold/`
- **Conteúdo**: Dados agregados para análise
- **Formato**: Parquet, Delta Lake
- **Uso**: Relatórios e insights

## 🛠️ Tecnologias

- **Python**: Pandas, SQLAlchemy, Psycopg2
- **Banco de Dados**: PostgreSQL 15
- **Containerização**: Docker, Docker Compose
- **Visualização**: Jupyter Notebooks, Matplotlib, Seaborn
- **Orquestração**: Scripts Python personalizados

## 📋 Funcionalidades

### ✅ Implementado
- [x] Estrutura de pastas base
- [x] Configuração Docker com PostgreSQL
- [x] Scripts de automação
- [x] Notebooks de análise
- [x] Documentação completa
- [x] Dicionário de dados Bronze
- [x] Modelagem Silver
- [x] ETL Raw → Silver
- [x] Validação do Lakehouse

### 🔄 Em Desenvolvimento
- [ ] Camada Gold
- [ ] Dashboards interativos
- [ ] Monitoramento avançado
- [ ] Backup e recuperação

## 📖 Documentação

- [Modelagem Silver](docs/modelagem_silver.md)
- [Dicionário de Dados Bronze](docs/dicionario_dados_bronze.md)
- [Configuração Docker](docker/)

## 🔧 Configuração

### Requisitos
- Python 3.8+
- Docker e Docker Compose
- 8GB RAM recomendado
- 10GB espaço em disco

### Variáveis de Ambiente
```bash
# Banco de Dados
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sbd2_lakehouse
DB_USER=sbd2_user
DB_PASSWORD=sbd2_password

# pgAdmin
PGADMIN_EMAIL=admin@sbd2.com
PGADMIN_PASSWORD=admin123
```

## 📊 Monitoramento

### Logs
- **Automação**: `automation.log`
- **ETL**: `etl.log`
- **Docker**: `docker logs sbd2_postgres`

### Métricas
- Registros processados
- Tempo de execução
- Qualidade dos dados
- Performance do banco

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Equipe

- **Desenvolvedor**: Equipe SBD-2
- **Data**: 10/10/2025
- **Versão**: 1.0.0

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a documentação
2. Consulte os logs
3. Abra uma issue no repositório

---

**Data Lakehouse SBD-2** - Transformando dados brutos em insights valiosos! 🚀
