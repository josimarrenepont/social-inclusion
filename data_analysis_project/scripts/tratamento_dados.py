import os

import pandas as pd


def tratar_dados():
    # Imprime o diretório de trabalho atual
    print("Current working directory:", os.getcwd())
    
    # Carrega os dados do arquivo CSV
    dados = pd.read_csv(r'C:\temp\ws-vscode\social-inclusion\data_analysis_project\data\dados.csv', encoding='latin1')

    
    # Exibe as primeiras linhas do dataframe
    print(dados.head())

if __name__ == "__main__":
    tratar_dados()
