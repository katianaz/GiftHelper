import smtplib, ssl
import pandas as pd

sender_email = "gifthelper.cwb@gmail.com"
password = input("Type your password and press enter: ")

# data handling
df_respostas = pd.read_csv('respostas.csv', encoding='utf-8"')

# Create a secure SSL context
port = 465  # For SSL
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    for i in range(0,len(df_respostas)):
        message = "Subject: Presente!\n\n" + "Hey " + df_respostas['Nome'][i] + "! Como vai?\nVocê acaba de receber a lista de sugestões para presentes do GiftHelper!\nAgradecemos a confiança e com certeza " + df_respostas['Presenteado'][i] + " vai curtir muito o presente. Segue a lista de sugestões que preparamos para você:\n" + df_respostas['Sugestoes de presente'][i]
        message=message.encode('utf-8')
        server.sendmail(sender_email, df_respostas['Email'][i], message)
        