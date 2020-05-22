import opcoes_presentes
import pontuacao_categorias
import random

pontuacao_presentes = {pontuacao_categorias.cont_cultura: opcoes_presentes.presentes_cultura,
                       pontuacao_categorias.cont_esporte: opcoes_presentes.presentes_esportes,
                       pontuacao_categorias.cont_entretenimento: opcoes_presentes.presentes_entretenimento,
                       pontuacao_categorias.cont_conexao_social: opcoes_presentes.presentes_conexao_social,
                       pontuacao_categorias.cont_hobby: opcoes_presentes.presentes_hobby,
                       pontuacao_categorias.cont_vestuario: opcoes_presentes.presentes_vestuario,
                       pontuacao_categorias.cont_saude: opcoes_presentes.presentes_saude,
                       pontuacao_categorias.cont_gastronomia: opcoes_presentes.presentes_gastronomia}

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

print('Oi {}! Os presentes que {} vai amar são: \n'.format(pontuacao_categorias.respostas_formulario.iloc[1][2],
                                                           pontuacao_categorias.respostas_formulario.iloc[1][3]))
cont = 0
for i in sugestoes_finais:
    cont += 1
    print('{}. {}'.format(cont, i))
print(sugestoes_finais)
