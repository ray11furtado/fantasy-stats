import smtplib 
from datetime import datetime

# gmail
# yahoo
# outlook hotmail
#login takes your email and password
#send takes the recipient of email, subject, and the text
class emailer:
  def __init__(self, service):
    service = service.lower()
    if service == 'gmail':
      service = 'smtp.gmail.com'
    elif service == 'outlook' or service == 'hotmail':
      service = 'smtp-mail.outlook.com'
    elif service == 'yahoo':
      service = 'smtp.mail.yahoo.com'
    else:
      raise NameError('Please enter, gmail, yahoo, outlook or hotmail') 
    self.conn = smtplib.SMTP(service, 587)
    self.conn.ehlo()
    self.conn.starttls()

  def login(self, email, pw):
    self.email = email
    self.conn.login(email, pw)

  def send(self, recipient, subject, text):
    self.conn.sendmail(self.email, recipient, subject, text)


