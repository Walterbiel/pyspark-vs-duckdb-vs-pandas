# 🚀 Análise de Milhões de Linhas com PySpark, DuckDB e Pandas

Este projeto demonstra como lidar com grandes volumes de dados — 50 milhões de linhas — utilizando três tecnologias distintas: **PySpark**, **DuckDB** e **Pandas**.

O objetivo é mostrar os pontos fortes de cada abordagem para leitura, transformação e análise de dados volumosos, comparando suas **performances em um mesmo cenário**.

---

## 📦 Estrutura dos Dados

Os dados foram gerados de forma sintética com `pandas` e `numpy`, simulando uma base com 50 milhões de registros, contendo as seguintes colunas:

| Coluna     | Tipo     | Descrição                                |
|------------|----------|------------------------------------------|
| `id`       | int      | Identificador único sequencial           |
| `categoria`| str      | Categoria aleatória (`A`, `B`, `C`, `D`) |
| `valor`    | float    | Valor monetário aleatório                |
| `data`     | datetime | Datas aleatórias entre 2023 e 2025       |
| `flag`     | bool     | Valor booleano aleatório                 |

---

## 📊 Consultas Realizadas

1. **Filtro de intervalo de datas + média por categoria**
   - Selecionar registros entre `2023-06-01` e `2024-06-01`
   - Agrupar por categoria e calcular média

2. **Contagem com múltiplas condições**
   - `valor > 500`
   - `flag == True`
   - `categoria != 'C'`

3. **Agrupamento por ano e categoria**
   - Extrair o ano da data
   - Agrupar por ano e categoria
   - Calcular média e soma

4. **Janela de tempo (rolling)**
   - Para cada categoria, calcular a média móvel de 7 dias

5. **Top N com ordenação**
   - Listar os 10 maiores valores para cada categoria

> ⚠️ Mais 4 etapas serão adicionadas em breve nesta seção.

---

## 📈 Resultados

### 🔥 PySpark

| Etapa                          | Tempo (segundos)      |
|-------------------------------|------------------------|
| Leitura e preparação          | 5.10                   |
| Filtro + média                | 1.86                   |
| Contagem com condições        | 0.74                   |
| Agrupamento por ano + categoria | 1.01                 |
| Média móvel                   | 0.38                   |
| Top 10 por categoria          | 1.24                   |
| **Tempo total**               | **10.33**              |

---

### 🐼 Pandas

| Etapa                          | Tempo (segundos)      |
|-------------------------------|------------------------|
| Leitura e preparação          | 0.40                   |
| Filtro + média                | 0.06                   |
| Contagem com condições        | 0.07                   |
| Agrupamento por ano + categoria | 0.12                 |
| Média móvel                   | 0.44                   |
| Top 10 por categoria          | 0.39                   |
| **Tempo total**               | **1.48**               |

---

### 🦆 DuckDB

| Etapa                          | Tempo (segundos)      |
|-------------------------------|------------------------|
| Filtro + média                | 0.18                   |
| Contagem com condições        | 0.12                   |
| Agrupamento por ano + categoria | 0.13                 |
| Média móvel                   | 0.53                   |
| Top 10 por categoria          | 0.37                   |
| **Tempo total**               | **1.33**               |

---

## ⚖️ Comparativo entre Tecnologias

| Tecnologia | Pontos Fortes                                      | Quando Usar                                              |
|------------|----------------------------------------------------|-----------------------------------------------------------|
| **PySpark** | Escalável, ideal para clusters e Big Data          | Quando os dados ultrapassam o que cabe em memória         |
| **DuckDB**  | SQL embutido, super rápido, roda localmente        | Quando você precisa de agilidade com milhões de registros |
| **Pandas**  | Flexível, ótimo para visualizações e ajustes finais | Ideal para etapas finais ou amostras menores              |

---

## 📌 Considerações Finais

Este projeto mostra que é possível lidar com dezenas de milhões de registros **mesmo em ambiente local**, desde que se escolha a ferramenta adequada para o contexto.

Cada tecnologia tem seu papel, e **combiná-las de forma estratégica** pode trazer o melhor de cada uma: escalabilidade, velocidade e flexibilidade.

---

## ✅ Próximos Passos

- [ ] Adicionar mais 4 etapas de análise
- [ ] Incluir benchmark com paralelismo no PySpark
- [ ] Publicar resultados detalhados no Medium/LinkedIn
- [ ] Criar versão com dados reais de domínio público

---

> Projeto criado por **Walter Gonzaga - WGG Digital Solutions**  
> 📬 [LinkedIn](https://linkedin.com/in/walter-gonzaga) | 🌐 [wggsolutions.com](https://wggsolutions.com)

