import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

# Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Se autentica
gc = gspread.authorize(credentials)

# Abre a planilha
wks = gc.open_by_key('1l1fq6h4vH7S1OctNAboTq0ekGFVEtZWXPCSa7lCdliw')

# Seleciona a primeira página da planilha
planilha = wks.get_worksheet(0)

with open('dados_formulario.csv', 'w', newline='') as csvfile:
    esc = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for i in range(1, len(planilha.get_all_values())+1):
        esc.writerow(planilha.row_values(i))
