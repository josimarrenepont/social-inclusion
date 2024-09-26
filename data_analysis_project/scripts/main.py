import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def gerar_relatorio():
    relatorios_path = "relatorios"
    if not os.path.exists(relatorios_path):
        os.makedirs(relatorios_path)
        print("Diretório 'relatorios' criado.")
    
    pdf_path = os.path.join(relatorios_path, "relatorio_final.pdf")
    print(f"Arquivo PDF será salvo em: {pdf_path}")

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, "Relatório Final - Análise de Dados LGBT")
    c.drawString(100, 730, "Resumo das Descobertas:")
    c.drawString(100, 710, "1. Distribuição de Gênero")
    c.drawString(100, 690, "2. Distribuição de Escolaridade")

    # Verifique a existência das imagens
    genero_img_path = "visualizations/distribuicao_genero.png"
    escolaridade_img_path = "visualizations/distribuicao_escolaridade.png"

    if os.path.exists(genero_img_path):
        c.drawImage(genero_img_path, 100, 450, width=400, height=300)
        print("Imagem distribuicao_genero.png adicionada.")
    else:
        print("Imagem distribuicao_genero.png não encontrada.")

    if os.path.exists(escolaridade_img_path):
        c.drawImage(escolaridade_img_path, 100, 100, width=400, height=300)
        print("Imagem distribuicao_escolaridade.png adicionada.")
    else:
        print("Imagem distribuicao_escolaridade.png não encontrada.")

    c.showPage()
    c.save()
    print(f"Relatório salvo com sucesso em '{pdf_path}'.")

if __name__ == "__main__":
    gerar_relatorio()
