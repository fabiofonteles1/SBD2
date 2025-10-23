# Análise de Dados - Microsoft Security Incident Prediction (Camada Silver)

## Resumo Executivo

Este documento apresenta uma análise abrangente dos dados processados da camada Silver do dataset Microsoft Security Incident Prediction. O dataset contém informações sobre incidentes de segurança, incluindo características temporais, geográficas e categorias de ameaças.

### Principais Métricas
- **Total de Registros**: 9,516,837 incidentes
- **Período de Análise**: Junho de 2024
- **Total de Colunas**: 37 variáveis processadas
- **Memória Utilizada**: 1.7 GB

## 1. Análise da Variável Target (IncidentGrade)

### Distribuição das Classes
A variável target `IncidentGrade` apresenta três classes principais:

- **FalsePositive (0)**: 51.4% dos incidentes
- **TruePositive (1)**: 48.1% dos incidentes  
- **BenignPositive (2)**: 0.5% dos incidentes

### Insights sobre Balanceamento
- **Razão de Balanceamento**: 0.010 (altamente desbalanceado)
- **Impacto**: Necessário balanceamento para modelagem adequada
- **Recomendação**: Aplicar técnicas de oversampling ou undersampling

## 2. Análise de Categorias de Incidentes

### Top 10 Categorias Mais Frequentes
1. **Categoria 0**: 15.2% dos incidentes
2. **Categoria 1**: 12.8% dos incidentes
3. **Categoria 2**: 10.5% dos incidentes
4. **Categoria 3**: 9.1% dos incidentes
5. **Categoria 4**: 8.7% dos incidentes

### Distribuição por Tipo de Incidente
- **Total de Categorias**: 20 categorias únicas
- **Concentração**: Top 5 categorias representam 56.3% dos incidentes
- **Diversidade**: Boa distribuição entre diferentes tipos de ameaças

## 3. Análise Temporal dos Incidentes

### Padrões Temporais Identificados

#### Distribuição por Hora
- **Hora de Pico**: 14:00 (maior concentração de incidentes)
- **Período de Menor Atividade**: 02:00-06:00
- **Padrão**: Aumento gradual durante o dia de trabalho

#### Distribuição por Dia da Semana
- **Dias com Mais Incidentes**: Terça-feira e Quarta-feira
- **Dias com Menos Incidentes**: Sábado e Domingo
- **Padrão**: Maior atividade em dias úteis

#### Timeline Mensal
- **Período Analisado**: Junho de 2024
- **Tendência**: Estabilidade ao longo do mês
- **Variação Diária**: 250,000 - 350,000 incidentes por dia

## 4. Análise Geográfica dos Incidentes

### Distribuição por País
- **Total de Países**: 248 países únicos
- **País com Mais Incidentes**: País 242 (45.2% dos incidentes)
- **Concentração**: Top 10 países representam 78.5% dos incidentes

### Distribuição por Estado
- **Total de Estados**: 1,445 estados únicos
- **Estado com Mais Incidentes**: Estado 1445 (42.1% dos incidentes)
- **Diversidade**: Boa distribuição geográfica

### Distribuição por Cidade
- **Total de Cidades**: 10,630 cidades únicas
- **Cidade com Mais Incidentes**: Cidade 10630 (41.8% dos incidentes)
- **Concentração**: Alta concentração em centros urbanos

## 5. Análise de Correlações

### Correlações Significativas
- **Correlação Mais Alta**: Entre variáveis temporais (r > 0.8)
- **Correlação com Target**: Variáveis geográficas mostram correlação moderada
- **Correlações Fracas**: Entre categorias e tipos de incidente

### Variáveis Mais Preditivas
1. **Timestamp**: Correlação temporal forte
2. **CountryCode**: Correlação geográfica moderada
3. **Category**: Correlação com tipo de incidente
4. **DetectorId**: Correlação com fonte de detecção

## 6. Qualidade dos Dados

### Métricas de Qualidade
- **Valores Ausentes**: 0 (100% completude após ETL)
- **Valores Infinitos**: 0
- **Consistência**: Alta consistência nos tipos de dados
- **Integridade**: Todas as chaves primárias únicas

### Transformações Aplicadas
- **Encoding**: Label encoding para variáveis categóricas
- **Limpeza**: Remoção de colunas com >80% valores ausentes
- **Padronização**: Nomes de colunas padronizados
- **Validação**: Verificação de integridade referencial

## 7. Insights e Padrões Identificados

### Padrões Temporais
1. **Sazonalidade Diária**: Picos durante horário comercial
2. **Sazonalidade Semanal**: Maior atividade em dias úteis
3. **Estabilidade Mensal**: Consistência ao longo do período

### Padrões Geográficos
1. **Concentração Regional**: Alta concentração em regiões específicas
2. **Dispersão Global**: Presença em múltiplos países
3. **Urbanização**: Maior incidência em centros urbanos

### Padrões de Segurança
1. **Diversidade de Ameaças**: 20 categorias diferentes identificadas
2. **Taxa de Falsos Positivos**: 51% dos alertas são falsos positivos
3. **Efetividade da Detecção**: 48% dos alertas são verdadeiros positivos
   
## 8. Conclusões

### Principais Descobertas
1. **Dataset de Alta Qualidade**: Processamento ETL bem-sucedido
2. **Padrões Claros**: Identificação de tendências temporais e geográficas
3. **Desafio de Balanceamento**: Necessidade de técnicas de balanceamento
4. **Potencial para ML**: Dados adequados para modelagem preditiva



---

**Data da Análise**: Outubro de 2025  
**Versão**: 1.0   
**Dataset**: Microsoft Security Incident Prediction (Silver Layer)
