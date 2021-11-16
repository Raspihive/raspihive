#!/usr/bin/env python3
"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""
# libraries
import os
from PyQt5 import QtGui, QtWidgets, Qt


#from .helpers import os_parse

#test import for cpu and ram values etc.
#import psutil
###########################################################################
#Hornet Log
class hornet_log_win(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)
        #Set window position and size
        super().__init__()
        self.left = 300
        self.top = 100
        self.width = 1450
        self.height = 810
        #End of set window position and size
        #Window size
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.setFixedSize(1000, 1000)
        self.setStyleSheet('background-color: #2B3440') #rgb(255,255,255);  #2B3440
        self.setWindowTitle('Hornet-Logs')

        # For hornet node logs
        Outputfileobject = os.popen("journalctl -u hornet -n 50")
        Output = Outputfileobject.read()
        Outputfileobject.close()

        #Create label
        labelT = QtWidgets.QLabel(self)
        #Set label text
        labelT.setText(Output)
        #Set label font
        labelT.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Black))
        # setting up background and text color
        labelT.setStyleSheet("background-color: #2B3440 ; color: white; border: \
        0px solid black")
        #Setting position x y
        labelT.move(10, 30)
        #Setting label width
        labelT.setFixedWidth(1450)
        #Setting label height
        labelT.setFixedHeight(810)
        #End label

        # creating a quit button
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(0, 0, 150, 40)
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #2B3440; color: white')
        #Setting button text
        self.pushButton.setText('Close log window')
        # adding action to a button
        self.pushButton.clicked.connect(self.close)
        # End of creating a quit button

        # opening window in maximized size
        self.showMaximized()

#End of Hornet Log
