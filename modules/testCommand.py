#!/usr/bin/env python

import re
from cloudText import *

WORDS = ['test', 'testing']

def handle(text, profile):
    """
        Responds to user input
        
        Arguments:
        text: the user input
        profile: information on the client
    """
    message = "This is the test message"
    try:
        test = cloudText(profile, message)
    except:
        print 'it didnt work'
    #try:
    test.sendResponse()
    #except:
    #print 'This part is still not working'
    print message

def isValid(text):
    """
        Returns true if the input is related to this command
    """
    
    return bool(re.search(r'\btest|testing\b', text, re.IGNORECASE))

