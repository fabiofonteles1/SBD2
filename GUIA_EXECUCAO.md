# 🚀 GUIA DE EXECUÇÃO - DATA LAKEHOUSE SBD-2

## 📋 VISÃO GERAL

Este guia apresenta o passo a passo completo para executar o projeto Data Lakehouse, desde a configuração inicial até a validação final do sistema.

---

## 🎯 OBJETIVOS DO PROJETO

O projeto implementa um Data Lakehouse com arquitetura em camadas:
- **Bronze (Raw)**: Dados brutos sem tratamento
- **Silver (Processed)**: Dados limpos e estruturados
- **Gold (Analytics)**: Dados agregados para análise

---

## 📋 PRÉ-REQUISITOS

### Software Necessário
- **Python 3.8+** (recomendado 3.9 ou superior)
- **Docker Desktop** (versão 20.10+)
- **Git** (para controle de versão)
- **8GB RAM** (mínimo recomendado)
- **10GB espaço em disco** (para dados e containers)

### Verificação dos Pré-requisitos
```bash
# Verificar Python
python --version

# Verificar Docker
docker --version

# Verificar Git
git --version
```

---

## 🛠️ CONFIGURAÇÃO INICIAL

### Passo 1: Navegar para o Diretório do Projeto
```bash
cd "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2"
```

### Passo 2: Verificar Estrutura do Projeto
```bash
# Listar arquivos e pastas
dir

# Verificar se o arquivo de dados existe
dir raw\train.csv
```

**Estrutura esperada:**
```
sbd-2/
├── docker/
├── docs/
├── notebooks/
├── raw/
│   └── train.csv (2.4GB)
├── scripts/
├── README.md
├── setup.py
└── run_all.py
```

---

## 🚀 EXECUÇÃO AUTOMÁTICA (RECOMENDADO)

### Opção 1: Execução Completa em Uma Etapa
```bash
# Executa setup, validação e automação
python run_all.py
```

**O que este comando faz:**
1. ✅ Verifica pré-requisitos
2. ✅ Instala dependências Python
3. ✅ Cria estrutura de diretórios
4. ✅ Configura repositório Git
5. ✅ Valida configuração
6. ✅ Inicia containers Docker
7. ✅ Executa ETL completo
8. ✅ Valida lakehouse

---

## 🔧 EXECUÇÃO MANUAL (PASSO A PASSO)

### Etapa 1: Setup do Projeto
```bash
# Executa configuração inicial
python setup.py
```

**O que acontece:**
- Verifica Python e Docker
- Instala dependências (`pandas`, `psycopg2`, `sqlalchemy`, etc.)
- Cria diretórios necessários (`silver/`, `gold/`, `logs/`, `output/`)
- Configura repositório Git
- Faz commit inicial

**Saída esperada:**
```
=== SETUP DO PROJETO DATA LAKEHOUSE ===
✓ Python 3.9 encontrado
✓ Docker 20.10 disponível
✓ Dependências instaladas
✓ Diretórios criados
✓ Git configurado
=== SETUP CONCLUÍDO ===
```

### Etapa 2: Validação do Setup
```bash
# Valida se tudo está configurado corretamente
python scripts/validate_setup.py
```

**O que é verificado:**
- ✅ Estrutura de arquivos
- ✅ Docker funcionando
- ✅ Containers rodando
- ✅ Conexão com banco de dados
- ✅ Tabelas Silver criadas
- ✅ Arquivo de dados presente
- ✅ Pacotes Python instalados

**Saída esperada:**
```
=== INICIANDO VALIDAÇÃO DO SETUP ===
✓ Estrutura de arquivos OK
✓ Docker disponível
✓ Container PostgreSQL rodando
✓ Conexão com banco de dados OK
✓ Tabelas Silver OK: ['train_data', 'data_metadata', 'processing_logs']
✓ Arquivo de dados OK: 2.40 GB
✓ Pacotes Python OK
🎉 SETUP VALIDADO COM SUCESSO!
```

### Etapa 3: Automação Completa
```bash
# Executa ETL e popula o lakehouse
python scripts/run_automation.py
```

**Processo detalhado:**

#### 3.1 Inicialização do Docker
```bash
# Para containers existentes
docker-compose -f docker/docker-compose.yml down

# Inicia serviços
docker-compose -f docker/docker-compose.yml up -d
```

**Containers criados:**
- `sbd2_postgres`: Banco PostgreSQL 15
- `sbd2_pgadmin`: Interface web pgAdmin

#### 3.2 Criação do Banco de Dados
- Executa script `docker/init.sql`
- Cria schema `silver`
- Cria tabelas: `train_data`, `data_metadata`, `processing_logs`
- Configura índices e constraints

#### 3.3 Processamento ETL
- Lê arquivo `raw/train.csv` (2.4GB)
- Processa em chunks para otimizar memória
- Aplica transformações de limpeza
- Insere dados no PostgreSQL
- Registra logs de processamento

**Saída esperada:**
```
=== INICIANDO AUTOMAÇÃO COMPLETA ===
✓ Docker verificado
✓ Containers iniciados
✓ Banco de dados disponível
✓ ETL executado com sucesso
✓ Lakehouse validado
=== AUTOMAÇÃO CONCLUÍDA COM SUCESSO ===
```

---

## 📊 ACESSO AOS RECURSOS

### 1. Jupyter Notebooks
```bash
# Iniciar Jupyter
jupyter notebook notebooks/

# Ou usar VS Code
code notebooks/
```

**Notebooks disponíveis:**
- `01_data_exploration.ipynb`: Análise dos dados brutos
- `02_etl_raw_to_silver.ipynb`: Processo ETL
- `03_lakehouse_validation.ipynb`: Validação final

### 2. pgAdmin (Interface Web)
- **URL**: http://localhost:8080
- **Email**: admin@sbd2.com
- **Senha**: admin123

**Configuração do servidor:**
- **Host**: postgres (ou localhost)
- **Port**: 5432
- **Database**: sbd2_lakehouse
- **Username**: sbd2_user
- **Password**: sbd2_password

### 3. Conexão Direta ao Banco
```python
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='sbd2_lakehouse',
    user='sbd2_user',
    password='sbd2_password'
)
```

---

## 🔍 MONITORAMENTO E LOGS

### Logs de Execução
```bash
# Logs de automação
type automation.log

# Logs de ETL
type etl.log

# Logs de validação
type validation_report.txt
```

### Logs do Docker
```bash
# Logs do PostgreSQL
docker logs sbd2_postgres

# Logs do pgAdmin
docker logs sbd2_pgadmin

# Status dos containers
docker ps
```

### Métricas de Performance
- **Registros processados**: Verificar em `silver.processing_logs`
- **Tempo de execução**: Logs de início/fim
- **Qualidade dos dados**: Estatísticas no banco
- **Uso de recursos**: Monitor do sistema

---

## 🛠️ TROUBLESHOOTING

### Problema 1: Docker não inicia
**Sintomas:**
```
Error: Docker not running
```

**Solução:**
1. Verificar se Docker Desktop está rodando
2. Reiniciar Docker Desktop
3. Verificar recursos disponíveis (RAM/CPU)

### Problema 2: Erro de conexão com banco
**Sintomas:**
```
psycopg2.OperationalError: connection refused
```

**Solução:**
1. Verificar se container está rodando: `docker ps`
2. Aguardar inicialização: `docker logs sbd2_postgres`
3. Verificar porta 5432: `netstat -an | findstr 5432`

### Problema 3: Arquivo de dados não encontrado
**Sintomas:**
```
FileNotFoundError: raw/train.csv not found
```

**Solução:**
1. Verificar se arquivo existe: `dir raw\train.csv`
2. Verificar permissões de leitura
3. Verificar espaço em disco

### Problema 4: Dependências Python não instaladas
**Sintomas:**
```
ModuleNotFoundError: No module named 'pandas'
```

**Solução:**
```bash
# Instalar dependências
pip install -r scripts/requirements.txt

# Ou instalar individualmente
pip install pandas psycopg2-binary sqlalchemy
```

---

## 📈 VALIDAÇÃO DO SUCESSO

### 1. Verificar Containers
```bash
docker ps
```
**Saída esperada:**
```
CONTAINER ID   IMAGE                STATUS
abc123def456   postgres:15          Up 2 hours
def456ghi789   dpage/pgadmin4      Up 2 hours
```

### 2. Verificar Banco de Dados
```sql
-- Conectar ao banco e executar:
SELECT table_name FROM information_schema.tables WHERE table_schema = 'silver';
```
**Resultado esperado:**
```
train_data
data_metadata
processing_logs
```

### 3. Verificar Logs de Processamento
```sql
SELECT process_name, status, records_processed, completed_at 
FROM silver.processing_logs 
ORDER BY completed_at DESC;
```

### 4. Verificar Dados Processados
```sql
SELECT COUNT(*) as total_records FROM silver.train_data;
```

---

## 🔄 COMANDOS ÚTEIS

### Gerenciamento de Containers
```bash
# Parar todos os containers
docker-compose -f docker/docker-compose.yml down

# Iniciar containers
docker-compose -f docker/docker-compose.yml up -d

# Reiniciar containers
docker-compose -f docker/docker-compose.yml restart

# Ver logs em tempo real
docker-compose -f docker/docker-compose.yml logs -f
```

### Limpeza do Sistema
```bash
# Parar e remover containers
docker-compose -f docker/docker-compose.yml down -v

# Limpar volumes Docker
docker volume prune

# Limpar logs
del automation.log etl.log validation_report.txt
```

### Backup e Restauração
```bash
# Backup do banco
docker exec sbd2_postgres pg_dump -U sbd2_user sbd2_lakehouse > backup.sql

# Restaurar banco
docker exec -i sbd2_postgres psql -U sbd2_user sbd2_lakehouse < backup.sql
```

---

## 📚 PRÓXIMOS PASSOS

### 1. Análise dos Dados
- Execute os notebooks em `notebooks/`
- Explore os dados com visualizações
- Identifique padrões e insights

### 2. Expansão do Sistema
- Adicione mais fontes de dados
- Implemente camada Gold
- Crie dashboards interativos

### 3. Otimização
- Ajuste parâmetros de performance
- Implemente cache
- Configure monitoramento avançado

### 4. Documentação
- Atualize dicionários de dados
- Documente regras de negócio
- Crie guias de usuário

---

## 🆘 SUPORTE

### Em Caso de Problemas
1. **Verificar logs**: `automation.log`, `etl.log`
2. **Validar setup**: `python scripts/validate_setup.py`
3. **Reiniciar sistema**: `python run_all.py`
4. **Consultar documentação**: `docs/README.md`

### Contatos
- **Equipe**: SBD-2
- **Data**: 10/10/2025
- **Versão**: 1.0.0

---

## 🎉 CONCLUSÃO

Este guia fornece todas as informações necessárias para executar o projeto Data Lakehouse SBD-2 com sucesso. O sistema está projetado para ser robusto, escalável e fácil de usar.

**Lembre-se**: Sempre verifique os logs e monitore o sistema durante a execução para garantir que tudo está funcionando corretamente.

---

*Data Lakehouse SBD-2 - Transformando dados brutos em insights valiosos! 🚀*
