import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações de e-mail
email_host = 'smtp.example.com'  # O servidor de e-mail
email_port = 587  # Porta do servidor de e-mail
email_username = 'seu_email@example.com'
email_password = 'sua_senha'
sender_email = 'seu_email@example.com'

# Função para enviar e-mail
def enviar_email(destinatario, assunto, corpo):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))
    
    try:
        server = smtplib.SMTP(email_host, email_port)
        server.starttls()
        server.login(email_username, email_password)
        server.sendmail(sender_email, destinatario, msg.as_string())
        server.quit()
        print(f'E-mail enviado para {destinatario}')
    except Exception as e:
        print(f'Erro ao enviar e-mail: {str(e)}')

dados = pd.read_csv('dados_usuario.csv')

for index, row in dados.iterrows():
    nome_cliente = row['Nome']
    email_cliente = row['Email']
    novidades_design = row['Novidades']


    if novidades_design:
        assunto = 'Novidades em Arte - Revista Artê'
        corpo = f'Olá, {nome_cliente}!\n\nHá novidades emocionantes no mundo da arte. Visite nosso site para saber mais.'
        enviar_email(email_cliente, assunto, corpo)

# Encerramento da Pipeline ETL
print('Pipeline ETL concluída.')