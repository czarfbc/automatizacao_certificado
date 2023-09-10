from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import PDF

cnv = canvas.Canvas("meu_pdf.pdf", pagesize=PDF)

cnv.rect(14.173259595, 20.409493816, 691.655068216, 498.89873773)

cnv.save()