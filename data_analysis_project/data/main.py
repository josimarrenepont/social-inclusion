import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dados = pd.read_csv('dados.csv')


print(dados.head())


print(dados.info())


dados = dados.dropna()
