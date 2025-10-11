# Dicionário de Dados - Camada Bronze

## Visão Geral

Este documento descreve a estrutura e características dos dados brutos (camada Bronze) do projeto Data Lakehouse.

## Arquivo de Dados

- **Nome**: `train.csv`
- **Localização**: `raw/train.csv`
- **Tamanho**: ~2.4 GB
- **Formato**: CSV (Comma Separated Values)
- **Encoding**: UTF-8

## Estrutura dos Dados

### Informações Gerais
- **Número de colunas**: A ser determinado após análise
- **Número de registros**: A ser determinado após análise
- **Separador**: Vírgula (,)
- **Delimitador de texto**: Aspas duplas (")

### Metadados do Arquivo
- **Data de criação**: 10/10/2025
- **Fonte**: Dataset de treino
- **Propósito**: Análise e modelagem de dados
- **Qualidade**: Dados brutos, sem tratamento

## Análise de Qualidade

### Métricas de Qualidade
- **Completude**: A ser calculada
- **Consistência**: A ser avaliada
- **Precisão**: A ser verificada
- **Unicidade**: A ser analisada

### Problemas Identificados
- A ser documentado após análise completa

## Estrutura das Colunas

*Nota: Esta seção será preenchida após a execução do notebook de análise exploratória*

### Coluna 1
- **Nome**: A ser determinado
- **Tipo**: A ser determinado
- **Descrição**: A ser documentada
- **Valores únicos**: A ser contado
- **Valores nulos**: A ser verificado

### Coluna 2
- **Nome**: A ser determinado
- **Tipo**: A ser determinado
- **Descrição**: A ser documentada
- **Valores únicos**: A ser contado
- **Valores nulos**: A ser verificado

*[Esta seção será expandida conforme a análise dos dados]*

## Regras de Negócio

### Validações Necessárias
1. Verificação de tipos de dados
2. Detecção de valores nulos
3. Identificação de outliers
4. Validação de formatos

### Transformações Planejadas
1. Limpeza de dados
2. Normalização
3. Enriquecimento
4. Validação final

## Próximos Passos

1. **Executar análise exploratória**: Notebook `01_data_exploration.ipynb`
2. **Documentar estrutura completa**: Atualizar este dicionário
3. **Definir regras de transformação**: Para camada Silver
4. **Implementar ETL**: Processo Raw → Silver

## Contatos

- **Responsável**: Equipe SBD-2
- **Data de atualização**: 10/10/2025
- **Versão**: 1.0

---

*Este documento será atualizado conforme a análise dos dados progride.*
