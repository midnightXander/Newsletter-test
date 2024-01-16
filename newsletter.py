import smtplib
import ssl

from dotenv import load_dotenv
import os

from email.message import EmailMessage
#load secrets from .env
load_dotenv()

gmail_adress = os.getenv("GMAIL_ADRESS")
gmail_pwd = os.getenv("GMAIL_PASSWORD") 

#create the email
email = EmailMessage()

#subject of the email
email["Subject"] = "Newsletter test"

#sender's adress
email["From"] = gmail_adress

#adding html 
email.add_alternative(f"""\
    <html>
    <head></head>
    <body>
    <p><b>Ready to receive incredible news?</b></p>
    </body>
    </html>
    """,subtype="html")

#add content as a fallback option
#email.set_content("just testing...")

#send email to subscribers list
subscriber_email_adresses = ["denzelwashington913@gmail.com","denzeldecode@gmail.com","melidaletha@gmail.com"]

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as smtp_server:
    smtp_server.login(gmail_adress,gmail_pwd)

    for subscriber_email_adress in subscriber_email_adresses:
        #receiver's adress
        email["To"] = subscriber_email_adress
        
        #send the message
        smtp_server.send_message(email)
        del email["To"]
        print("sent")


