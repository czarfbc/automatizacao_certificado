from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


#=================================FAZER PDF========================================
pdfmetrics.registerFont(TTFont('Poppins-Regular', './Poppins/Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Bold', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Medium', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FiraCode-Bold', '../../../../Downloads/Fira_Code_v6.2/ttf/FiraCode-Bold.ttf'))

largura_pagina = letter[0]

def mm__to__p(mm):
    return mm / 0.352777

def centralizar__x(largura__pagina, largura__texto):
    centro = (largura__pagina - (largura__texto) / 2) / 2
    return centro

def nome_arquivo(colaborador_nome, colaborador_rg):
    return f"Certificado_{colaborador_nome}_{colaborador_rg}.pdf"

def certificado(cnv):
    cnv.setFont('FiraCode-Bold', 30)
    texto__certificado = f'CERTIFICADO'
    largura__texto__certificado = cnv.stringWidth(texto__certificado, 'FiraCode-Bold', 30)
    cnv.drawString(centralizar__x(largura_pagina, largura__texto__certificado), mm__to__p(163), texto__certificado)

def especializada(cnv):
    cnv.setFont('Poppins-Regular', 12.7)
    cnv.drawString(mm__to__p(15), mm__to__p(147), f"A ESS – Especializada em Segurança e Saúde Ocupacional certifica que:")

def nome(cnv, colaborador_nome):
    cnv.setFont('Poppins-Medium', 21)
    largura__texto__nome = cnv.stringWidth(colaborador_nome, 'Poppins-Medium', 21)
    cnv.drawString(centralizar__x(largura_pagina, largura__texto__nome), mm__to__p(125), colaborador_nome)

def texto(cnv, colaborador_rg, primeira_linha_topico, primeira_linha_duracao):
    cnv.setFont('Poppins-Regular', 16)
    cnv.drawString(mm__to__p(15), mm__to__p(107), f"Pintor, CPF.:{colaborador_rg}, realizou com êxito o {primeira_linha_topico}, com duração de {primeira_linha_duracao}, de acordo com a exigência da Norma Regulamentadora NR 35, portaria SEPRT 915 do Ministério do Trabalho.")

def data__assinatura(cnv, colaborador_nome):
    cnv.setFont('Poppins-Regular', 15)
    cnv.line(mm__to__p(15), mm__to__p(26), mm__to__p(100), mm__to__p(26))

    cnv.drawString(mm__to__p(15), mm__to__p(61), f"Piracicaba, 05 de setembro de 2023.")
    nome__formatado = colaborador_nome.title()
    cnv.drawString(mm__to__p(15), mm__to__p(19), nome__formatado)

def construcao__pdf(colaborador_nome, colaborador_rg, primeira_linha_topico, primeira_linha_duracao):
    cnv = canvas.Canvas(nome_arquivo(colaborador_nome, colaborador_rg), pagesize=PDF)
    cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))
    certificado(cnv)
    especializada(cnv)
    nome(cnv, colaborador_nome)
    texto(cnv, colaborador_rg, primeira_linha_topico, primeira_linha_duracao)
    data__assinatura(cnv, colaborador_nome)

    cnv.save()  
