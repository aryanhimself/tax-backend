import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = 'sandbox.smtp.mailtrap.io'
PORT = 587
SENDER_MAIL = 'tax_payment_system@gmail.com'
USERNAME = 'd22b17c4774d31'
PASSWORD = '8bdcc25c172684'


def send_mail(receiver, subject, body):
    smtp_server = smtplib.SMTP(HOST, PORT)
    smtp_server.connect(HOST, PORT)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.ehlo()
    smtp_server.login(USERNAME, PASSWORD)

    message = MIMEMultipart()
    message['From'] = SENDER_MAIL
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    smtp_server.sendmail(
        SENDER_MAIL,
        receiver,
        message.as_string()
    )
