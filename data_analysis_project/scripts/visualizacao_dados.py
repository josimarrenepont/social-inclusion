import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def gerar_visualizacoes():
    # Carregar os dados
    dados = pd.read_csv('../data/dados_tratados.csv', delimiter=';')
    
    # Verificar o conteúdo do DataFrame
    print(dados.head())
    print(dados.columns)

    # Visualização para a distribuição de gênero
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Gênero', data=dados)
    plt.title('Distribuição de Gênero')
    plt.savefig('../visualizations/distribuicao_genero.png')
    plt.close()  # Fecha a figura para evitar sobreposições

    # Visualização para a distribuição de escolaridade
    plt.figure(figsize=(8, 6))
    sns.countplot(x='Escolaridade', data=dados)
    plt.title('Distribuição de Escolaridade')
    plt.savefig('../visualizations/distribuicao_escolaridade.png')
    plt.close()  # Fecha a figura para evitar sobreposições

if __name__ == "__main__":
    gerar_visualizacoes()
