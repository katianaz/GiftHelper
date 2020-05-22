import smtplib, ssl

sender_email = "gifthelper.cwb@gmail.com"
receiver_email = "gifthelper.cwb@gmail.com"
password =  input("Type your password and press enter: ")

port = 465  # For SSL

message = """\
Subject: Lista de Presentes GiftHelper

Hey, NOME! Como vai?

Você acaba de receber a lista de sugestões para presentes do GiftHelper! 
Agradecemos a confiança e com certeza você dará o presente ideal.


Att,
Equipe GitHelper

"""


# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)