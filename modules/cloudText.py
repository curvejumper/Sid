#!/usr/bin/env python

import smtplib
import re

class cloudText(object):
    """
    This will take a string from a module and send it to the
    client
    
    """
    def __init__(self, profile, response):
        self.profile = profile
        self.response = response
        self.user_phone = self.profile['phone_number']
        self.carrier = self.profile['carrier']
        
    def sendResponse(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.profile['jarvis_address'], self.profile['jarvis_password'])
        server.sendmail('Jarvis', self.user_phone + '@' + self.carrier, self.response)
    
    def text_other(self, text):
        #needs to find phonenumber and message to send
        phone_numbers = re.findall(r'\b(\d{3})\D*(\d{3})\D*(\d{4})\b$',text)
        for phone_number in phone_numbers:
            receiver_phone = ''.join(phone_number)
        
        messages = re.findall(r'message:\s(.+)\sstop', text, re.IGNORECASE)
        for body in messages:
            message = body
        new_response = self.response + message
        #will find the carrier of said phonenumber
        send_to_rando(receiver_phone, new_response)
    
    def send_to_rando(self, phone_number, message):
        carriers = ['message.alltel.com',
                    'txt.att.net',
                    'tmomail.net',
                    'vmobl.com',
                    'messaging.sprintpcs.com',
                    'vtext.com',
                    'messaging.nextel.com',
                    'mms.uscc.net']
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.profile['jarvis_address'], self.profile['jarvis_password'])
        try:
            for carrier in carriers:
                server.sendmail('Jarvis', phone_number + '@' + carrier, message)
        except:
            print 'error in send_to_rando function'
        