#!/usr/bin/env python
import yaml
import sys
from conversation import Conversation


if __name__ == '__main__':
    
    print "================================================="
    print " Jarvis personal assistant extraordinar          "
    print " By Michael Ortiz                                "
    print " ================================================"
    
    profile = yaml.safe_load(open("profile.yml", "r"))
    
    conversation = Conversation(profile)
    
    conversation.handleForever()
    
