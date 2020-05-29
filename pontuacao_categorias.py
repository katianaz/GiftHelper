import pandas as pd
import opcoes_resposta
import opcoes_presentes
import random
import csv

def converter_df(arq_csv):
    with open(arq_csv, encoding='latin-1') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        tabela = pd.DataFrame(csv_reader)

    return tabela

tabela = converter_df('dados_formulario.csv')

tabela.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                  '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
len(tabela.index) # 12

sugestoes = []

for j in range(0, len(tabela.index)):
    cont_cultura = 0
    cont_esporte = 0
    cont_entretenimento = 0
    cont_conexao_social = 0
    cont_hobby = 0
    cont_vestuario = 0
    cont_saude = 0
    cont_gastronomia = 0

    for i in range(7, 31):
        resp = tabela['{}'.format(i)][j]  # 0 - 11

        if i == 7:
            if opcoes_resposta.ops_resp_q1[0] in resp:
                cont_conexao_social += 3
                cont_hobby += 1
                cont_saude += 2

            if opcoes_resposta.ops_resp_q1[1] in resp:
                cont_cultura += 2
                cont_entretenimento += 3
                cont_conexao_social += 3
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q1[2] in resp:
                cont_cultura += 3
                cont_entretenimento += 3
                cont_hobby += 3

            if opcoes_resposta.ops_resp_q1[3] in resp:
                cont_esporte += 3
                cont_entretenimento += 3
                cont_conexao_social += 2
                cont_hobby += 3
                cont_vestuario += 1
                cont_saude += 2

            if opcoes_resposta.ops_resp_q1[4] in resp:
                cont_cultura += 2
                cont_entretenimento += 3
                cont_conexao_social += 1
                cont_hobby += 3

            if opcoes_resposta.ops_resp_q1[5] in resp:
                cont_cultura += 2
                cont_entretenimento += 3
                cont_conexao_social += 1
                cont_hobby += 3
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q1[6] in resp:
                cont_cultura += 1
                cont_entretenimento += 3
                cont_hobby += 3

            if opcoes_resposta.ops_resp_q1[7] in resp:
                cont_cultura += 2
                cont_entretenimento += 3
                cont_conexao_social += 1
                cont_hobby += 1

            if opcoes_resposta.ops_resp_q1[8] in resp:
                cont_cultura += 2
                cont_entretenimento += 3
                cont_conexao_social += 2
                cont_hobby += 3

            if opcoes_resposta.ops_resp_q1[9] in resp:
                cont_cultura += 1
                cont_entretenimento += 3
                cont_hobby += 3
                cont_vestuario += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q1[10] in resp:
                cont_cultura += 1
                cont_esporte += 1
                cont_entretenimento += 3
                cont_conexao_social += 3

            if opcoes_resposta.ops_resp_q1[11] in resp:
                cont_entretenimento += 3
                cont_conexao_social += 1
                cont_hobby += 3

        if i == 8:
            if opcoes_resposta.ops_resp_q2[0] in resp:
                cont_cultura += 2
                cont_hobby += 1
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q2[1] in resp:
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q2[2] in resp:
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q2[3] in resp:
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q2[4] in resp:
                cont_cultura += 1
                cont_vestuario += 1

        if i == 9:
            if opcoes_resposta.ops_resp_q3[0] in resp:
                cont_cultura += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q3[1] in resp:
                cont_esporte += 2
                cont_saude += 3
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q3[2] in resp:
                cont_esporte -= 1
                cont_saude -= 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q3[3] in resp:
                cont_cultura += 1
                cont_saude += 2
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q3[4] in resp:
                cont_conexao_social += 1
                cont_saude -= 1
                cont_gastronomia += 3

        if i == 10:
            if opcoes_resposta.ops_resp_q4[0] in resp:
                cont_conexao_social += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q4[1] in resp:
                cont_conexao_social += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q4[2] in resp:
                cont_esporte += 1
                cont_saude += 2
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q4[3] in resp:
                cont_esporte -= 1
                cont_saude -= 2
                cont_gastronomia += 1

            if opcoes_resposta.ops_resp_q4[4] in resp:
                cont_conexao_social += 1
                cont_hobby += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q4[5] in resp:
                cont_conexao_social += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q4[6] in resp:
                cont_esporte += 2
                cont_saude += 3
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q4[7] in resp:
                cont_esporte += 1
                cont_saude += 3
                cont_gastronomia += 1

            if opcoes_resposta.ops_resp_q4[8] in resp:
                cont_conexao_social += 1
                cont_hobby += 2
                cont_saude += 1
                cont_gastronomia += 3

        if i == 11:
            if opcoes_resposta.ops_resp_q5[0] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_conexao_social += 2
                cont_hobby += 3
                cont_vestuario += 1
                cont_saude += 1

            if opcoes_resposta.ops_resp_q5[1] in resp:
                cont_cultura += 3
                cont_entretenimento += 3
                cont_conexao_social += 3
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q5[2] in resp:
                cont_cultura += 3
                cont_entretenimento += 2
                cont_hobby += 1

            if opcoes_resposta.ops_resp_q5[3] in resp:
                cont_conexao_social += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q5[4] in resp:
                cont_cultura += 3
                cont_entretenimento += 3
                cont_conexao_social += 1
                cont_hobby += 1

            if opcoes_resposta.ops_resp_q5[5] in resp:
                cont_cultura += 3
                cont_entretenimento += 3
                cont_conexao_social += 1

            if opcoes_resposta.ops_resp_q5[6] in resp:
                cont_conexao_social += 3
                cont_hobby += 1
                cont_gastronomia += 1

        if i == 12:
            if opcoes_resposta.ops_resp_q6[0] in resp:
                cont_esporte += 1
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q6[1] in resp:
                cont_esporte += 3
                cont_entretenimento += 1
                cont_hobby += 3
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q6[2] in resp:
                cont_vestuario += 1

            if opcoes_resposta.ops_resp_q6[3] in resp:
                cont_entretenimento += 2
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q6[4] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q6[5] in resp:
                cont_entretenimento += 1
                cont_conexao_social += 1
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q6[6] in resp:
                cont_vestuario += 2

        if i == 15:
            if opcoes_resposta.ops_resp_q9[0] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q9[1] in resp:
                cont_hobby += 1

            if opcoes_resposta.ops_resp_q9[2] in resp:
                cont_hobby += 1

            if opcoes_resposta.ops_resp_q9[3] in resp:
                cont_entretenimento += 1

            if opcoes_resposta.ops_resp_q9[4] in resp:
                cont_entretenimento += 1
                cont_hobby += 1

        if i == 16:
            if opcoes_resposta.ops_resp_q10[0] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[1] in resp:
                cont_vestuario += 3
                cont_saude += 2

            if opcoes_resposta.ops_resp_q10[2] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[3] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[4] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[5] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[6] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[7] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[8] in resp:
                cont_vestuario += 3

            if opcoes_resposta.ops_resp_q10[9] in resp:
                cont_esporte += 1
                cont_vestuario += 3
                cont_saude += 2

            if opcoes_resposta.ops_resp_q10[10] in resp:
                cont_vestuario -= 3

        if i == 19:
            if opcoes_resposta.ops_resp_q13[0] in resp:
                cont_hobby += 1
                cont_gastronomia += 1

            if opcoes_resposta.ops_resp_q13[1] in resp:
                cont_hobby += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q13[2] in resp:
                cont_hobby += 1
                cont_gastronomia += 3

        if i == 20:
            if opcoes_resposta.ops_resp_q14[0] in resp:
                cont_saude -= 1

            if opcoes_resposta.ops_resp_q14[1] in resp:
                cont_saude += 1

            if opcoes_resposta.ops_resp_q14[2] in resp:
                cont_saude += 2

            if opcoes_resposta.ops_resp_q14[3] in resp:
                cont_saude += 3

        if i == 21:
            if opcoes_resposta.ops_resp_q15[2] in resp:
                cont_hobby += 2

        if i == 22:
            if opcoes_resposta.ops_resp_q16[1] in resp:
                cont_conexao_social += 2
                cont_hobby += 2
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q16[2] in resp:
                cont_conexao_social += 2
                cont_hobby += 3
                cont_gastronomia += 3

        if i == 23:
            if opcoes_resposta.ops_resp_q17[1] in resp:
                cont_saude += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q17[2] in resp:
                cont_saude += 1
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q17[3] in resp:
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q17[4] in resp:
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q17[5] in resp:
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q17[6] in resp:
                cont_gastronomia += 3

        if i == 24:
            if opcoes_resposta.ops_resp_q18[1] in resp:
                cont_saude += 3
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q18[2] in resp:
                cont_saude += 3
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q18[3] in resp:
                cont_saude += 3
                cont_gastronomia += 3

            if opcoes_resposta.ops_resp_q18[4] in resp:
                cont_saude += 3
                cont_gastronomia += 3

        if i == 27:
            if opcoes_resposta.ops_resp_q21[0] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[1] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[2] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[3] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[4] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[5] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[6] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[7] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[8] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q21[10] in resp:
                cont_esporte -= 3
                cont_saude -= 2

            if opcoes_resposta.ops_resp_q21[11] in resp:
                cont_esporte += 3
                cont_entretenimento += 2
                cont_hobby += 1
                cont_saude += 3

        if i == 28:
            if opcoes_resposta.ops_resp_q22[0] in resp:
                cont_saude += 3

            if opcoes_resposta.ops_resp_q22[1] in resp:
                cont_saude += 3

            if opcoes_resposta.ops_resp_q22[3] in resp:
                cont_saude += 2

        if i == 29:
            if opcoes_resposta.ops_resp_q23[0] in resp:
                cont_entretenimento += 1
                cont_saude += 3

            if opcoes_resposta.ops_resp_q23[2] in resp:
                cont_entretenimento += 1
                cont_saude += 1

        if i == 30:
            if opcoes_resposta.ops_resp_q24[0] in resp:
                cont_saude += 3

            if opcoes_resposta.ops_resp_q24[2] in resp:
                cont_saude += 2

    pontuacao_presentes = {cont_cultura: opcoes_presentes.presentes_cultura,
                           cont_esporte: opcoes_presentes.presentes_esportes,
                           cont_entretenimento: opcoes_presentes.presentes_entretenimento,
                           cont_conexao_social: opcoes_presentes.presentes_conexao_social,
                           cont_hobby: opcoes_presentes.presentes_hobby,
                           cont_vestuario: opcoes_presentes.presentes_vestuario,
                           cont_saude: opcoes_presentes.presentes_saude,
                           cont_gastronomia: opcoes_presentes.presentes_gastronomia}

    pontuacao_cres = sorted(pontuacao_presentes)

    sugestoes_finais = []

    for i in range(-3, 0):
        for i in random.sample(pontuacao_presentes[pontuacao_cres[i]], k=3):
            sugestoes_finais.append(i)

    sugestoes.append(sugestoes_finais)

    """print('Oi {}! Os presentes que {} vai amar são: \n'.format(tabela['3'][j], tabela['4'][j]))
    
    cont = 0
    for i in sugestoes_finais:
        cont += 1
        print('{}. {}'.format(cont, i))
    
    print('===========')"""
