#!/usr/bin/python
# Code to send Email from AMDENV1 in Python v2.6
"""
Objective: This code will send email to Amdocs machine from amdenv1
"""
import smtplib

sender = 'amdenv1@blp13626001.eezone.bt.com'
receiver = ['vinil.mehta@amdocs.com']


def email(*args):
    message = """From: amdenv1@blp13626001.eezone.bt.com
    To: To Vinil Mehta
    Subject: SMTP e-mail test

    This is a test e-mail message.
    """
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receiver, message)
        print("Successfully sent email")
    except smtplib.SMTPException as e:
        print('Error: unable to send email', e)


email(sender, receiver)
