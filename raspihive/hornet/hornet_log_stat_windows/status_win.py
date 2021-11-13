###############################################################################
# libraries
import os
from PyQt5 import QtGui, QtWidgets, Qt

#absolute import
#from raspihive.gui_window1 import Window1
#/home/paul/Dokumente/raspihive_rebuild/raspihive/raspihive

#from .helpers import os_parse

#test import for cpu and ram values etc.
#import psutil
###########################################################################
# Hornet Status
class hornet_status_win(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)
        #Set window position and size
        super().__init__()
        #self.left = 300
        #self.top = 100
        #self.width = 1100
        #self.height = 500
        #End of set window position and size
        #Window size
        #self.setGeometry(self.left, self.top, self.width, self.height)

        #self.setFixedSize(1000, 1000)
        self.setStyleSheet('background-color: #2B3440') #rgb(255,255,255);
        self.setWindowTitle('Hornet-Status')

        #Test
        # For hornet node status
        Outputfileobject = os.popen("service hornet status")     #sudo service hornet status
        Output = Outputfileobject.read()
        Outputfileobject.close()

         #Create label
        labelT = QtWidgets.QLabel(self)
        #Set label text
        labelT.setText(Output)
        #Set label font
        labelT.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Black))
        # setting up background and text color
        labelT.setStyleSheet("background-color: #2B3440; color: white; border: \
        0px solid black")
        #Setting position x y
        labelT.move(20, 10)
        #Setting label width
        labelT.setFixedWidth(1100)
        labelT.setFixedHeight(500)
        #End label

        # creating a quit button
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(0, 0, 150, 40)
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #2B3440; color: white')
        #Setting button text
        self.pushButton.setText('Quit status window')
        # adding action to a button
        self.pushButton.clicked.connect(self.close)
        # End of creating a quit button

        # opening window in maximized size
        self.showMaximized()

#End of Hornet Status
