#!/usr/bin/python
# Code to send Email from AMDENV1 in Python v2.6
import smtplib


def email():

    sender = 'amdenv1@blp13626001.eezone.bt.com'
    receivers = ['vinil.mehta@amdocs.com']

    message = """From: amdenv1@blp13626001.eezone.bt.com
    To: To Vinil Mehta
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """

   try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender,receivers, message)
	   print "Successfully sent email"
   except smtplib.SMTPException:
       print 'Error: unable to send email'