from features import mm__to__p
from topicosConteudo import topicos_conteudo

def conteudo__progamatico(cnv):
    cnv.setFont('FiraCode-Bold', 24)
    texto = f'CERTIFICADO PROGAMÁTICO DO CURSO:'
    cnv.drawString(mm__to__p(41), mm__to__p(163), texto)

def descricao__conteudo__progamtico(cnv):
    topicos_conteudo(cnv)

def colocar_imagens(cnv):
    cnv.drawImage('./imagens/nr35.png', mm__to__p(195), mm__to__p(10), width=130, height=130, mask='auto')

def segunda_pagina_pdf(cnv):
    cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))
    conteudo__progamatico(cnv)
    descricao__conteudo__progamtico(cnv)
    colocar_imagens(cnv)
