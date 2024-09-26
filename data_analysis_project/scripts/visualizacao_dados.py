import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dados = pd.read_csv('../data/dados_limpos.csv')


sns.set(style="whitegrid")


plt.figure(figsize=(8,6))
sns.countplot(x='Gênero', data=dados)
plt.title('Distribuição de Gênero')
plt.savefig('../visualizations/distribuicao_genero.png')
plt.show()


plt.figure(figsize=(8,6))
sns.countplot(x='Escolaridade', data=dados)
plt.title('Distribuição de Escolaridade')
plt.savefig('../visualizations/distribuicao_escolaridade.png')
plt.show()
