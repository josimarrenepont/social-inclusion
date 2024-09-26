import pandas as pd


def tratar_dados():
    dados = pd.read_csv('../data/dados.csv')
    dados = dados.dropna()
    dados.to_csv('../data/dados_tratados.csv', index=False)
    print("Dados tratados e salvos com sucesso.")

if __name__ == "__main__":
    tratar_dados()
