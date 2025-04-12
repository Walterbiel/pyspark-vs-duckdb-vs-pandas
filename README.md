# 🚀 Análise de 50 Milhões de Linhas com PySpark, DuckDB e Pandas

Este projeto demonstra como lidar com grandes volumes de dados (50 milhões de linhas) utilizando três tecnologias diferentes: **PySpark**, **DuckDB** e **Pandas**.

A ideia é mostrar os pontos fortes de cada abordagem para leitura, transformação e análise de dados volumosos — e comparar suas performances em um cenário comum.

---

## 📦 Estrutura dos Dados

Os dados foram gerados de forma sintética utilizando `pandas` e `numpy`, simulando uma base com 50 milhões de registros e as seguintes colunas:

| Coluna     | Tipo      | Descrição                            |
|------------|-----------|----------------------------------------|
| `id`       | int       | Identificador único sequencial        |
| `categoria`| str       | Categoria aleatória (A, B, C, D)      |
| `valor`    | float     | Valor monetário aleatório             |
| `data`     | datetime  | Datas aleatórias entre 2023 e 2025    |
| `flag`     | bool      | Valor booleano aleatório              |


📊 Consultas Avançadas
1. 📅 Filtro de intervalo de datas + média por categoria
Selecionar registros entre 2023-06-01 e 2024-06-01

Agrupar por categoria e calcular média

2. 🧮 Contagem com múltiplas condições
Contar quantos registros têm:

valor > 500

flag == True

categoria != 'C'

3. 🔗 Agrupamento por ano e categoria
Extrair ano da data

Agrupar por ano e categoria

Calcular média e soma

4. 🧵 Janela de tempo (rolling)
Para cada categoria, calcular a média móvel de 7 dias

5. 🧠 Top N com ordenação
Listar os 10 maiores valores para cada categoria

---
## RESULTADOS

### Spark
Base com 1 milhão de linhas:
etapa                          |tempo_segundos    |
+-------------------------------+------------------+
|Leitura e preparação           |5.102538347244263 |
|Filtro + média                 |1.8560850620269775|
|Contagem com condições         |0.7441680431365967|
|Agrupamento por ano + categoria|1.0112082958221436|
|Média móvel                    |0.379549503326416 |
|Top 10 por categoria           |1.2397093772888184|
|Tempo total                    |10.33382534980774 |


### Pandas
                             etapa  tempo_segundos
0             Leitura e preparação        0.397176
1                   Filtro + média        0.062554
2           Contagem com condições        0.073110
3  Agrupamento por ano + categoria        0.118819
4                      Média móvel        0.442486
5             Top 10 por categoria        0.387176
6                      Tempo total        1.481698

### duckdb
                        etapa  tempo_segundos
0                   Filtro + média        0.182756
1           Contagem com condições        0.116865
2  Agrupamento por ano + categoria        0.129946
3                      Média móvel        0.530592
4             Top 10 por categoria        0.365201
5                      Tempo total        1.330935


📊 Comparação entre Tecnologias
Tecnologia	Pontos Fortes	Quando Usar
PySpark	Escalável, ideal para clusters e Big Data	Quando os dados ultrapassam o que cabe em memória
DuckDB	SQL embutido, super rápido, roda localmente	Quando você precisa agilidade com milhões de registros
Pandas	Flexível, ótimo para visualizações e ajustes	Ideal para etapas finais ou amostras pequenas

📌 Considerações
Este projeto mostra que é possível lidar com milhões de registros mesmo em ambiente local, escolhendo bem as ferramentas. Cada tecnologia tem seu papel e combiná-las pode ser a melhor estratégia!# pyspark-vs-duckdb-vs-pandas
