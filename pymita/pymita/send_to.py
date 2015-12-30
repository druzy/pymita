#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 déc. 2015

@author: druzy
'''

from py_druzy_mvc.controller import Controller
from py_druzy_mvc.view import View
from py_druzy_mvc.model import Model
from send_to_ui import Ui_Form
import sys
from PyQt4 import QtGui

class SendTo(Controller):
    
    def __init__(self,model):
        Controller.__init__(self, model)
        self.add_view(SendToView(self))
        
class SendToView(View,QtGui.QMainWindow):
    
    
    
    def __init__(self,controller):
        View.__init__(self, controller)
        
        self.app = QtGui.QApplication(sys.argv)
        
        QtGui.QWidget.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
    def display(self):
        self.show()
        sys.exit(self.app.exec_())
        
class SendToModel(Model):
    
    def __init__(self):
        Model.__init__(self)
        
if __name__=="__main__":
    
    s=SendTo(SendToModel())
    s.display_views()
    
   