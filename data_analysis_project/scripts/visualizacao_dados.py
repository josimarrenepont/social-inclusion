import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def gerar_visualizacoes():
    
    dados = pd.read_csv('../data/dados_tratados.csv', delimiter=';')
    
    print(dados.head())
    print(dados.columns)

    plt.figure(figsize=(8, 6))
    sns.countplot(x='Gênero', data=dados)
    plt.title('Distribuição de Gênero')
    plt.savefig('../visualizations/distribuicao_genero.png')
    plt.close()

    plt.figure(figsize=(8, 6))
    sns.countplot(x='Escolaridade', data=dados)
    plt.title('Distribuição de Escolaridade')
    plt.savefig('../visualizations/distribuicao_escolaridade.png')
    plt.close()

if __name__ == "__main__":
    gerar_visualizacoes()
