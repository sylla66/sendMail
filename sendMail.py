import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from html import code_html

fromaddr = 'Team SendMail <no-reply@orange-sonatel.com>'


def envoieMail(etat, fromaddr, toaddr):
    # # instance of MIMEMultipart
    msg = MIMEMultipart()

    # # storing the senders email address
    msg['From'] = fromaddr

    # # storing the receivers email address
    msg['To'] = ", ".join(toaddr)

    # # storing the subject
    msg['Subject'] = f"Résultats du modèle jeune"

    if (etat == "success"):

        # # string to store the body of the mail
        body = code_html()

        # # attach the body with the msg instance
        part2 = MIMEText(body, 'html')
        msg.attach(part2)
        s = smtplib.SMTP('', 25)

        # # Converts the Multipart msg into a string
        text = msg.as_string()

        # # sending the mail
        s.sendmail(fromaddr, toaddr, text)

    else:
        # # string to store the body of the mail
        body = f'''
            <br>Bonjour, 
            <br>
            <p>Une erreur à été notée lors de l'execution du Modele Jeune:</p>

            <br>Cordialement 
            <br>
          '''

        # # attach the body with the msg instance
        part2 = MIMEText(body, 'html')
        msg.attach(part2)
        s = smtplib.SMTP('', 25)

        # # Converts the Multipart msg into a string
        text = msg.as_string()

        # # sending the mail
        s.sendmail(fromaddr, toaddr, text)


fromaddr = 'Team SendMail <>'
toaddr = ['hamidou.sylla@orange-sonatel.com']
etat = "success"

if __name__ == '__main__':
    envoieMail(etat, fromaddr, toaddr)