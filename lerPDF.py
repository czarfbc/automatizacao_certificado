import tabula
import pandas as pd
from tabulate import tabulate
from fazerPDF import construcao__pdf

lista_tabelas = tabula.read_pdf("teste.pdf", pages="1", multiple_tables=True)

tabela1 = lista_tabelas[1]
tabela2 = lista_tabelas[2]

tabela_info_curso = pd.DataFrame(tabela1)
tabela_info_alunos = pd.DataFrame(tabela2)

tabela_info_alunos["RG"] = pd.to_numeric(tabela_info_alunos["RG"], errors="coerce").fillna(0).astype(int)
tabela_info_alunos = tabela_info_alunos.loc[tabela_info_alunos['RG'] != 0]

tabela_info_alunos = tabela_info_alunos.dropna(subset=["Colaborador"], how="any")

print(tabulate(tabela_info_curso,headers='keys',tablefmt='pretty'))
print(tabulate(tabela_info_alunos, headers='keys', tablefmt='pretty'))

topico_assunto = tabela_info_curso['Tópico/Assunto']
primeira_linha_topico = topico_assunto.iloc[0]

duracao = tabela_info_curso['Duração']
primeira_linha_duracao = duracao.iloc[0]

for index, row in tabela_info_alunos.iterrows():
    colaborador_rg = row['RG']
    colaborador_nome = row['Colaborador']
    colaborador_nome_replace = colaborador_nome.replace(" ", "_")
    construcao__pdf(colaborador_nome, colaborador_nome_replace, colaborador_rg, primeira_linha_topico, primeira_linha_duracao)
    print(colaborador_nome_replace)
