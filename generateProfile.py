#!/usr/bin/env python
import json


class GenerateProfile(object):
    
    """
    The goal here is to check if a user profile exists. 
    User profiles will be in JSON format for easy data retrieval and entry
    
    If the file does not exists. createProfile will be called and used to create
    the file by asking the user information. 
    """
    
    def __init__(self, profile):
        self.profile = profile
        if os.path.isfile(self.profile):
            return True
        else:
            createProfile()
             
        
        
    def createProfile(self):
        
           