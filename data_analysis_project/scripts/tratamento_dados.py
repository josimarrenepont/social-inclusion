
import pandas as pd

dados = pd.read_csv('../data/dados.csv')


print(dados.head())


print(dados.info())


dados = dados.dropna()


dados.to_csv('../data/dados_limpos.csv', index=False)
