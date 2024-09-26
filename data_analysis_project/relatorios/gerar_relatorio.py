from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def gerar_relatorio():
    c = canvas.Canvas("../relatorios/relatorio_final.pdf", pagesize=letter)
    c.drawString(100, 750, "Relatório Final - Análise de Dados LGBT")
    c.drawString(100, 730, "Resumo das Descobertas:")
    c.drawString(100, 710, "1. Distribuição de Gênero")
    c.drawString(100, 690, "2. Distribuição de Escolaridade")
    c.drawImage("../visualizations/distribuicao_genero.png", 100, 450, width=400, height=300)
    c.drawImage("../visualizations/distribuicao_escolaridade.png", 100, 100, width=400, height=300)
    
    c.showPage()
    c.save()

if __name__ == "__main__":
    gerar_relatorio()
