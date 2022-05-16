import os
import sys
import base64
import smtplib
import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

sender_mail = "cluster_BPCA_exploitation@ca-gip.fr"
receiver_mail = "exploitation.bureau.entree@ca-gip.fr"
receiver_mail_cc = "CAGIP_SUPERVISION_PPX@ca-gip.fr, CAGIP_PSL_DBL_GDC@ca-gip.fr"
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

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    "attachment", filename=base
    )
msg.attach(part)

data_uri = base64.b64encode(open('D:\\Applis\\automatisation\\mail\\bpc\\signature_bpc.png', 'rb').read()).decode('utf-8')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

html = """\
<html>
    <body>
        <p>Bonjour,</p>
        <p>Une nouvelle version est à mettre à jour sous Carine.</p>
        <p>Par avance, je vous en remercie.</p>
        <p>Cordialement,</p>
        <p><i>PS: merci de confirmer la bonne prise en compte à </i>CAGIP_SUPERVISION_PPX@ca-gip.fr<i> et </i>CAGIP_PSL_DBL_GDC@ca-gip.fr</p>
        <p><var>{img_tag}</var></p>
    </body>
</html>
""".format(**locals())

part = MIMEText(html, 'html')
msg.attach(part)

encoders.encode_base64(part)

server = smtplib.SMTP('federateur-applis.prodinfo.gca')

server.sendmail(sender_mail, toaddrs, msg.as_string())
server.quit()
