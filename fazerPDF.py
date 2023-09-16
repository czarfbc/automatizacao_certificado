from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from unidecode import unidecode

# =================================FAZER PDF========================================
pdfmetrics.registerFont(TTFont('Poppins-Regular', './Poppins/Poppins-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Poppins-Bold', './Poppins/Poppins-Bold.ttf'))
pdfmetrics.registerFont(TTFont('FiraCode-Bold', '../../../../Downloads/Fira_Code_v6.2/ttf/FiraCode-Bold.ttf'))

largura_pagina = letter[0]
largura_pagina2 = letter[1]

def mm__to__p(mm):
    return mm / 0.352777

def centralizar__x(largura__pagina, largura__texto):
    centro = (largura__pagina - (largura__texto) / 2) / 2
    return centro

def nome_arquivo(colaborador_nome, colaborador_rg):
    return f"Certificado_{colaborador_nome}_{colaborador_rg}.pdf"

def certificado(cnv):
    cnv.setFont('FiraCode-Bold', 30)
    texto = f'CERTIFICADO'
    largura__texto = cnv.stringWidth(texto, 'FiraCode-Bold', 30)
    cnv.drawString(centralizar__x(largura_pagina, largura__texto), mm__to__p(163), texto)

def especializada(cnv):
    cnv.setFont('Poppins-Regular', 12.7)
    cnv.drawString(mm__to__p(15), mm__to__p(147), f"A ESS – Especializada em Segurança e Saúde Ocupacional certifica que:")

def nome(cnv, colaborador_nome):
    cnv.setFont('Poppins-Bold', 21)
    largura__texto__nome = cnv.stringWidth(colaborador_nome, 'Poppins-Bold', 21)
    nome__formatado = unidecode(colaborador_nome).upper()
    cnv.drawString(centralizar__x(largura_pagina, largura__texto__nome), mm__to__p(125), nome__formatado)

def texto(cnv, colaborador_rg, primeira_linha_topico, primeira_linha_duracao):
    texto = f"Pintor, CPF.:{colaborador_rg}, realizou com êxito o {primeira_linha_topico}, com duração de {primeira_linha_duracao}, de acordo com a exigência da Norma Regulamentadora NR 35, portaria SEPRT 915 do Ministério do Trabalho."

    largura_maxima = mm__to__p(226)
    x_inicial = mm__to__p(15)
    y_inicial = mm__to__p(107)
    tamanho_fonte = 16
    cnv.setFont('Poppins-Regular', tamanho_fonte)

    palavras = texto.split()
    linhas = []

    x, y = x_inicial, y_inicial
    linha_atual = []
    largura_atual = 0

    for palavra in palavras:
        largura_palavra = cnv.stringWidth(palavra, 'Poppins-Regular', tamanho_fonte)

        if largura_atual + largura_palavra <= largura_maxima:
            linha_atual.append(palavra)
            largura_atual += largura_palavra + cnv.stringWidth(' ', 'Poppins-Regular', tamanho_fonte)
        else:
            linhas.append(' '.join(linha_atual))
            linha_atual = [palavra]
            largura_atual = largura_palavra + cnv.stringWidth(' ', 'Poppins-Regular', tamanho_fonte)

    linhas.append(' '.join(linha_atual))

    for linha in linhas:
        cnv.drawString(x, y, linha)
        y -= tamanho_fonte * 1.2 


def data__assinatura(cnv, colaborador_nome):
    cnv.setFont('Poppins-Regular', 15)
    cnv.line(mm__to__p(15), mm__to__p(26), mm__to__p(100), mm__to__p(26))

    cnv.drawString(mm__to__p(15), mm__to__p(61), f"Piracicaba, 05 de setembro de 2023.")
    nome__formatado = colaborador_nome.title()
    cnv.drawString(mm__to__p(15), mm__to__p(19), nome__formatado)


def colocar_logo(cnv):
    cnv.drawImage('logo-gestro.png', mm__to__p(15), mm__to__p(156), width=105, height=57, mask='auto')

def conteudo__progamatico(cnv):
    cnv.setFont('FiraCode-Bold', 24)
    texto = f'CERTIFICADO PROGAMÁTICO DO CURSO:'
    cnv.drawString(mm__to__p(46), mm__to__p(163), texto)

def construcao__pdf(colaborador_nome, colaborador_nome_replace, colaborador_rg, primeira_linha_topico, primeira_linha_duracao):
    nome__pdf = nome_arquivo(colaborador_nome_replace, colaborador_rg)
    cnv = canvas.Canvas(nome__pdf, pagesize=PDF)
    cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))
    certificado(cnv)
    especializada(cnv)
    nome(cnv, colaborador_nome)
    texto(cnv, colaborador_rg, primeira_linha_topico, primeira_linha_duracao)
    data__assinatura(cnv, colaborador_nome)
    colocar_logo(cnv)
    

    cnv.showPage()
    cnv.rect(mm__to__p(9), mm__to__p(17), mm__to__p(236), mm__to__p(162))
    conteudo__progamatico(cnv)

    cnv.save()  
