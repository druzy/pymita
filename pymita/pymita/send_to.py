#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 déc. 2015

@author: druzy
'''

from py_druzy_mvc.controller import Controller

class SendTo(Controller):
    
    def __init__(self,model):
        Controller(self,model)
        
        