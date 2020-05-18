import presentes
import pontuacao
import random

pontuacao_presentes = {pontuacao.cont_cultura: presentes.presentes_cultura,
                       pontuacao.cont_esporte: presentes.presentes_esportes,
                       pontuacao.cont_entretenimento: presentes.presentes_entretenimento,
                       pontuacao.cont_conexao_social: presentes.presentes_conexao_social,
                       pontuacao.cont_hobby: presentes.presentes_hobby,
                       pontuacao.cont_vestuario: presentes.presentes_vestuario,
                       pontuacao.cont_saude: presentes.presentes_saude,
                       pontuacao.cont_gastronomia: presentes.presentes_gastronomia}

pontuacao_cres = sorted(pontuacao_presentes)
sugestoes_finais = []

while len(sugestoes_finais) != 9:
    presentes_categoria1 = random.choice(pontuacao_presentes[pontuacao_cres[-1]])
    if presentes_categoria1 not in sugestoes_finais:
        sugestoes_finais.append(presentes_categoria1)
    if presentes_categoria1 in sugestoes_finais:
        presentes_categoria1 = random.choice(pontuacao_presentes[pontuacao_cres[-1]])

    presentes_categoria2 = random.choice(pontuacao_presentes[pontuacao_cres[-2]])
    if presentes_categoria2 not in sugestoes_finais:
        sugestoes_finais.append(presentes_categoria2)
    if presentes_categoria2 in sugestoes_finais:
        presentes_categoria2 = random.choice(pontuacao_presentes[pontuacao_cres[-2]])

    presentes_categoria3 = random.choice(pontuacao_presentes[pontuacao_cres[-3]])
    if presentes_categoria3 not in sugestoes_finais:
        sugestoes_finais.append(presentes_categoria3)
    if presentes_categoria3 in sugestoes_finais:
        presentes_categoria3 = random.choice(pontuacao_presentes[pontuacao_cres[-3]])

    if len(sugestoes_finais) == 9:
        break

print('Nossas sugestões de presentes são: \n')
for i in sugestoes_finais:
    print('{}'.format(i))
