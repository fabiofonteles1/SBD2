# Análise de Dados - Microsoft Security Incident Prediction

Este projeto contém uma análise exploratória de dados do dataset da competição Microsoft Security Incident Prediction do Kaggle.

## 📋 Pré-requisitos

- Python 3.13
- pip (gerenciador de pacotes Python)

## 🚀 Instalação

1. **Clone ou baixe este repositório**

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual:**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Como executar

1. **Inicie o Jupyter Notebook:**
   ```bash
   jupyter notebook
   ```

2. **Abra o arquivo `raw/train_analytics.ipynb`**

3. **Execute as células sequencialmente**

## 📁 Estrutura do Projeto

```
sbd2/
├── silver/
│   ├── security_analytics.ipynb     # Notebook de análise
│   └── Dicionário_de_Dados_silver.md  # Documentação dos dados
│   ├── mer-der-dld-dicionario-silver     # Documentação do Banco de Dados
│   └── security_analytics.md  # Explicação da Análise em markdown
│   ├── security_ddl     # Arquivo com a criação da tabela
│   └── security_der_dld # Diagrama entidade relacionamento e dld
│   ├── security_incident_prediction_silver.csv     # Arquivo csv da camada silver ( já com tratamento)
├── raw/
│   ├── train.csv                 # Dataset principal
│   ├── train_analytics.ipynb     # Notebook de análise
│   └── Dicionário_de_Dados_train.csv.md  # Documentação dos dados
├── transformer/
│   ├── etl/
│   ├── ETL_Security_Incident_Prediction.md # arquivo explicativo
│   ├── raw_to_silver_security.ipynb # Notebook Jupyter que executa o etl raw to silver
├── requirements.txt              # Dependências do projeto
├── docker-compose              # Docker Compose do Projeto
└── README.md                     # Este arquivo
```

## 📚 Bibliotecas Principais Utilizadas

- **pandas**: Manipulação e análise de dados
- **numpy**: Computação numérica
- **matplotlib**: Visualização de dados
- **seaborn**: Visualizações estatísticas avançadas
- **jupyter**: Ambiente de notebook interativo

## ⚠️ Observações Importantes

- O dataset `train.csv` deve estar presente na pasta `raw/` para que o notebook funcione corretamente
- O dataset é grande e pode consumir bastante memória RAM
- Certifique-se de ter pelo menos 8GB de RAM disponível para uma execução fluida
- Caso de problema no arquivo csv, baixe diretamente do site: https://www.kaggle.com/datasets/Microsoft/microsoft-security-incident-prediction , o utilizado na análise e o GUIDE.train.csv

## 🐛 Solução de Problemas

### Erro de memória:
Se você encontrar problemas de memória, considere:
- Usar um subset menor dos dados para testes
- Fechar outras aplicações que consomem muita RAM
- Usar `low_memory=False` no `pd.read_csv()` (já configurado)

### Problemas com encoding:
Se houver problemas com caracteres especiais, certifique-se de que o arquivo CSV está em UTF-8.
