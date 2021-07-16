from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage
import smtplib

from_email = 'SEU EMAIL'
from_pass = 'SUA SENHA'

msg = MIMEMultipart()
msg['from'] = 'SEU NOME'
msg['to'] = 'EMAIL DO DESTINATÁRIO'
msg['subject'] = 'Este é o nosso primeiro contato'
body = MIMEText('Este é um texto simples para o envio de um primeiro email')
msg.attach(body)

with open('hello.png', 'rb') as img:
    image = MIMEImage(img.read())
    msg.attach(image)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(from_email, from_pass)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except: 
        print('Erro ao enviar e-mail')