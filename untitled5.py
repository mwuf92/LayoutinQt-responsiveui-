# -*- coding: utf-8 -*-
"""
Created on Tue May  2 19:07:02 2023

@author: admin
"""

from PyQt5 import QtCore, QtGui, QtWidgets,uic

class MyWindow (QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('login.ui', self)
        

    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
           
        
        
