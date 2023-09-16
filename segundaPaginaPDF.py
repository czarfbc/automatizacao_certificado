from features import mm__to__p

def conteudo__progamatico(cnv):
    cnv.setFont('FiraCode-Bold', 24)
    texto = f'CERTIFICADO PROGAMÁTICO DO CURSO:'
    cnv.drawString(mm__to__p(41), mm__to__p(163), texto)

def segunda_pagina_pdf(cnv):
    cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))
    conteudo__progamatico(cnv)
