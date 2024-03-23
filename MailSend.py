import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = "yuhtian23ok@gmail.com"
receiver = "ctho64571@gmail.com"

msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = Header("Test of sending email", "utf-8").encode()

body = "This is a test email sended by Python"

msg.attach(MIMEText(body))

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender,"qqtrniorianwdjka")
    server.sendmail(sender, receiver, msg.as_string())
print("Send email success!")

