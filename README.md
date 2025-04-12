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

## 🧪 Geração dos Dados

```python
import pandas as pd
import numpy as np

n = 50_000_000

np.random.seed(42)

df = pd.DataFrame({
    'id': np.arange(n),
    'categoria': np.random.choice(['A', 'B', 'C', 'D'], size=n),
    'valor': np.random.uniform(0, 1000, size=n).round(2),
    'data': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 730, size=n), unit='D'),
    'flag': np.random.choice([True, False], size=n)
})

df.to_parquet('dados_50_milhoes.parquet', index=False)

```


🔥 Análise com PySpark
python
Copy
Edit
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("Analise50Milhoes").getOrCreate()
df_spark = spark.read.parquet("dados_50_milhoes.parquet")

df_resultado = df_spark.groupBy("categoria").agg(avg("valor").alias("media_valor"))
df_resultado.show()

📊 Comparação entre Tecnologias
Tecnologia	Pontos Fortes	Quando Usar
PySpark	Escalável, ideal para clusters e Big Data	Quando os dados ultrapassam o que cabe em memória
DuckDB	SQL embutido, super rápido, roda localmente	Quando você precisa agilidade com milhões de registros
Pandas	Flexível, ótimo para visualizações e ajustes	Ideal para etapas finais ou amostras pequenas

📌 Considerações
Este projeto mostra que é possível lidar com milhões de registros mesmo em ambiente local, escolhendo bem as ferramentas. Cada tecnologia tem seu papel e combiná-las pode ser a melhor estratégia!# pyspark-vs-duckdb-vs-pandas
