#!/usr/bin/env python

import smtplib

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
