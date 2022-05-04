# Envoie de mail avec python
import os
import sys
import base64
import html
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart



sender_mail = "xxxxx@vde.fr"
receiver_mail = "xxxxxx@vde.fr"
receiver_mail_cc = "xxxxxxx@vde.fr, xxxxxx@vde.fr"
receiver_mail_bcc = ""

path = '\\Silnas100.prodgrp.local\\BUREAUTIQUE$\\EQUIPE\\DBL_EBL_EBL\\EBL - Référentiel Applications (Application, IEM, MOE)\\EPC - Référentiel Applications.xlsx'
base = os.path.basename(path)

msg = MIMEMultipart('alternative')
msg["From"] = sender_mail
msg["To"] = receiver_mail
msg["Cc"] = receiver_mail_cc
msg["Bcc"] = receiver_mail_bcc
msg["Subject"] = "[BPC]Mise à jour du référentiel des applications"

toaddrs = [receiver_mail] + [receiver_mail_cc] + [receiver_mail_bcc]

with open((r'\\Silnas100.prodgrp.local\\BUREAUTIQUE$\\EQUIPE\\DBL_EBL_EBL\\EBL - Référentiel Applications (Application, IEM, MOE)\\EPC - Référentiel Applications.xlsx'), 'rb') as attachment:
    part = MIMEBase("application", "octet-stram")
    part.set_payload(attachment.read())

part.add_header(
    "Content-Disposition",
    "attachment", filename=base
    )
msg.attach(part)
recv1 = "xxxxxxx@vde.fr"
recv2 = "xxxxxx@vde.fr"

texto =f""" 
Bonjour, 
Une nouvelle version est à mettre à jour sous Carine.
Par avance, je vous en remercie.
Merci de confirmer la bonne prise en compte à {recv1} et à {recv2}.

Bien Cordialement !"""
body = texto
msg.attach(MIMEText(body, 'htmml'))
# importer l'image
#img ="D:\\Applis\\automatisation\\mail\\bpc\\signature_bpc.png"
#from PIL import image
#im = Image.open(img)
#im.show()


#img ="D:\\Applis\\automatisation\\mail\\bpc\\signature_bpc.png"
#img_data = open(img, "rb").read()
#image = MIMEImage(img_data, base = os.path.basename(img))
#msg.attach(image,'img')



#data_uri = base64.b64encode(open('D:\\Applis\\automatisation\\mail\\bpc\\signature_bpc.png', 'rb').read()).decode('utf-8')
#img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)


email.encoders.encode_base64(part)

server = smtplib.SMTP('federateur-applis.prodinfo.gca')

server.sendmail(sender_mail, toaddrs, msg.as_string())

server.quit()





