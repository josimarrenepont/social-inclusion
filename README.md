# Projeto Análise de Dados

Este projeto tem como objetivo realizar o tratamento, análise e visualização de dados de uma pesquisa relacionada à comunidade LGBT.

## Estrutura do Projeto

- `data/`: Contém o arquivo `dados.csv` com os dados brutos e `dados_tratados.csv` com os dados após o tratamento.
- `notebooks/`: Notebooks Jupyter para tratamento e análise dos dados.
- `scripts/`: Scripts Python para automatizar o tratamento e a visualização dos dados.
- `visualizations/`: Gráficos gerados a partir da análise.
- `relatorios/`: Relatório final em formato PDF com as descobertas do projeto.
- `requirements.txt`: Dependências do projeto.

## Como Executar

1. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
     
2. Executar Projeto:
    ```bash
    python scripts/main.py
    ```
   
3. Gere o relatório final:
    ```bash
    python scripts/gerar_relatorio.py
    ```

## Notas
- Certifique-se de que os arquivos de dados estão localizados na pasta data/ antes de executar os scripts.
- O projeto utiliza as seguintes bibliotecas:
    * pandas
    * matplotlib
    * seaborn
    * reportlab


