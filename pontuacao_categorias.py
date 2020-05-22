import pandas as pd

respostas_formulario = pd.read_csv("respostas_formulario.csv", low_memory=False)

cont_cultura = 0
cont_esporte = 0
cont_entretenimento = 0
cont_conexao_social = 0
cont_hobby = 0
cont_vestuario = 0
cont_saude = 0
cont_gastronomia = 0

ops_resp_q1 = ['Passar o tempo com a família', 'Ir a festas e eventos sociais', 'Ler',
               'Praticar esportes, academia, trilha', 'Jogos tabuleiro, virtual, etc', 'Pintura', 'Escrever',
               'Ver filmes/séries', 'Tocar instrumentos musicais', 'Cozinhar', 'Encontrar amigos', 'Fazer compras',
               'Outros', 'Não sei dizer']

ops_resp_q2 = ['Roupas de bandas', 'Roupas pretas/cinzas', 'Roupas coloridas', 'Roupas xadrez', 'Roupas com estampas',
               'Indiferente', 'Não sei dizer']

ops_resp_q3 = ['Culinária de países (italiana, portuguesa, árabe...)', 'Alimentação saudável', 'Doces',
               'Cozinhar em casa', 'Fast food', 'Não sei dizer']

ops_resp_q4 = ['Destilados', 'Cerveja', 'Sucos', 'Refrigerantes', 'Café', 'Chá', 'Vitaminas', 'Água', 'Vinhos',
               'Outros', 'Não sei dizer']

ops_resp_q5 = ['Trilhas, cachoeiras, natureza', 'Festa, balada, evento social, show', 'Lançamento de um livro',
               'Restaurante/café/confeitaria', 'Teatro', 'Cinema', 'Bar', 'Não sei dizer']

ops_resp_q6 = ['Tênis normal', 'Tênis de esporte, trilha', 'Chinelo', 'Calçado social', 'Bota', 'Salto alto',
               'Sapatilha', 'Não sei dizer']

ops_resp_q7 = ['Ação', 'Romance', 'Comédia', 'Drama', 'Terror', 'Sci-fic', 'Documentário', 'Animação', 'Musical',
               'Não gosta de filmes/séries', 'Não sei dizer']

ops_resp_q8 = ['Auto-ajudo', 'Romance', 'Terror', 'Fantasia', 'Suspense', 'Informativo (culinária, biografia...',
               'Sci-fic', 'Policial', 'Não gosta de livros', 'Não sei dizer']

ops_resp_q9 = ['Roupas e acessórios', 'Produtos para casa', 'Produtos para carro', 'Produtos de decoração',
               'Produtos de papelaria', 'Nenhum destes', 'Não sei dizer']

ops_resp_q10 = ['Relógio', 'Óculos de sol', 'Colar/corrente/gargantilha', 'Anel', 'Pulseira', 'Brinco', 'Cachecol',
                'Luvas', 'Piercing', 'Chapéu/Boné/Touca/Bandana', 'Não usa acessórios', 'Não sei dizer']

ops_resp_q11 = ['Não tem carro', 'Tem e gosta de comprar acessórios', 'Tem e não gosta de comprar acessórios',
                'Não sei dizer']

ops_resp_q12 = ['Não tem tatuagens e não quer fazer', 'Não tem tatuagens e quer fazer',
                'Tem tatuagens e quer fazer mais', 'Tem tatuagens e não quer fazer mais', 'Não sei dizer']

ops_resp_q13 = ['Gosta de ganhar objetos de decoração', 'Gosta de ganhar objetos de decoração e utensílios domésticos',
                'Gosta apenas de ganhar utensílios domésticos', 'Não gosta de ganhar presentes para casa',
                'Não sei dizer']

ops_resp_q14 = ['Não usa e não gosta',
                'Não usa, porém gosta', 'Usa pouco', 'Usa bastante', 'Não sei dizer']

ops_resp_q15 = ['Não gosta de plantas', 'Gosta de plantas, porém não gosta de receber como presente',
                'Gosta de plantas e gosta de receber como presente', 'Não sei dizer']

ops_resp_q16 = ['Não gosta de cozinhar', 'Gosta de cozinhar para seus amigos, porém não tem o material adequado',
                'Gosta de cozinhar e tem todos os equipamentos necessários', 'Não sei dizer']

ops_resp_q17 = ['Não gosta', 'Gosta, mas tem que ser light', 'Gosta, mas tem que ser diet',
                'Gosta somente de chocolate escuro', 'Gosta somente de chocolate branco',
                'Não gosta de chocolate amargo', 'Gosta de qualquer chocolate', 'Não sei dizer']

ops_resp_q18 = ['Não tem restrições', 'Intolerância ao glúten', 'Intolerância à lactose',
                'Ovolactovegetariano (não consome nenhum tipo de carne, mas consome ovos e laticínios)',
                'Vegetariano estrito (não consome nenhum tipo de carne, ovo ou laticínios)', 'Não sei dizer']

ops_resp_q19 = ['Sim', 'Não',
                'Talvez', 'Não sei dizer']

ops_resp_q20 = ['Sim', 'Não',
                'Talvez', 'Não sei dizer']

ops_resp_q21 = ['Futebol', 'Basquete', 'Handball', 'Dança', 'Corrida', 'Natação', 'Lutas', 'Vôlei', 'Ciclismo',
                'Não sei dizer', 'Não gosta de esportes', 'Outros']

ops_resp_q22 = ['Sim, usa vários', 'Sim, mas usa sempre o mesmo', 'Sim, mas não usa',
                'Não usa, mas gostaria de ter um',
                'Não usa e não gosta', 'Não sei dizer']

ops_resp_q23 = ['Sim', 'Não',
                'Talvez', 'Não sei dizer']

ops_resp_q24 = ['Sim', 'Não',
                'Talvez', 'Não sei dizer']

for i in range(6, 30):
    resp = respostas_formulario.iloc[1][i]

    if i == 6:
        if ops_resp_q1[0] in resp:
            cont_conexao_social += 3
            cont_hobby += 1
            cont_saude += 2

        if ops_resp_q1[1] in resp:
            cont_cultura += 2
            cont_entretenimento += 3
            cont_conexao_social += 3
            cont_vestuario += 1

        if ops_resp_q1[2] in resp:
            cont_cultura += 3
            cont_entretenimento += 3
            cont_hobby += 3

        if ops_resp_q1[3] in resp:
            cont_esporte += 3
            cont_entretenimento += 3
            cont_conexao_social += 2
            cont_hobby += 3
            cont_vestuario += 1
            cont_saude += 2

        if ops_resp_q1[4] in resp:
            cont_cultura += 2
            cont_entretenimento += 3
            cont_conexao_social += 1
            cont_hobby += 3

        if ops_resp_q1[5] in resp:
            cont_cultura += 2
            cont_entretenimento += 3
            cont_conexao_social += 1
            cont_hobby += 3
            cont_vestuario += 1

        if ops_resp_q1[6] in resp:
            cont_cultura += 1
            cont_entretenimento += 3
            cont_hobby += 3

        if ops_resp_q1[7] in resp:
            cont_cultura += 2
            cont_entretenimento += 3
            cont_conexao_social += 1
            cont_hobby += 1

        if ops_resp_q1[8] in resp:
            cont_cultura += 2
            cont_entretenimento += 3
            cont_conexao_social += 2
            cont_hobby += 3

        if ops_resp_q1[9] in resp:
            cont_cultura += 1
            cont_entretenimento += 3
            cont_hobby += 3
            cont_vestuario += 1
            cont_gastronomia += 3

        if ops_resp_q1[10] in resp:
            cont_cultura += 1
            cont_esporte += 1
            cont_entretenimento += 3
            cont_conexao_social += 3

        if ops_resp_q1[11] in resp:
            cont_entretenimento += 3
            cont_conexao_social += 1
            cont_hobby += 3

    if i == 7:
        if ops_resp_q2[0] in resp:
            cont_cultura += 2
            cont_hobby += 1
            cont_vestuario += 1

        if ops_resp_q2[1] in resp:
            cont_vestuario += 1

        if ops_resp_q2[2] in resp:
            cont_vestuario += 1

        if ops_resp_q2[3] in resp:
            cont_vestuario += 1

        if ops_resp_q2[4] in resp:
            cont_cultura += 1
            cont_vestuario += 1

    if i == 8:
        if ops_resp_q3[0] in resp:
            cont_cultura += 1
            cont_gastronomia += 3

        if ops_resp_q3[1] in resp:
            cont_esporte += 2
            cont_saude += 3
            cont_gastronomia += 3

        if ops_resp_q3[2] in resp:
            cont_esporte -= 1
            cont_saude -= 1
            cont_gastronomia += 3

        if ops_resp_q3[3] in resp:
            cont_cultura += 1
            cont_saude += 2
            cont_gastronomia += 3

        if ops_resp_q3[4] in resp:
            cont_conexao_social += 1
            cont_saude -= 1
            cont_gastronomia += 3

    if i == 9:
        if ops_resp_q4[0] in resp:
            cont_conexao_social += 1
            cont_gastronomia += 3

        if ops_resp_q4[1] in resp:
            cont_conexao_social += 1
            cont_gastronomia += 3

        if ops_resp_q4[2] in resp:
            cont_esporte += 1
            cont_saude += 2
            cont_gastronomia += 3

        if ops_resp_q4[3] in resp:
            cont_esporte -= 1
            cont_saude -= 2
            cont_gastronomia += 1

        if ops_resp_q4[4] in resp:
            cont_conexao_social += 1
            cont_hobby += 1
            cont_gastronomia += 3

        if ops_resp_q4[5] in resp:
            cont_conexao_social += 1
            cont_gastronomia += 3

        if ops_resp_q4[6] in resp:
            cont_esporte += 2
            cont_saude += 3
            cont_gastronomia += 3

        if ops_resp_q4[7] in resp:
            cont_esporte += 1
            cont_saude += 3
            cont_gastronomia += 1

        if ops_resp_q4[8] in resp:
            cont_conexao_social += 1
            cont_hobby += 2
            cont_saude += 1
            cont_gastronomia += 3

    if i == 10:
        if ops_resp_q5[0] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_conexao_social += 2
            cont_hobby += 3
            cont_vestuario += 1
            cont_saude += 1

        if ops_resp_q5[1] in resp:
            cont_cultura += 3
            cont_entretenimento += 3
            cont_conexao_social += 3
            cont_vestuario += 1

        if ops_resp_q5[2] in resp:
            cont_cultura += 3
            cont_entretenimento += 2
            cont_hobby += 1

        if ops_resp_q5[3] in resp:
            cont_conexao_social += 1
            cont_gastronomia += 3

        if ops_resp_q5[4] in resp:
            cont_cultura += 3
            cont_entretenimento += 3
            cont_conexao_social += 1
            cont_hobby += 1

        if ops_resp_q5[5] in resp:
            cont_cultura += 3
            cont_entretenimento += 3
            cont_conexao_social += 1

        if ops_resp_q5[6] in resp:
            cont_conexao_social += 3
            cont_hobby += 1
            cont_gastronomia += 1

    if i == 11:
        if ops_resp_q6[0] in resp:
            cont_esporte += 1
            cont_vestuario += 3

        if ops_resp_q6[1] in resp:
            cont_esporte += 3
            cont_entretenimento += 1
            cont_hobby += 3
            cont_vestuario += 3

        if ops_resp_q6[2] in resp:
            cont_vestuario += 1

        if ops_resp_q6[3] in resp:
            cont_entretenimento += 2
            cont_vestuario += 3

        if ops_resp_q6[4] in resp:
            cont_vestuario += 3

        if ops_resp_q6[5] in resp:
            cont_entretenimento += 1
            cont_conexao_social += 1
            cont_vestuario += 3

        if ops_resp_q6[6] in resp:
            cont_vestuario += 2

    if i == 14:
        if ops_resp_q9[0] in resp:
            cont_vestuario += 3

        if ops_resp_q9[1] in resp:
            cont_hobby += 1

        if ops_resp_q9[2] in resp:
            cont_hobby += 1

        if ops_resp_q9[3] in resp:
            cont_entretenimento += 1

        if ops_resp_q9[4] in resp:
            cont_entretenimento += 1
            cont_hobby += 1

    if i == 15:
        if ops_resp_q10[0] in resp:
            cont_vestuario += 3

        if ops_resp_q10[1] in resp:
            cont_vestuario += 3
            cont_saude += 2

        if ops_resp_q10[2] in resp:
            cont_vestuario += 3

        if ops_resp_q10[3] in resp:
            cont_vestuario += 3

        if ops_resp_q10[4] in resp:
            cont_vestuario += 3

        if ops_resp_q10[5] in resp:
            cont_vestuario += 3

        if ops_resp_q10[6] in resp:
            cont_vestuario += 3

        if ops_resp_q10[7] in resp:
            cont_vestuario += 3

        if ops_resp_q10[8] in resp:
            cont_vestuario += 3

        if ops_resp_q10[9] in resp:
            cont_esporte += 1
            cont_vestuario += 3
            cont_saude += 2

        if ops_resp_q10[10] in resp:
            cont_vestuario -= 3

    if i == 18:
        if ops_resp_q13[0] in resp:
            cont_hobby += 1
            cont_gastronomia += 1

        if ops_resp_q13[1] in resp:
            cont_hobby += 1
            cont_gastronomia += 3

        if ops_resp_q13[2] in resp:
            cont_hobby += 1
            cont_gastronomia += 3

    if i == 19:
        if ops_resp_q14[0] in resp:
            cont_saude -= 1

        if ops_resp_q14[1] in resp:
            cont_saude += 1

        if ops_resp_q14[2] in resp:
            cont_saude += 2

        if ops_resp_q14[3] in resp:
            cont_saude += 3

    if i == 20:
        if ops_resp_q15[2] in resp:
            cont_hobby += 2

    if i == 21:
        if ops_resp_q16[1] in resp:
            cont_conexao_social += 2
            cont_hobby += 2
            cont_gastronomia += 3

        if ops_resp_q16[2] in resp:
            cont_conexao_social += 2
            cont_hobby += 3
            cont_gastronomia += 3

    if i == 22:
        if ops_resp_q17[1] in resp:
            cont_saude += 1
            cont_gastronomia += 3

        if ops_resp_q17[2] in resp:
            cont_saude += 1
            cont_gastronomia += 3

        if ops_resp_q17[3] in resp:
            cont_gastronomia += 3

        if ops_resp_q17[4] in resp:
            cont_gastronomia += 3

        if ops_resp_q17[5] in resp:
            cont_gastronomia += 3

        if ops_resp_q17[6] in resp:
            cont_gastronomia += 3

    if i == 23:
        if ops_resp_q18[1] in resp:
            cont_saude += 3
            cont_gastronomia += 3

        if ops_resp_q18[2] in resp:
            cont_saude += 3
            cont_gastronomia += 3

        if ops_resp_q18[3] in resp:
            cont_saude += 3
            cont_gastronomia += 3

        if ops_resp_q18[4] in resp:
            cont_saude += 3
            cont_gastronomia += 3

    if i == 26:
        if ops_resp_q21[0] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[1] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[2] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[3] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[4] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[5] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[6] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[7] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[8] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

        if ops_resp_q21[10] in resp:
            cont_esporte -= 3
            cont_saude -= 2

        if ops_resp_q21[11] in resp:
            cont_esporte += 3
            cont_entretenimento += 2
            cont_hobby += 1
            cont_saude += 3

    if i == 27:
        if ops_resp_q22[0] in resp:
            cont_saude += 3

        if ops_resp_q22[1] in resp:
            cont_saude += 3

        if ops_resp_q22[3] in resp:
            cont_saude += 2

    if i == 28:
        if ops_resp_q23[0] in resp:
            cont_entretenimento += 1
            cont_saude += 3

        if ops_resp_q23[2] in resp:
            cont_entretenimento += 1
            cont_saude += 1

    if i == 29:
        if ops_resp_q24[0] in resp:
            cont_saude += 3

        if ops_resp_q24[2] in resp:
            cont_saude += 2
