import smtplib
"""
    Provider                     SMTP server domain name 
====================================================================
    Gmail                        smtp.gmail.com  (port 587)
    Outlook.com/Hotmail.com      smtp-mail.outlook.com  (port 587)
    Yahoo Mail                   smtp.mail.yahoo.com  (port 587)
    AT&T                         smpt.mail.att.net (port 465)
    Comcast                      smtp.comcast.net  (port 587)
    Verizon                      smtp.verizon.net (port 465)
"""

mail_username = ''
mail_password = ''
reciever_username = ''
SUBJECT =''
TEXT =''
messsage = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(mail_username,mail_password)
if smtp_object.login:
    smtp_object.sendmail(mail_username,reciever_username,messsage)
    print('Message Sent')
else:
    print("Invalid credentials")
smtp_object.quit()
