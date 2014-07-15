#!/usr/bin/env python

"""
    This module will text another person at any time the client wishes

    goals:
        -take in desired message with a time stamp
        -send the message at the desired time
        
    extra credit:
        -allow recipent to send back a reply to Jarvis for the client
"""

import re
from cloudText import *

WORDS =['text', 'other']

def handle(text, profile):
    """
        takes in the text and parses it:
            1.finds phonenumber of recipent
            2.finds message for recipient
            3.finds optional name of recipient
            4.finds optional time to send message to recipiant (do later)
    """
    #finds a phonenumber in any form; hyphens, spaces or no spaces
    message = 'The great Michael Ortiz himself wanted me to send you this message: '
    #try:
    to_receiver = cloudText(profile, message)
    #print 'message to other sent'
    #except:
    #print 'error in textOther.py handle function'
    #try:
    to_receiver.text_other(text)
    #print 'message to other sent'
    #except:
    #print 'error2 in textOther.py cloudText function'
    
    
    
    
def isValid(text):
    """
        Returns true if the input is related to this command
    """
    
    return bool(re.search(r'\btext|message|send\b', text, re.IGNORECASE))