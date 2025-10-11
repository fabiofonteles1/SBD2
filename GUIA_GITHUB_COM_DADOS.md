# 🚀 GUIA PARA SUBIR O PROJETO COMPLETO NO GITHUB (COM DADOS RAW)

## 📋 INCLUINDO A BASE DE DADOS RAW

Como o professor pede a base de dados raw no GitHub, vamos usar **Git LFS** para gerenciar o arquivo grande (2.4 GB).

---

## 🛠️ **CONFIGURAÇÃO COM GIT LFS**

### Passo 1: Instalar Git LFS
```bash
# Baixar e instalar Git LFS
# Acesse: https://git-lfs.github.io/
# Ou use o instalador automático:
git lfs install
```

### Passo 2: Configurar Git LFS para Arquivos CSV
```bash
# Navegar para o projeto
cd "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2"

# Configurar Git LFS para arquivos CSV
git lfs track "*.csv"
git lfs track "raw/*.csv"

# Adicionar .gitattributes
git add .gitattributes
```

### Passo 3: Configurar .gitignore (sem excluir dados)
```bash
# Criar .gitignore sem excluir dados raw
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".DS_Store" >> .gitignore
echo "venv/" >> .gitignore
echo ".env" >> .gitignore
```

---

## 🚀 **PROCESSO COMPLETO**

### **OPÇÃO 1: NOVO REPOSITÓRIO (RECOMENDADA)**

#### Passo 1: Criar Repositório no GitHub
1. **Acesse**: https://github.com
2. **Clique**: "New repository"
3. **Nome**: `data-lakehouse-sbd2`
4. **Descrição**: "Data Lakehouse SBD-2 - Projeto completo com dados raw"
5. **Visibilidade**: Public ou Private
6. **NÃO marque**: "Add a README file"
7. **Clique**: "Create repository"

#### Passo 2: Preparar o Projeto Local
```bash
# 1. Navegar para o projeto
cd "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2"

# 2. Inicializar Git LFS
git lfs install

# 3. Configurar tracking para arquivos grandes
git lfs track "*.csv"
git lfs track "raw/*.csv"
git lfs track "*.parquet"
git lfs track "*.xlsx"

# 4. Configurar .gitignore
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
echo ".DS_Store" >> .gitignore
echo "venv/" >> .gitignore
echo ".env" >> .gitignore

# 5. Adicionar .gitattributes
git add .gitattributes
```

#### Passo 3: Adicionar Todos os Arquivos
```bash
# Adicionar todos os arquivos (incluindo train.csv)
git add .

# Verificar status
git status
```

#### Passo 4: Commit e Push
```bash
# Fazer commit inicial
git commit -m "Initial commit: Data Lakehouse SBD-2 with raw data (2.4GB)"

# Adicionar remote origin
git remote add origin https://github.com/seu-usuario/data-lakehouse-sbd2.git

# Fazer push (pode demorar devido ao arquivo grande)
git push -u origin main
```

---

## 🔄 **OPÇÃO 2: USAR GIT EXISTENTE**

Se já tem Git inicializado:

```bash
# 1. Navegar para o projeto
cd "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2"

# 2. Configurar Git LFS
git lfs install
git lfs track "*.csv"
git lfs track "raw/*.csv"

# 3. Configurar .gitignore
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore

# 4. Adicionar arquivos
git add .

# 5. Commit
git commit -m "Data Lakehouse SBD-2 with raw data (2.4GB)"

# 6. Adicionar remote
git remote add origin https://github.com/seu-usuario/data-lakehouse-sbd2.git

# 7. Push
git push -u origin main
```

---

## 📁 **ESTRUTURA FINAL NO GITHUB**

```
data-lakehouse-sbd2/
├── 📁 docker/
│   ├── docker-compose.yml
│   └── init.sql
├── 📁 docs/
│   ├── README.md
│   ├── modelagem_silver.md
│   ├── dicionario_dados_bronze.md
│   └── arquitetura.md
├── 📁 notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_etl_raw_to_silver.ipynb
│   └── 03_lakehouse_validation.ipynb
├── 📁 raw/
│   └── train.csv (2.4GB) ← INCLUÍDO COM GIT LFS
├── 📁 scripts/
│   ├── run_etl.py
│   ├── run_automation.py
│   ├── validate_setup.py
│   └── requirements.txt
├── 📁 silver/ (pasta vazia)
├── 📁 gold/ (pasta vazia)
├── 📄 README.md
├── 📄 setup.py
├── 📄 run_all.py
├── 📄 .gitignore
├── 📄 .gitattributes ← CONFIGURADO PARA GIT LFS
└── 📄 GUIA_EXECUCAO.md
```

---

## ⚠️ **CONSIDERAÇÕES IMPORTANTES**

### **Tamanho do Repositório**
- **Com dados raw**: ~2.5 GB
- **Sem dados raw**: ~50 MB
- **Git LFS**: Gerencia arquivos grandes eficientemente

### **Limitações do GitHub**
- **Repositórios gratuitos**: 1 GB (Git LFS resolve)
- **Git LFS gratuito**: 1 GB/mês
- **Para arquivos maiores**: Considere GitHub Pro ou alternativas

### **Alternativas se Git LFS não funcionar**
1. **Comprimir o arquivo**:
   ```bash
   # Comprimir train.csv
   gzip train.csv
   # Resultado: train.csv.gz (menor)
   ```

2. **Dividir o arquivo**:
   ```bash
   # Dividir em partes menores
   split -b 500M train.csv train_part_
   ```

3. **Usar serviços de armazenamento**:
   - Google Drive
   - Dropbox
   - OneDrive
   - Incluir link no README

---

## 🚀 **COMANDOS RÁPIDOS**

### **Configuração Completa**
```bash
# 1. Navegar para o projeto
cd "C:\Users\fabio\OneDrive\Área de Trabalho\sbd-2"

# 2. Configurar Git LFS
git lfs install
git lfs track "*.csv"
git lfs track "raw/*.csv"

# 3. Configurar .gitignore
echo "*.log" >> .gitignore
echo "__pycache__/" >> .gitignore

# 4. Adicionar todos os arquivos
git add .

# 5. Commit
git commit -m "Data Lakehouse SBD-2 with raw data (2.4GB)"

# 6. Adicionar remote (substitua pela sua URL)
git remote add origin https://github.com/seu-usuario/data-lakehouse-sbd2.git

# 7. Push
git push -u origin main
```

---

## 📝 **README.md ATUALIZADO**

```markdown
# 🏗️ Data Lakehouse SBD-2

Projeto completo de Data Lakehouse com arquitetura em camadas (Bronze → Silver → Gold).

## 📊 Dados Incluídos

- **train.csv**: 2.4 GB de dados brutos
- **Formato**: CSV (Comma Separated Values)
- **Gerenciamento**: Git LFS para arquivos grandes

## 🚀 Início Rápido

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/data-lakehouse-sbd2.git
cd data-lakehouse-sbd2

# Execute o projeto
python run_all.py
```

## ⚠️ Nota sobre Dados

Este repositório inclui dados brutos de 2.4 GB gerenciados com Git LFS.
Para clonar completamente:

```bash
git lfs pull
```

## 📚 Documentação

- [Guia de Execução](GUIA_EXECUCAO.md)
- [Comandos Windows](COMANDOS_WINDOWS.md)
- [Checklist Completo](CHECKLIST_COMPLETO.md)
```

---

## ✅ **VERIFICAÇÃO FINAL**

Após subir no GitHub, verifique:

1. **✅ Todos os arquivos estão presentes**
2. **✅ train.csv está visível (com ícone LFS)**
3. **✅ README.md está visível**
4. **✅ Estrutura de pastas está correta**
5. **✅ .gitattributes está configurado**
6. **✅ Documentação está acessível**

---

## 🎯 **RECOMENDAÇÃO FINAL**

**Use a OPÇÃO 1 (Novo repositório)** porque:
- ✅ Controle total sobre configuração
- ✅ Git LFS configurado desde o início
- ✅ Evita problemas com Git existente
- ✅ Inclui todos os dados conforme solicitado

**O professor terá acesso completo ao projeto com dados raw! 🚀**
