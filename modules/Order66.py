#!/usr/bin/env python

"""
    This is just for fun
"""

import re
from cloudText import *

WORDS = ['Order', '66']

def handle(text, profile):
    """
        Takes in the order
        executes it to the fullest extent
    """
    message = "youtu.be/tCuUIkEtJjo"
    execute = cloudText(profile, message)
    execute.sendResponse()
    print 'it is done'

def isValid(text):
    """
        Returns true if the input is related to this command
    """
    
    return bool(re.search(r'\border\s66\b', text, re.IGNORECASE))