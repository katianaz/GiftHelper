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
worksheet = wks.get_worksheet(0)
