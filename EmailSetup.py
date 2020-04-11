#!/usr/bin/python
# Code to send Email from AMDENV1 in Python v2.6
"""
Objective: This code will send email to Amdocs machine from amdenv1
"""
import smtplib

sender = 'hostname'
receiver = ['email_id']


def email(*args):
    message = """From: host_name
    To: To User NAme
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
