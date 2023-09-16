from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from unidecode import unidecode
from primeiraPaginaPDF import primeira_pagina_pdf
from segundaPaginaPDF import segunda_pagina_pdf

pdfmetrics.registerFont(TTFont('Poppins-Regular', './Poppins/Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Bold', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FiraCode-Bold', '../../../../Downloads/Fira_Code_v6.2/ttf/FiraCode-Bold.ttf'))

largura_pagina = letter[0]

def nome_arquivo(colaborador_nome, colaborador_rg):
    return f"Certificado_{colaborador_nome}_{colaborador_rg}.pdf"

def construcao__pdf(colaborador_nome, colaborador_nome_replace, colaborador_rg, primeira_linha_topico, primeira_linha_duracao):
    nome__pdf = nome_arquivo(colaborador_nome_replace, colaborador_rg)
    cnv = canvas.Canvas(nome__pdf, pagesize=PDF) 
    primeira_pagina_pdf(cnv, colaborador_nome, colaborador_rg, primeira_linha_topico,primeira_linha_duracao, largura_pagina, unidecode)
    
    cnv.showPage()
    segunda_pagina_pdf(cnv)

    cnv.save()  
