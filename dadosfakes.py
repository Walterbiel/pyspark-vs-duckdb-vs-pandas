import pandas as pd
import numpy as np
from datetime import timedelta

# Total de registros
n = 500_000_000
np.random.seed(42)

# Gerando os dados
df = pd.DataFrame({
    'id': np.arange(n),
    'categoria': np.random.choice(['A', 'B', 'C', 'D'], size=n),
    'valor': np.random.uniform(0, 1000, size=n).round(2),
    'data': pd.to_datetime('2023-01-01') + pd.to_timedelta(np.random.randint(0, 730, size=n), unit='D'),
    'flag': np.random.choice([True, False], size=n)
})

# Salvando como CSV (sem index)
df.to_csv("dados_500_milhoes.csv", index=False)
