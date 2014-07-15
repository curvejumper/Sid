#!/usr/bin/env python
from brain import Brain
from mpd import MPDClient
import imaplib
import email
import re
import time
from dateutil import parser

class Conversation(object):
    
    def __init__(self, profile):
        self.profile = profile
        self.brain = Brain(profile)
        
    def delegateInput(self, text):
        """A wrapper for querying brain """
        
        self.brain.query(text)
    
    def get_first_text_part(self, msg):
        """Decodes the email's encryption and gives back plaintext email body """
	maintype = msg.get_content_maintype()
	if maintype == 'multipart':
	    for part in msg.get_payload():
		if part.get_content_maintype() == 'text':
			return part.get_payload(decode=True)
	elif maintype == 'text':
	    return msg.get_payload(decode=True)
        
    
    def getSender(self, email):
        """
            Returns the best-guess sender of an email.
    
            Arguments:
            email -- the email whose sender is desired
    
            Returns:
            Sender of the email.
        """
        sender = email['From']
        m = re.match(r'(.*)\s<.*>', sender)
        if m:
            return m.group(1)
        return sender
    
    def fetchCloudCommand(self, user_phone, since=None, markRead=False):
        """
            This opens the IMAP4 connection with information about the email account.
            It will then look for the clients phonenumber in the unread emails
            If found, it will take the body of the message and return it as a string
            
            Arguments:
                user_phone -- The user's profile phonenumber to match with sender email address
            Returns:
                String of the body of email(former text message)
        """
        try:
	    conn = imaplib.IMAP4_SSL('imap.gmail.com')
	except:
	    print 'Could not connect to gmail server'
	    return None
        try:
            conn.debug = 0
            conn.login(self.profile['jarvis_address'], self.profile['jarvis_password'])
            conn.select(readonly=(markRead))
            (retcode, messages) = conn.search(None, '(UNSEEN)')
            if retcode == 'OK' and messages != ['']:
                for num in messages[0].split(' '):
                    #parse email RFC822 format
                    ret, data = conn.fetch(num, '(RFC822)')
                    msg = email.message_from_string(data[0][1])
                    if not since or getDate(msg) > since:
                        phone_email = self.getSender(msg)
                        if re.search(r'\b%s\b' %user_phone, phone_email, re.IGNORECASE):
                            command = self.get_first_text_part(msg)
                            conn.close()
                            conn.logout()
                            return command
                        else:
                            conn.uid('store', num, '+FLAGS', 'UNSEEN')
                    
            conn.close()
            conn.logout()
        except:
            print 'error in conversation fetchCloudCommand'
	return None
	
    
    
    def cloudCommand(self):
        user_phone = self.profile['phone_number']
        if user_phone:
            msgs = self.fetchCloudCommand(user_phone)
        else:
            print 'Phone number could not be found, try reediting your profile'
        
        return msgs
        
    
    
    def userInput(self):
        """
        The user will give Jarvis a command from a text message to jarvis
        
        it will check to see if email is set up and if so, will parse through new
        emails to check for one from the users phone number.
        
        If the user did not give the profile a phone or gmail, it will still allow commands from teh terminal
        """
        phone_command = self.cloudCommand()
	if phone_command:
            return phone_command
        
        
    
    def handleForever(self):
        """Delegates user input to the handling function when activated"""
        
        while True:
            
            #activate delegateInput if signaled by client
            command = self.userInput()
            try:
                self.delegateInput(command)
	    except:
	        print "nothing to report"
	    time.sleep(60)
		
            
    
        
    

