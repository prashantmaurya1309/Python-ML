# import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
# fromaddr = "test1@example.com"
# toaddr = "test2@example.com"
# msg = MIMEMultipart()
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "Test Mail"
# body = "Test mail from python"
# msg.attach(MIMEText(body, 'plain'))
# server = smtplib.SMTP('smtp.example.com', 25)
# server.ehlo()
# server.starttls()
# server.ehlo()
# server.login(fromaddr, "password")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()



#  this is correct form for aboc=ve code----

# server = smtplib.SMTP('smtp.example.com', 25)
# server.connect("smtp.example.com",465)
# server.ehlo()
# server.starttls()
# server.ehlo()
# server.login(fromaddr, "password")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()




import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.google.com',25)  # 25 is port number
server.connect('smtp.google.com',465)

server.ehlo()  # to start the whole proccess
server.starttls()
server.ehlo()

with open('gmail pass.txt','r') as f:
    password = f.read()

server.login('amanrajsdpa78e2@gmail.com', password)

msg=MIMEMultipart()
# header
msg['From']='amanrajsdpa78e2@gmail.com'
msg['To']='prashantmaurya1309@gmail.com'
msg['Subject']='test mail'

with open('email msg','r') as f:
    message=f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'unnamed (1).jpg'
attachment = open(filename,'rb')

p= MIMEBase('application','octet-stream')  # An email message consists of headers and a payload (which is also referred to as the content)
# p stands for payload
p.set_payload((attachment.read()))

encoders.encode_base64((p))
p.add_header('Content-Disposition', f'attachment ; filename={filename}')
msg.attach(p)

text=msg.as_string()
server.sendmail('amanrjsdpa78e2@gmail.com','prashantmaurya1309@gmail.com',text)