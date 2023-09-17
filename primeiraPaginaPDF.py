from features import mm__to__p, centralizar__x

def certificado(cnv, largura_pagina):
    cnv.setFont('FiraCode-Bold', 30)
    texto = f'CERTIFICADO'
    largura__texto = cnv.stringWidth(texto, 'FiraCode-Bold', 30)
    cnv.drawString(centralizar__x(largura_pagina, largura__texto), mm__to__p(163), texto)

def especializada(cnv):
    cnv.setFont('Poppins-Regular', 12.7)
    cnv.drawString(mm__to__p(15), mm__to__p(147), f"A ESS – Especializada em Segurança e Saúde Ocupacional certifica que:")

def nome(cnv, colaborador_nome, largura_pagina, unidecode):
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

def colocar_imagens(cnv):
    cnv.drawImage('./imagens/logo-gestro.png', mm__to__p(15), mm__to__p(156), width=105, height=57, mask='auto')

    cnv.drawImage('./imagens/assinatura.png', mm__to__p(168), mm__to__p(45), width=205, height=123, mask='auto')
    

def data__assinatura(cnv, colaborador_nome):
    cnv.setFont('Poppins-Regular', 15)
    cnv.line(mm__to__p(15), mm__to__p(26), mm__to__p(100), mm__to__p(26))

    cnv.drawString(mm__to__p(15), mm__to__p(61), f"Piracicaba, 05 de setembro de 2023.")
    nome__formatado = colaborador_nome.title()
    cnv.drawString(mm__to__p(15), mm__to__p(19), nome__formatado)



def primeira_pagina_pdf(cnv, colaborador_nome, colaborador_rg, primeira_linha_topico, primeira_linha_duracao, largura_pagina, unidecode):
    cnv.rect(mm__to__p(5), mm__to__p(7.2), mm__to__p(244), mm__to__p(176))
    certificado(cnv, largura_pagina)
    especializada(cnv)
    nome(cnv, colaborador_nome, largura_pagina, unidecode)
    texto(cnv, colaborador_rg, primeira_linha_topico, primeira_linha_duracao)
    colocar_imagens(cnv)
    data__assinatura(cnv, colaborador_nome)