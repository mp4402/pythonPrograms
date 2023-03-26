import smtplib

sender = 'mariopisquiy@ufm.edu'
receivers = ['mario897071@gmail.com']

message = """From: Mario Pisquiy mariopisquiy@ufm.edu
To: Enrique Gómez mario897071@gmail.com
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except:
   print("Error: unable to send email")
