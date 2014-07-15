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
	try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.profile['jarvis_address'], self.profile['jarvis_password'])
            server.sendmail('Jarvis', self.user_phone + '@' + self.carrier, self.response)
	except:
	    print 'Error in sendResponse function of cloudText'
    
    def text_other(self, text):
        #needs to find phonenumber and message to send
        phone_numbers = re.findall(r'\b(\d{3})\D*(\d{3})\D*(\d{4})\b',text)
	if phone_numbers:
	    for the_numbers in phone_numbers:
	        phone_number = ''.join(the_numbers)
            messages = re.findall(r'message:\s(.+)\sstop', text, re.IGNORECASE)
            for body in messages:
                message = body
            new_response = self.response + message
            #will find the carrier of said phonenumber
            self.send_to_rando(phone_number, new_response)
	else:
	    print 'did not find phone number'
    
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
        server.sendmail('Jarvis', self.user_phone + '@' + self.carrier, self.response)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.profile['jarvis_address'], self.profile['jarvis_password'])
            server.sendmail('Jarvis', self.user_phone + '@' + self.carrier, self.response)
	    for carrier in carriers:
            	server.sendmail('Jarvis', phone_number + '@' + carrier, message)
	    print '====================================================='
	    print phone_number + '@' + carrier + '  message: ' + message
	    print '====================================================='
	    server.quit()
        except:
            print 'error in send_to_rando function'
        