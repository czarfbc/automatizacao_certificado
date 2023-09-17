from features import quebra__linha

def topico_a(cnv):
    texto = f'a) Normas e regulamentos aplicáveis ao trabalho em altura;'
    quebra__linha(cnv, texto, 137)

def topico_b(cnv):
    texto = f'b) Análise de Risco e condições impeditivas;'
    quebra__linha(cnv, texto, 127)

def topico_c(cnv):
    texto = f'c) Riscos potenciais inerentes ao trabalho em altura e medidas de prevenção e controle;'
    quebra__linha(cnv, texto, 117)

def topico_d(cnv):
    texto = f'd) Sistemas, equipamentos e procedimentos de proteção coletiva;'
    quebra__linha(cnv, texto, 100)

def topico_e(cnv):
    texto = f'e) Equipamentos de Proteção Individual para trabalho em altura: seleção, inspeção, conservação e limitação de uso;'
    quebra__linha(cnv, texto, 90)

def topico_f(cnv):
    texto = f'f) Acidentes típicos em trabalhos em altura;'
    quebra__linha(cnv, texto, 73)

def topico_g(cnv):
    texto = f'g) Condutas em situações de emergência, incluindo noções de técnicas de resgate e de primeiros socorros.'
    quebra__linha(cnv, texto, 63)

def topicos_conteudo(cnv):
    topico_a(cnv)
    topico_b(cnv)
    topico_c(cnv)
    topico_d(cnv)
    topico_e(cnv)
    topico_f(cnv)
    topico_g(cnv)
    