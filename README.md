# 🚀 Análise com 100 Milhões de Linhas — PySpark vs DuckDB vs Pandas

Este projeto demonstra como lidar com grandes volumes de dados utilizando três tecnologias distintas: **PySpark**, **DuckDB** e **Pandas**.

O objetivo é destacar os pontos fortes de cada abordagem na leitura, transformação e análise de dados volumosos, **comparando suas performances em um mesmo cenário**.

---

## 📦 Estrutura dos Dados

Os dados foram gerados de forma sintética com `pandas` e `numpy`, simulando uma base com até **100 milhões de registros**, contendo as seguintes colunas:

| Coluna      | Tipo     | Descrição                                |
|-------------|----------|------------------------------------------|
| `id`        | int      | Identificador único sequencial           |
| `categoria` | str      | Categoria aleatória (`A`, `B`, `C`, `D`) |
| `valor`     | float    | Valor monetário aleatório                |
| `data`      | datetime | Datas aleatórias entre 2023 e 2025       |
| `flag`      | bool     | Valor booleano aleatório                 |

---

## 📊 Consultas Realizadas

1. **Filtro por intervalo de datas + média por categoria**
2. **Contagem com múltiplas condições**
3. **Agrupamento por ano e categoria**
4. **Média móvel (Janela de tempo)**
5. **Top 10 por categoria**

---

## 📈 Resultados — 1 Milhão de Linhas

### 🔥 PySpark

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Leitura e preparação             | 5.10      |
| Filtro + média                   | 1.86      |
| Contagem com condições           | 0.74      |
| Agrupamento por ano + categoria  | 1.01      |
| Média móvel                      | 0.38      |
| Top 10 por categoria             | 1.24      |
| **Tempo total**                  | **10.33** |

### 🐼 Pandas

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Leitura e preparação             | 0.40      |
| Filtro + média                   | 0.06      |
| Contagem com condições           | 0.07      |
| Agrupamento por ano + categoria  | 0.12      |
| Média móvel                      | 0.44      |
| Top 10 por categoria             | 0.39      |
| **Tempo total**                  | **1.48**  |

### 🦆 DuckDB

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Filtro + média                   | 0.18      |
| Contagem com condições           | 0.12      |
| Agrupamento por ano + categoria  | 0.13      |
| Média móvel                      | 0.53      |
| Top 10 por categoria             | 0.37      |
| **Tempo total**                  | **1.33**  |

---

## 📈 Resultados — 10 Milhões de Linhas

### 🔥 PySpark

| Etapa                            | Tempo (s)      |
|----------------------------------|----------------|
| Leitura e preparação             | 3.69           |
| Filtro + média                   | 3.23           |
| Contagem com condições           | 2.02           |
| Agrupamento por ano + categoria  | 3.15           |
| Média móvel                      | 0.67           |
| Top 10 por categoria             | 4.47           |
| **Tempo total**                  | **17.23**      |

### 🐼 Pandas

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Leitura e preparação             | 3.52      |
| Filtro + média                   | 0.41      |
| Contagem com condições           | 0.50      |
| Agrupamento por ano + categoria  | 0.93      |
| Média móvel                      | 5.04      |
| Top 10 por categoria             | 4.66      |
| **Tempo total**                  | **15.05** |

### 🦆 DuckDB

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Filtro + média                   | 0.51      |
| Contagem com condições           | 0.46      |
| Agrupamento por ano + categoria  | 0.48      |
| Média móvel                      | 5.50      |
| Top 10 por categoria             | 3.70      |
| **Tempo total**                  | **10.83** |

---

## 📈 Resultados — 50 Milhões de Linhas

### 🔥 PySpark

| Etapa                            | Tempo (s)     |
|----------------------------------|---------------|
| Leitura e preparação             | 18.33         |
| Filtro + média                   | 17.46         |
| Contagem com condições           | 10.33         |
| Agrupamento por ano + categoria  | 24.12         |
| Média móvel                      | 5.38          |
| Top 10 por categoria             | 36.55         |
| **Tempo total**                  | **112.16**    |

### 🐼 Pandas

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Leitura e preparação             | 19.70     |
| Filtro + média                   | 2.33      |
| Contagem com condições           | 2.84      |
| Agrupamento por ano + categoria  | 5.27      |
| Média móvel                      | 27.38     |
| Top 10 por categoria             | 26.11     |
| **Tempo total**                  | **83.64** |

### 🦆 DuckDB

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Filtro + média                   | 2.27      |
| Contagem com condições           | 2.11      |
| Agrupamento por ano + categoria  | 2.26      |
| Média móvel                      | 30.71     |
| Top 10 por categoria             | 22.88     |
| **Tempo total**                  | **60.23** |

---

## 📈 Resultados — 100 Milhões de Linhas

### 🔥 PySpark

| Etapa                            | Tempo (s)     |
|----------------------------------|---------------|
| Leitura e preparação             | 37.37         |
| Filtro + média                   | 35.93         |
| Contagem com condições           | 21.73         |
| Agrupamento por ano + categoria  | 48.22         |
| Média móvel                      | 10.60         |
| Top 10 por categoria             | 78.32         |
| **Tempo total**                  | **232.17**    |

### 🐼 Pandas

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Leitura e preparação             | 44.28     |
| Filtro + média                   | 4.79      |
| Contagem com condições           | 6.18      |
| Agrupamento por ano + categoria  | 11.14     |
| Média móvel                      | 64.97     |
| Top 10 por categoria             | 57.38     |
| **Tempo total**                  | **188.76** |

### 🦆 DuckDB

| Etapa                            | Tempo (s) |
|----------------------------------|-----------|
| Filtro + média                   | 5.15      |
| Contagem com condições           | 4.18      |
| Agrupamento por ano + categoria  | 4.56      |
| Média móvel                      | 86.12     |
| Top 10 por categoria             | 61.36     |
| **Tempo total**                  | **161.37** |

---

![output](https://github.com/user-attachments/assets/2a7f3377-5d32-4c15-bd75-b7bf107c96e4)


## ⚖️ Comparativo entre Tecnologias

| Tecnologia | Pontos Fortes                                       | Quando Usar                                                  |
|------------|------------------------------------------------------|---------------------------------------------------------------|
| **PySpark**| Altamente escalável, ideal para clusters e Big Data  | Quando os dados excedem a capacidade de memória               |
| **DuckDB** | Extremamente rápido, executa localmente com SQL puro | Quando é preciso performance local em datasets grandes        |
| **Pandas** | Flexível e excelente para ajustes e visualizações    | Ideal para análises pontuais, protótipos e dados menores      |

---

## 📌 Considerações Finais

Este projeto demonstra que é possível lidar com dezenas — ou até centenas — de milhões de registros **mesmo em ambiente local**, desde que a tecnologia certa seja escolhida para o cenário adequado.

Cada ferramenta tem seus pontos fortes. **Combiná-las estrategicamente** permite tirar o melhor proveito de cada uma: **escalabilidade, velocidade e flexibilidade**.

---

> Projeto desenvolvido por **Walter Gonzaga — WGG Digital Solutions**  
> 📬 [LinkedIn](https://linkedin.com/in/walter-gonzaga) | 🌐 [wggsolutions.com](https://wggsolutions.com)
