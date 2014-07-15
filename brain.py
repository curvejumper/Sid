#!/usr/bin/env python
import logging
from os import listdir
from cloud import *

class Brain(object):
    
    def __init__(self, profile):
        """
        Instantiates a new Brain object, which takes in user input and checks
        it with a list of modules.
        the order of the modules is important, the Brain can stop looking if
        it finds one that acepts a given input
        
        Arguments:
        profile -- contains information related to the user
        (e.g., email, phone number, location)
        """
        
        def get_modules():
            """
            Dynamically loads all the modules in the modules folder and sorts them
            by PRIORITY key. Default is 0
            """
            
            folder = 'modules'
            
            def get_module_names():
                module_names = [m.replace('.py', '') for m in listdir(folder) if m.endswith('.py')]
		module_names = map(lambda s: folder + '.' + s, module_names)
                return module_names
            
            def import_module(name):
                mod = __import__(name)
                components = name.split('.')
                for comp in components[1:]:
                    mod = getattr(mod, comp)
                return mod
            
            def get_module_priority(m):
                try:
                    return m.PRIORITY
                except:
                    return 0
                
            modules = map(import_module, get_module_names())
            modules = filter(lambda m: hasattr(m, 'WORDS'), modules)
            modules.sort(key=get_module_priority, reverse=True)
	    print modules
            return modules
        
        self.profile = profile
        self.modules = get_modules()
            
            
        
        
    def query(self, text):
        """
        Passes user input to the appropiate module, testing it against
        each candidate module's  isValid function
        
        Arguments:
        text -- user input, to be parsed by a module
        """
	validCommand = 0
        for module in self.modules:
            if module.isValid(text):
                #try:
                module.handle(text, self.profile)
                validCommand = 1;
                #break
                #except:
		#print 'error in query'
                #break
        
        if validCommand != 1:
            error = cloudText(self.profile, "Command was not recognized, please try again")
            error.sendResponse()

