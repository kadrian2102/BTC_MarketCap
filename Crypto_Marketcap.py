# 1
# Importar librerias
import pandas as pd
import matplotlib.pyplot as plt

# Leer market cap a pandas dataframe
dec6 = pd.read_csv("datasets/coinmarketcap_06122017.csv")

# Seleccionar columnas
market_cap_raw = dec6["id", "market_cap_usd"]

# Contanto el numero de valores
print(market_cap_raw.count())

# 2

# Filtrar filas de valores en blanco
cap = market_cap_raw.query()

# Contando el numero de valores
print(cap.count())

# 3 How big is Bitcoin compared with the rest of the cryptocurrencies?

# Selecting the first 10 rows and setting the index
cap10 = cap.set_index(id)[:11]

# Calcula el porcentaje de capitalización por cada moneda
cap10.assign(cap10=lambda cap : (cap.market_cap_usd * 100) / cap.market_cap_usd.sum())


