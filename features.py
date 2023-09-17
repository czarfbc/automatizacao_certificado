def mm__to__p(mm):
    return mm / 0.352777

def centralizar__x(largura__pagina, largura__texto):
    centro = (largura__pagina - (largura__texto) / 2) / 2
    return centro

def quebra__linha(cnv, texto, y__inicial):
    largura_maxima = mm__to__p(226)
    x_inicial = mm__to__p(15)
    y_inicial = mm__to__p(y__inicial)
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
        