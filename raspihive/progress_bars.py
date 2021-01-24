###############################################################################
# libraries
import sys, time, os, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QProgressBar, QPushButton, QAction, qApp, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtGui
from subprocess import Popen, PIPE
from PyQt5.QtWidgets import (QMainWindow, QToolTip, QLabel, QVBoxLayout, QTabWidget, QHBoxLayout)
from PyQt5.QtCore import pyqtSlot, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QFont, QCursor, QImage

from .threads import *

##############################################################################
#Progress bar for OS Update
class Window_os_update(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2B3440; color: black;') #rgb(255,255,255);
        self.title = "OS Update"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        #self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}""QProgressBar::chunk {background:black}")
        #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightblue, stop: 1 lightblue); }")
        #self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        #self.startProgressBar(self)
        self.setLayout(vbox)
        self.show()

    #def startProgressBar():
        self.thread = MyThread_os_update()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
    
    
    def setProgressVal(self, val):
        self.progressbar.setValue(val)
#End of Progress bar for OS Update
##############################################################################

###############################################################################
#Progress bar for packages update
class Window_packages(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2B3440; color: black;') #rgb(255,255,255);
        self.title = "Packages Update"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        #self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}""QProgressBar::chunk {background:black}")
        #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightblue, stop: 1 lightblue); }")
        #self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        #self.startProgressBar(self)
        self.setLayout(vbox)
        self.show()

    #def startProgressBar():
        self.thread = MyThread_packages()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
 
    def setProgressVal(self, val):
        self.progressbar.setValue(val)
#End of Progress bar for packages update
###############################################################################

###############################################################################
#Progress bar for hornet update
class Window_hornet_update(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2B3440; color: black;') #rgb(255,255,255);
        self.title = "Hornet Update"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        #self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}""QProgressBar::chunk {background:black}")
        #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightblue, stop: 1 lightblue); }")
        #self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        #self.startProgressBar(self)
        self.setLayout(vbox)
        self.show()

    #def startProgressBar():
        self.thread = MyThread_hornet_update()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
 
    def setProgressVal(self, val):
        self.progressbar.setValue(val)
#End of Progress bar for hornet update
###############################################################################

###############################################################################
#Progress bar for hornet install
class Window_hornet_install(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2B3440; color: black;') #rgb(255,255,255);
        self.title = "Hornet install"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        #self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}""QProgressBar::chunk {background:black}")
        #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightblue, stop: 1 lightblue); }")
        #self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        #self.startProgressBar(self)
        self.setLayout(vbox)
        self.show()

    #def startProgressBar():
        self.thread = MyThread_hornet_install()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
 
    def setProgressVal(self, val):
        self.progressbar.setValue(val)
#End of Progress bar for hornet install
###############################################################################

###############################################################################
#Progress bar for hornet uninstall
class Window_hornet_uninstall(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2B3440; color: black;') #rgb(255,255,255);
        self.title = "Hornet uninstall"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        #self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}""QProgressBar::chunk {background:black}")
        #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightblue, stop: 1 lightblue); }")
        #self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        #self.startProgressBar(self)
        self.setLayout(vbox)
        self.show()

    #def startProgressBar():
        self.thread = MyThread_hornet_uninstall()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
 
    def setProgressVal(self, val):
        self.progressbar.setValue(val)
#End of Progress bar for hornet uninstall
###############################################################################

###############################################################################
#Progress bar for nginx+certbot install
class Window_nginx_certbot_install(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2B3440; color: black;') #rgb(255,255,255);
        self.title = "Nginx + Certbot install"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        #self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}""QProgressBar::chunk {background:black}")
        #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightblue, stop: 1 lightblue); }")
        #self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        #self.startProgressBar(self)
        self.setLayout(vbox)
        self.show()
    #def startProgressBar():
        self.thread = MyThread_nginx_certbot_install()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
 
    def setProgressVal(self, val):
        self.progressbar.setValue(val)
#End of Progress bar for nginx+certbot install
###############################################################################

###############################################################################
#Progress bar for nginx+certbot uninstall
class Window_nginx_certbot_uninstall(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #2B3440; color: black;') #rgb(255,255,255);
        self.title = "Nginx + Certbot uninstall"
        self.top = 200
        self.left = 500
        self.width = 300
        self.height = 100
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        self.progressbar = QProgressBar()
        #self.progressbar.setOrientation(Qt.Vertical)
        self.progressbar.setMaximum(100)
        #self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey;border-radius:8px;padding:1px}""QProgressBar::chunk {background:black}")
        #qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 red, stop: 1 white);
        self.progressbar.setStyleSheet("QProgressBar::chunk {background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 lightblue, stop: 1 lightblue); }")
        #self.progressbar.setTextVisible(False)
        vbox.addWidget(self.progressbar)
        #self.startProgressBar(self)
        self.setLayout(vbox)
        self.show()

    #def startProgressBar():
        self.thread = MyThread_nginx_certbot_uninstall()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()
 
    def setProgressVal(self, val):
        self.progressbar.setValue(val)
#End of Progress bar for nginx+certbot uninstall
