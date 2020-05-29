import pontuacao_categorias
import pandas as pd

nomes = []
nomes_presenteados = []
enderecos_emails = []

for p in range(len(pontuacao_categorias.tabela.index)):
    nomes.append(pontuacao_categorias.tabela['3'][p])
    nomes_presenteados.append(pontuacao_categorias.tabela['4'][p])
    enderecos_emails.append(pontuacao_categorias.tabela['2'][p])

informacoes = {'Nome': nomes,
               'Email': enderecos_emails,
               'Presenteado': nomes_presenteados,
               'Sugestoes': pontuacao_categorias.sugestoes}

infos = pd.DataFrame(informacoes, columns=['Nome', 'Email', 'Presenteado', 'Sugestoes'])

infos.to_csv('infos_emails.csv', encoding='latin-1')
