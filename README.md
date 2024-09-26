# Projeto Análise de Dados

Este projeto tem como objetivo realizar o tratamento, análise e visualização de dados de uma pesquisa relacionada à comunidade LGBT.

## Estrutura do Projeto

- `data/`: Contém o arquivo `dados.csv` com os dados brutos.
- `notebooks/`: Notebooks para tratamento e análise dos dados.
- `scripts/`: Scripts Python para automatizar o tratamento e a visualização.
- `visualizations/`: Gráficos gerados.
- `relatorios/`: Relatório final em PDF.
- `requirements.txt`: Dependências do projeto.

## Como Executar

1. Instale as dependências:
     ```bash
     pip install -r requirements.txt
     ```
    - pandas
    - matplotlib
    - seaborn
    - reportlab

 
2. Execute o script de tratamento de dados:
   ```bash
   python scripts/visualizacao_dados.py 
   ```
  
4. Gere o relatório final:
```bash
python scripts/gerar_relatorio.py
```
