#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

###############################################################################
# libraries
import sys, time, os, requests, pwd, grp
from PyQt5 import QtGui, QtWidgets, Qt, QtCore
from subprocess import Popen
from PyQt5.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QTabWidget,
    QHBoxLayout,
    QInputDialog,
    QLineEdit,
    QApplication,
    QWidget,
    QLabel,
    QApplication,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QAction,
    qApp
)

from PyQt5.QtGui import QIcon, QFont, QImage
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from .progress_bars import *
from .helpers import os_parse
from .gui.window_layout import Window1
###########################################################################
#Global variables
ICON_IMAGE_URL = "https://raw.githubusercontent.com/Raspihive/raspihiveWebsite/master/public/favicon.ico"
#####################################Start of Window frames################

def main():
    # create pyqt5 app
    app = Qt.QApplication(sys.argv)

    screen = app.primaryScreen()
    #print('Screen: %s' % screen.name())
    size = screen.size()
    #print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    #print('Available: %d x %d' % (rect.width(), rect.height()))
    #print()
    #print("Width", rect.width())
    #print("Height", rect.height())

    # create the instance of our Window
    window = Window1()
    # show the window is disabled by default
    if (rect.width()*rect.height()<=614400): # 7 inch Display = Fullscreen
        window.showMaximized()
        print("Fullscreen mode")
    else:
        (rect.width()*rect.height()<=2073600) # > 7 inch Display no Fullscreen
        print("No Fullscreen mode", rect.width())
        window.show()

    # start the app
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
