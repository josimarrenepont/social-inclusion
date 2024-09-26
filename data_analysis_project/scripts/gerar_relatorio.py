import os

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def gerar_relatorio():
    print("Iniciando a geração do relatório...")
    
    # Verifique se o diretório para salvar o relatório existe
    relatorios_path = "relatorios"
    if not os.path.exists(relatorios_path):
        os.makedirs(relatorios_path)
        print("Diretório 'relatorios' criado.")

    # Caminho para salvar o relatório
    pdf_path = os.path.join(relatorios_path, "relatorio_simples.pdf")
    print(f"Arquivo PDF será salvo em: {pdf_path}")

    # Criar o PDF
    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, "Relatório Simples")
    c.drawString(100, 730, "Este é um PDF de teste.")
    c.showPage()
    c.save()
    print(f"Relatório salvo com sucesso em '{pdf_path}'.")

if __name__ == "__main__":
    gerar_relatorio()
