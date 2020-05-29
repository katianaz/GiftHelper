import smtplib
import ssl
import pandas as pd
import password

sender_email = "gifthelper.cwb@gmail.com"
password = password.a

# data handling
df_respostas = pd.read_csv('infos_emails.csv', encoding='latin-1')

# Create a secure SSL context
port = 465  # For SSL
context = ssl.create_default_context()

"""with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    for i in range(0, len(df_respostas)):
        message = "Subject: Presente!\n\n" + "Hey " + df_respostas['Nome'][i] + "! Como vai?\nVocê acaba de receber a lista de sugestões para presentes do GiftHelper!\nAgradecemos a confiança e com certeza " + df_respostas['Presenteado'][i] + " vai curtir muito o presente. Segue a lista de sugestões que preparamos para você:\n" + df_respostas['Sugestoes'][i]
        message = message.encode('latin-1')
        server.sendmail(sender_email, df_respostas['Email'][i], message)"""

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    message = "Subject: Presente!\n\n" + \
              "Hey " + df_respostas['Nome'][0] + "! Como vai?\n" \
              "Você acaba de receber a lista de sugestões para presentes do GiftHelper!\n" \
              "Agradecemos a confiança e com certeza " + df_respostas['Presenteado'][0] + \
              " vai curtir muito o presente. Segue a lista de sugestões que preparamos para você:\n" + \
              df_respostas['Sugestoes'][0]

    message = message.encode('latin-1')
    server.sendmail(sender_email, df_respostas['Email'][0], message)  # algoritmo para teste
