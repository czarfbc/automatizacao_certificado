from features import mm__to__p

tamanho_fonte = 16
margen_x = 15


def topico_a(cnv):
    cnv.setFont('Poppins-Regular', tamanho_fonte)
    texto = f'a) Normas e regulamentos aplicáveis ao trabalho em altura;'
    cnv.drawString(mm__to__p(margen_x), mm__to__p(140), texto)

def topico_b(cnv):
    cnv.setFont('Poppins-Regular', tamanho_fonte)
    texto = f'b) Análise de Risco e condições impeditivas;'
    cnv.drawString(mm__to__p(margen_x), mm__to__p(125), texto)

def topico_c(cnv):
    cnv.setFont('Poppins-Regular', tamanho_fonte)
    texto = f'c) Riscos potenciais inerentes ao trabalho em altura e medidas de prevenção e controle;'
    cnv.drawString(mm__to__p(margen_x), mm__to__p(110), texto)

def topico_d(cnv):
    cnv.setFont('Poppins-Regular', tamanho_fonte)
    texto = f'd) Sistemas, equipamentos e procedimentos de proteção coletiva;'
    cnv.drawString(mm__to__p(margen_x), mm__to__p(95), texto)

def topico_e(cnv):
    cnv.setFont('Poppins-Regular', tamanho_fonte)
    texto = f'e) Equipamentos de Proteção Individual para trabalho em altura: seleção, inspeção, conservação e limitação de uso;'
    cnv.drawString(mm__to__p(margen_x), mm__to__p(80), texto)

def topico_f(cnv):
    cnv.setFont('Poppins-Regular', tamanho_fonte)
    texto = f'f) Acidentes típicos em trabalhos em altura;'
    cnv.drawString(mm__to__p(margen_x), mm__to__p(65), texto)

def topico_g(cnv):
    cnv.setFont('Poppins-Regular', tamanho_fonte)
    texto = f'g) Condutas em situações de emergência, incluindo noções de técnicas de resgate e de primeiros socorros.'
    cnv.drawString(mm__to__p(margen_x), mm__to__p(50), texto)

def topicos_conteudo(cnv):
    topico_a(cnv)
    topico_b(cnv)
    topico_c(cnv)
    topico_d(cnv)
    topico_e(cnv)
    topico_f(cnv)
    topico_g(cnv)