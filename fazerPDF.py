from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def mm__to__p(mm):
    return mm / 0.352777


pdfmetrics.registerFont(TTFont('Poppins-Regular', './Poppins/Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Bold', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-SemiBold', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Medium', './Poppins/Poppins-Bold.ttf'))

cnv = canvas.Canvas("meu_pdf.pdf", pagesize=PDF)
largura_pagina = letter[0]

cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))

cnv.setFont('Poppins-Bold', 30)
texto__certificado = f'CERTIFICADO'
largura__texto__certificado = cnv.stringWidth(texto__certificado, 'Poppins-Regular', 30)
pos__x__certificado = (largura_pagina - (largura__texto__certificado) / 2) / 2
cnv.drawString(pos__x__certificado, mm__to__p(163), texto__certificado)

cnv.setFont('Poppins-Regular', 14)
cnv.drawString(mm__to__p(15), mm__to__p(147), f"A ESS – Especializada em Segurança e Saúde Ocupacional certifica que:")

cnv.setFont('Poppins-Medium', 21)
texto__nome = f'JOEL JANUARIO MIRON'
largura__texto__nome = cnv.stringWidth(texto__nome, 'Poppins-Regular', 21)
pos__x__nome = (largura_pagina - (largura__texto__nome) / 2) / 2
cnv.drawString(pos__x__nome, mm__to__p(125), texto__nome)

cnv.setFont('Poppins-Regular', 16)
# cnv.drawString(mm__to__p(30), mm__to__p(45), f"Pintor, CPF.:19178632846, realizou com êxito o TREINAMENTO DE NR – 35 – TRABALHO EM ALTURA, com duração de 8 (Oito) horas, de acordo com a exigência da Norma Regulamentadora NR 35, portaria SEPRT 915 do Ministério do Trabalho.")

cnv.setFont('Poppins-Regular', 15)

cnv.drawString(mm__to__p(15), mm__to__p(61), f"Piracicaba, 05 de setembro de 2023.")

cnv.line(mm__to__p(15), mm__to__p(26), mm__to__p(100), mm__to__p(26))

nome__formatado = texto__nome.title()
cnv.drawString(mm__to__p(15), mm__to__p(19), nome__formatado)

cnv.save()