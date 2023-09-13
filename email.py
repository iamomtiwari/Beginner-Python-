from email.message import EmailMessage
from email import password
import ssl
import smtplib

email_sender="imomtiwari@gmail.com"
email_password=password

email_reciever='rovow21886@irebah.com'

subject="Prepare for GRE"
body=""" 
start preparing ASAP"""

em=EmailMessage()
em['From']==email_reciever
em['To']=email_reciever
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever, em.as_string())
