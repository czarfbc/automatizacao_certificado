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

cnv = canvas.Canvas("meu_pdf.pdf", pagesize=PDF)
cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))

cnv.setFont('Poppins-Bold', 30)
cnv.drawString(mm__to__p(90), mm__to__p(163), f"CERTIFICADO")

cnv.setFont('Poppins-Regular', 14)
cnv.drawString(mm__to__p(120), mm__to__p(150), f"A ESS – Especializada em Segurança e Saúde Ocupacional certifica que:")

cnv.setFont('Poppins-SemiBold', 22)
cnv.drawString(mm__to__p(120), mm__to__p(120), f"JOEL JANUARIO MIRON")

cnv.setFont('Poppins-Regular', 16)
cnv.drawString(mm__to__p(30), mm__to__p(45), f"Pintor, CPF.:19178632846, realizou com êxito o TREINAMENTO DE NR – 35 – TRABALHO EM ALTURA, com duração de 8 (Oito) horas, de acordo com a exigência da Norma Regulamentadora NR 35, portaria SEPRT 915 do Ministério do Trabalho.")

cnv.drawString(mm__to__p(120), mm__to__p(90), f"Piracicaba, 05 de setembro de 2023.")

cnv.line(mm__to__p(120), mm__to__p(60), mm__to__p(400), mm__to__p(60))

cnv.drawString(mm__to__p(120), mm__to__p(30), f"JOEL JANUARIO MIRON")

cnv.save()