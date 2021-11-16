#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

###############################################################################
# libraries
import sys

from PyQt5 import Qt

#Modularizing code...#relative import
from .gui.gui_window1 import Window1
from .hornet.hornet_log_stat_windows.log_win import *
from .hornet.hornet_log_stat_windows.status_win import *
from .gui.progress_bars.progress_bars import *

#from .helpers import os_parse

#test import for cpu and ram values etc.
#import psutil
###########################################################################
#Global variables
ICON_IMAGE_URL = "https://raw.githubusercontent.com/Raspihive/raspihiveWebsite/\
    master/public/favicon.ico"

#Mainwindow
def main():
    # create pyqt5 app
    app = Qt.QApplication(sys.argv)

    screen = app.primaryScreen()
    #print('Screen: %s' % screen.name())
    screen.size()
    #print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    #print('Available: %d x %d' % (rect.width(), rect.height()))
    #print()
    #print("Width", rect.width())
    #print("Height", rect.height())

    # create the instance of our Window
    window = Window1()
    # show the window is disabled by default
    if rect.width()*rect.height() <= 614400: # 7 inch Display = Fullscreen
        window.showMaximized()
        print("Fullscreen mode")
    else:
        (rect.width()*rect.height() <= 2073600) # > 7 inch Display no Fullscreen
        print("No Fullscreen mode", rect.width())
        window.show()

    # start the app
    sys.exit(app.exec_())
#End of MainWindow

# Start main programm
###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
#End main programm
