from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


pdfmetrics.registerFont(TTFont('Poppins-Regular', './Poppins/Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Bold', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Medium', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FiraCode-Bold', '../../../../Downloads/Fira_Code_v6.2/ttf/FiraCode-Bold.ttf'))

def mm__to__p(mm):
    return mm / 0.352777

def canvas__var(cnv):
   return cnv

def centralizar__x(largura__pagina, largura__texto):
    centro = (largura__pagina - (largura__texto) / 2) / 2
    return centro

cnv1 = canvas.Canvas(f"kkkpdf.pdf", pagesize=PDF)
cnv = canvas__var(cnv1)
cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))

largura_pagina = letter[0]
texto__nome = f'JOEL JANUARIO MIRON'

def certificado():
    cnv.setFont('FiraCode-Bold', 30)
    texto__certificado = f'CERTIFICADO'
    largura__texto__certificado = cnv.stringWidth(texto__certificado, 'FiraCode-Bold', 30)
    cnv.drawString(centralizar__x(largura_pagina, largura__texto__certificado), mm__to__p(163), texto__certificado)

def especializada():
    cnv.setFont('Poppins-Regular', 12.7)
    cnv.drawString(mm__to__p(15), mm__to__p(147), f"A ESS – Especializada em Segurança e Saúde Ocupacional certifica que:")

def nome():
    cnv.setFont('Poppins-Medium', 21)
    
    largura__texto__nome = cnv.stringWidth(texto__nome, 'Poppins-Medium', 21)
    cnv.drawString(centralizar__x(largura_pagina, largura__texto__nome), mm__to__p(125), texto__nome)

def texto():
    cnv.setFont('Poppins-Regular', 16)
    cnv.drawString(mm__to__p(15), mm__to__p(107), f"Pintor, CPF.:19178632846, realizou com êxito o TREINAMENTO DE NR – 35 – TRABALHO EM ALTURA, com duração de 8 (Oito) horas, de acordo com a exigência da Norma Regulamentadora NR 35, portaria SEPRT 915 do Ministério do Trabalho.")

def data__assinatura():
    cnv.setFont('Poppins-Regular', 15)
    cnv.line(mm__to__p(15), mm__to__p(26), mm__to__p(100), mm__to__p(26))

    cnv.drawString(mm__to__p(15), mm__to__p(61), f"Piracicaba, 05 de setembro de 2023.")
    nome__formatado = texto__nome.title()
    cnv.drawString(mm__to__p(15), mm__to__p(19), nome__formatado)

def construcao__pdf():
    certificado()
    especializada()
    nome()
    texto()
    data__assinatura()

construcao__pdf()

cnv.save()