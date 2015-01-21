#!/usr/bin/env python
import sys
from conversation import Conversation


if __name__ == '__main__':
    
    """
    This is the main file that will simply start the process of conversing with the user.
    The program will load a profile (if present) and then go to the conversation class for 
    constant handleing of the program 
    
    """
    
    print("=================================================")
    print(" Sid personal assistant extraordinar          ")
    print(" By Michael Ortiz                                ")
    print(" ================================================")
    
    
    generateProfile('user.txt')
    
    conversation = Conversation(profile)
    
    conversation.handleForever()
    
