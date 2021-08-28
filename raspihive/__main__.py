#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

###############################################################################
# libraries
import sys, time, os, requests, pwd, grp, stat, getpass, re, fileinput
from os import path
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QAction,
    qApp,
    QCheckBox
)
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
    QLabel
)

from PyQt5.QtGui import QIcon, QFont, QImage
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtWidgets import QCheckBox
from .progress_bars import (
    Window_os_update,
    Window_packages,
    HornetProgress,
    NGINXCertbot
)
from pathlib import Path

# from .helpers import __default_message__

__default_message__ = f'Your Platform is not supported. Please raise a request for your OS on the discord server, on `#help` channel.'

# test import for cpu and ram values etc.
# import psutil
###########################################################################
# Global variables
ICON_IMAGE_URL = "https://raw.githubusercontent.com/Raspihive/raspihiveWebsite/master/public/favicon.ico"

#####################################Start of Window frames################
class Window1(QMainWindow):
    def __init__(self):
        #Set window position and size
        super().__init__()
        self.left = 300
        self.top = 300
        self.width = 800
        self.height = 330
        #Window size
        self.setGeometry(self.left, self.top, self.width, self.height)
        #End of set window position and size

        #icon in the taskbar
        self.label = QLabel('Raspihive')

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.label)

        self.setLayout(self.vertical_layout)

        self.nam = QNetworkAccessManager()
        self.nam.finished.connect(self.set_window_icon_from_response)
        self.nam.get(QNetworkRequest(QUrl(ICON_IMAGE_URL)))

        # Progress Bar Clients
        self.hornet_progress = HornetProgress()
        self.nginx_certbot_progress = NGINXCertbot()

    def set_window_icon_from_response(self, http_response):
        pixmap = QPixmap()
        pixmap.loadFromData(http_response.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)
    #End of icon in the taskbar

        #Start Toolbar
        #Toolbar Icon 1
        Act = QAction(QIcon('/home/raspihive/toolbar_raspihive_icons/raspihive_icon1.jpg'),\
            'Raspihive', self)
        #Act.setShortcut('Ctrl+Q')
        Act.triggered.connect(self.button1) #qApp.quit
        self.toolbar = self.addToolBar('Raspihive')
        self.toolbar.addAction(Act)
        # Set icon size and spacing
        self.toolbar.setIconSize(QtCore.QSize(32, 32))
        self.toolbar.setStyleSheet("background-color: #2B3440; QToolButton{padding-left: 5px; padding-right: 5px; }");
        #End Toolbar Icon 1


        #Toolbar Icon 2
        Act = QAction(QIcon('/home/raspihive/toolbar_raspihive_icons/close_icon2.jpg'),\
            'Raspihive', self)
        #Act.setShortcut('Ctrl+Q')
        Act.triggered.connect(qApp.quit) #qApp.quit
        self.toolbar = self.addToolBar('Close Raspihive')
        self.toolbar.addAction(Act)
        # Set icon size and spacing
        self.toolbar.setIconSize(QtCore.QSize(32, 32))
        self.toolbar.setStyleSheet("background-color: #2B3440; QToolButton{padding-left: 5px; padding-right: 5px; }");
        #End Toolbar Icon 2


        """
        #Toolbar Icon 3
        Act = QAction(QIcon('toolbar_raspihive_icons/raspihive_icon1.png'), 'Close Raspihive', self)
        Act.setShortcut('Ctrl+Q')
        Act.triggered.connect(qApp.quit) #qApp.quit
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(Act)
        # Set icon size and spacing
        self.toolbar.setIconSize(QtCore.QSize(32, 32))
        self.toolbar.setStyleSheet("QToolButton{padding-left: 5px; padding-right: 5px; }");
        #End Toolbar Icon
        """

        #self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Raspihive')
        #End Toolbar

        """ for further tests
        # set the size of window
        self.Width = 730
        self.height = int(0.600 * self.Width)
        self.resize(self.Width, self.height)
		"""

        # set the title of main window
        self.setWindowTitle(' Raspihive ')

        # add button 1 widget
        self.btn_1 = QPushButton('Update menu', self)
        #Setting background color or transparency
        self.btn_1.setStyleSheet('background-color: #2B3440; color: white')
        #add action
        self.btn_1.clicked.connect(self.button1)
        # add tab
        self.tab1 = self.ui1()
        #End of button 1 widget

        # add button 2 widget
        self.btn_2 = QPushButton(' Install menu ', self)
        #Setting background color or transparency
        self.btn_2.setStyleSheet('background-color: #2B3440; \
        color: white')
        #add action
        self.btn_2.clicked.connect(self.button2)
        # add tab
        self.tab2 = self.ui2()
        #End of button 2 widget

        # add button 3 widget
        self.btn_3 = QPushButton(' Node Control ', self)
        #Setting background color or transparency
        self.btn_3.setStyleSheet('background-color: #2B3440; color: white')
        #add action
        self.btn_3.clicked.connect(self.button3)
        # add tab
        self.tab3 = self.ui3()
        #End of button 3 widget

        #Invisible add button 4 widget
        self.btn_4 = QPushButton('Window 4', self)
        #Setting background color or transparency
        self.btn_4.setStyleSheet('background-color: #2B3440; color: white')
        #add action
        self.btn_4.clicked.connect(self.button4)
        # add tab
        self.tab4 = self.ui4()
        #End of invisible button 4 widget

        # add button 5 widget (Dashboard access)
        self.btn_5 = QPushButton(' Dashboard access ', self)
        #Setting background color or transparency
        self.btn_5.setStyleSheet('background-color: #2B3440; color: white')
        #add action
        self.btn_5.clicked.connect(self.button5)
        # add tab
        self.tab5 = self.ui5()
        #End of button 5 widget (Dashboard access)



        # add button 6 widget (Help)
        self.btn_6 = QPushButton(' Help ', self)
        #Setting background color or transparency
        self.btn_6.setStyleSheet('background-color: #2B3440; color: white')
        #add action
        self.btn_6.clicked.connect(self.button6)
        # add tab
        self.tab6 = self.ui6()
        #End of button 6 widget (Help)

        # add button 7 - Quit
        self.btn_7 = QPushButton(' Quit-Raspihive ', self)
        #Setting background color or transparency
        self.btn_7.setStyleSheet('background-color: #2B3440; color: white')
        #add action
        self.btn_7.clicked.connect(qApp.quit)
        # add tab
        self.tab7 = self.ui7()
        #End of button 7 - Quit

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1) #Update menu
        left_layout.addWidget(self.btn_2) # Install menu
        left_layout.addWidget(self.btn_3) # Node control
        #left_layout.addWidget(self.btn_4) Invisible window 4
        left_layout.addWidget(self.btn_5) #(Dashboard access)
        left_layout.addWidget(self.btn_6) #(Help)
        left_layout.addWidget(self.btn_7) #(Quit)


        #Add Status Bar
        self.statusBar().showMessage('Raspihive Version 2.3')
        #self.statusBar().setStyleSheet("background-image: url(assets/Logo/TheHive.png);")

        #End of status bar

        left_layout.addStretch(5)
        left_layout.setSpacing(30)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')
        self.right_widget.addTab(self.tab6, '')
        self.right_widget.addTab(self.tab7, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 5; padding: 0; border: none;}''')

        #Transparency
        self.setWindowOpacity(0.9875)
        #Background color Sidebar, Toolbar, widget windows
        self.setStyleSheet('background-color: #2B3440; color: white;')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 60)
        main_layout.setStretch(1, 280)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # -----------------
    # buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def button4(self):
        self.right_widget.setCurrentIndex(3)

    def button5(self):
        self.right_widget.setCurrentIndex(4)

    def button6(self):
        self.right_widget.setCurrentIndex(5)

    def button7(self):
        self.right_widget.setCurrentIndex(6)

    # End buttons

	# -----------------
    ####################### Start pages ##############

    # Update menu tab
    def ui1(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); #137394 this
        #Background Image + button image

        # creating the check-box
        checkbox = QCheckBox('Status Auto update', main)
        # setting geometry of check box
        checkbox.setGeometry(20, 220, 170, 50)


        if path.exists("/etc/crontab") == True:
            with open('/etc/crontab') as f:
                datafile = f.readlines()
            found = False  # This isn't really necessary
            for line in datafile:
                if "update.sh" in line:
                    #print("success")
                    # adding background color to indicator
                    checkbox.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "background-color : lightgreen;"
                               "}")
                else:
                    checkbox.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "background-color : red;"
                               "}")


        #Start button 1
        button = QPushButton(' Enable auto updates ', main)
        #Hover text
        button.setToolTip(' Enable automatic updates ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.enable_automatic_updates)
        #End button 1

        #Start button 2
        button = QPushButton(' Disable auto updates ', main)
        #Hover text
        button.setToolTip(' Disable automatic updates ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.disable_automatic_updates)
        #End button 2

        #Start button 3
        button = QPushButton('Update OS', main)
        #Hover text
        button.setToolTip('Update operating system')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.system_update)
        #End button 3


        #Start button 4
        button = QPushButton('Update packages', main)
        #Hover text
        button.setToolTip('Update necessary packages')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.packages_update)
        #End button 4

        #Start button 5
        button = QPushButton('Update Raspihive', main)
        #Hover text
        button.setToolTip('Update Raspihive')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(420, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.raspihive_update)
        #End button 5

        #Start button 6
        button = QPushButton('Update Hornet-Node', main)
        #Hover text
        button.setToolTip('Update Hornet-Node')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(420, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_update)
        #End button 6


        #Create label
        main.labelA = QtWidgets.QLabel(main)
        #Set label text
        main.labelA.setText(' Update menu ') #Raspihive menu
        #Set label text color
        main.labelA.setStyleSheet("color: white;")
        # setting font and size
        main.labelA.setFont(QFont('Arial', 16))
        # setting up background and text color

        #Setting position x y
        main.labelA.move(40, 10)
        #Setting label width
        main.labelA.setFixedWidth(180)
        #End label

        return main
    # End of update menu tab

    # Install menu
    def ui2(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); ##137394
        #Background Image + button image

        #Start button 1
        button = QPushButton(' Install Hornet ', main)
        #Hover text
        button.setToolTip(' Install IOTA Hornet Fullnode ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_install)
        #End button 1

        #Start button 2
        button = QPushButton(' Uninstall Hornet ', main)
        #Hover text
        button.setToolTip(' Uninstall IOTA Hornet Fullnode ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_uninstall)
        #End button 2

        #Start button 3
        button = QPushButton(' Install Nginx + Certbot ', main)
        #Hover text
        button.setToolTip(' Install Nginx-Server as a reverse Proxy + \
            Certbot for SSL Certificates ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.install_nginx_certbot)
        #End button 3

        #Start button 4
        button = QPushButton(' Start certbot process ', main)
        #Hover text
        button.setToolTip(' Enter the following command after the \
        installation of nginx+certbot into the terminal: \n "sudo \
certbot --nginx" (Domain needed) ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.certbot)
        #End button 4

        #Start button 5
        button = QPushButton(' Uninstall Nginx + Certbot ', main)
        #Hover text
        button.setToolTip(' Uninstall Nginx-Server as a reverse Proxy + \
        Certbot for SSL Certificates ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 210, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.uninstall_nginx_certbot)
        #End button 5

         # creating the check-box
        checkbox = QCheckBox('Status automatic \ncertificate renewal', main)
        # setting geometry of check box
        checkbox.setGeometry(440, 220, 170, 50)

        if path.exists("/var/spool/cron/crontabs/pi") == True:
            with open('/var/spool/cron/crontabs/pi') as f:
                datafile = f.readlines()
            found = False  # This isn't really necessary
            for line in datafile:
                if "renew" in line:
                    # adding background color to indicator
                    checkbox.setStyleSheet("QCheckBox::indicator"
                           "{"
                           "background-color : lightgreen;"
                           "}")
                else:
                    checkbox.setStyleSheet("QCheckBox::indicator"
                           "{"
                           "background-color : red;"
                           "}")


        #Start button 6
        button = QPushButton('Enable auto renewing \n SSL certificate', main)
        #Hover text
        button.setToolTip('Auto renewing SSL cert')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(420, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.enable_auto_renew_ssl)
        #End button 6

        #Start button 7
        button = QPushButton(' Disable auto renewal \nSSL certificate ', main)
        #Hover text
        button.setToolTip(' Automatic certificate renewal ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(420, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.disable_auto_renew_ssl)
        #End button 7

        #Create label
        main.labelA = QtWidgets.QLabel(main)
        #Set label text
        main.labelA.setText(' Install menu ') #Raspihive menu
        #Set label text color
        main.labelA.setStyleSheet("color: white;")
        # setting font and size
        main.labelA.setFont(QFont('Arial', 16))
        # setting up background and text color

        #Setting position x y
        main.labelA.move(40, 10)
        #Setting label width
        main.labelA.setFixedWidth(180)
        #End label

        return main
    # End of install menu

    # Node Control Center
    def ui3(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); ##137394
        #Background Image + button image


        #Start button 1
        button = QPushButton(' Hornet Control Center ', main)
        #Hover text
        button.setToolTip(' Hornet Control Center (settings) ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(40, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.button4)
        #End button 1

        """
        #Start button 2
        button = QPushButton('Update packages', main)
        #Hover text
        button.setToolTip('Update necessary packages')
        #button.move(150 ,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 10, 150, 50)
        #Setting background color or transparency
        button.setStyleSheet('background-color: #2B3440; color: white')
        #Background image for button
        #add action
        button.clicked.connect(self.packages_update)
        #End button 2
        """

        #Create label
        main.labelA = QtWidgets.QLabel(main)
        #Set label text
        main.labelA.setText('Node Control') #Raspihive menu
        #Set label text color
        main.labelA.setStyleSheet("color: white;")
        # setting font and size
        main.labelA.setFont(QFont('Arial', 16))
        # setting up background and text color

        #Setting position x y
        main.labelA.move(40, 10)
        #Setting label width
        main.labelA.setFixedWidth(180)
        #End label

        return main
    # End of Node Control Center

    # Invisible Hornet Node Control Center
    def ui4(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); ##137394
        #Background Image + button image


        #Start button 1
        button = QPushButton(' Start Hornet ', main)
        #Hover text
        button.setToolTip(' Start Hornet Node ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.start_hornet)
        #End button 1

        #Start button 2
        button = QPushButton(' Stop Hornet ', main)
        #Hover text
        button.setToolTip(' Stop Hornet Node ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.stop_hornet)
        #End button 2

        #Start button 3
        button = QPushButton(' Restart Hornet ', main)
        #Hover text
        button.setToolTip('Restart Hornet Node')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 210, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.restart_hornet)
        #End button 3

        #Start button 4
        button = QPushButton(' Status Hornet ', main)
        #Hover text
        button.setToolTip(' Status Hornet Node ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.status_hornet)
        #End button 4

        #Start button 5
        button = QPushButton(' Show Hornet Logs ', main)
        #Hover text
        button.setToolTip(' Show Hornet Logs ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_log_window)
        #End button 5

        #Start button 6
        button = QPushButton(' Remove the mainnetdb ', main)
        #Hover text
        button.setToolTip('Remove the mainnetdb (e.g. in case of a failure) ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(420, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.mainnetDB_hornet)
        #End button 6

        #Create label
        main.labelA = QtWidgets.QLabel(main)
        #Set label text
        main.labelA.setText(' Hornet Node Control ') #Raspihive menu
        #Set label text color
        main.labelA.setStyleSheet("color: white;")
        # setting font and size
        main.labelA.setFont(QFont('Arial', 16))
        # setting up background and text color

        #Setting position x y
        main.labelA.move(40, 10)
        #Setting label width
        main.labelA.setFixedWidth(200)
        #End label

        return main
    # End of invisible Hornet Node Control Center

    # Dashboard access
    def ui5(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); ##137394
        #Background Image + button image

        #Start button 1
        button = QPushButton(' Set or change username', main)
        #Hover text
        button.setToolTip(' Set or change username')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(40, 50, 220, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_dashboard_username)
        #End button 1

        #Start button 2
        button = QPushButton(' Set password', main)
        #Hover text
        button.setToolTip(' Set password')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(40, 130, 220, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_dashboard_password)
        #End button 2

        #Start button 3
        button = QPushButton(' Hornet Dashboard ', main)
        #Hover text
        button.setToolTip(' Open Hornet Dashboard ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(280, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_dashboard_access)
        #End button 3

        #Create label
        main.labelA = QtWidgets.QLabel(main)
        #Set label text
        main.labelA.setText(' Dashboard access ') #Raspihive menu
        #Set label text color
        main.labelA.setStyleSheet("color: white;")
        # setting font and size
        main.labelA.setFont(QFont('Arial', 16))
        # setting up background and text color

        #Setting position x y
        main.labelA.move(40, 10)
        #Setting label width
        main.labelA.setFixedWidth(180)
        #End label

        return main
    # End of Dashboard access

    # Help menu
    def ui6(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); ##137394 background-image: url(assets/Logo/TheHive.png
        #Background Image + button image


        #Start button 1
        button = QPushButton(' About ', main)
        #Hover text
        button.setToolTip(' About Raspihive ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.about)
        #End button 1

        #Start button 2
        button = QPushButton(' Prepartions ', main)
        #Hover text
        button.setToolTip(' Preparations - Port forwarding etc. ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.preparations)
        #End button 2

        #Start button 3
        button = QPushButton(' Report ', main)
        #Hover text
        button.setToolTip(' Report or Feedback ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(420, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.report)
        #End button 3

        """
        #Start button 2
        button = QPushButton(' Uninstall Hornet ', main)
        #Hover text
        button.setToolTip(' Uninstall IOTA Hornet Fullnode ')
        #button.move(150 ,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 50, 150, 50)
        #Setting background color or transparency
        button.setStyleSheet('background-color: #2B3440; color: white')
        #Background image for button
        #add action
        button.clicked.connect(self.hornet_uninstall)
        #End button 2
        """

        #Create label
        main.labelA = QtWidgets.QLabel(main)
        #Set label text
        main.labelA.setText(' Help ') #Raspihive menu
        #Set label text color
        main.labelA.setStyleSheet("color: white;")
        # setting font and size
        main.labelA.setFont(QFont('Arial', 16))
        # setting up background and text color

        #Setting position x y
        main.labelA.move(40, 10)
        #Setting label width
        main.labelA.setFixedWidth(180)
        #End label

        return main
    # End of Help menu

    # Quit button
    def ui7(self):
        main = QWidget()

        return main
    # End of Quit-button

    # End pages
    ##############################################################################

    ##############################################################################
    # Start Functions
    def system_update(self):
        app = Window_os_update()
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: \
        rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
        msg.setIcon(QMessageBox.Information)
        msg.setText("OS Update")
        msg.setInformativeText("OS update is running")
        msg.setWindowTitle("OS Update")
        msg.setDetailedText("Just close the window\
            if the progress bar reaches 100 %, #IOTAstrong")
        show = msg.exec_()  # this will show our messagebox

    def packages_update(self):
        app = Window_packages()
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: \
        rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
        msg.setIcon(QMessageBox.Information)
        msg.setText("Packages Update")
        msg.setInformativeText("Packages update is running")
        msg.setWindowTitle("Packages Update")
        msg.setDetailedText("Just close the window\
            if the progress bar reaches 100 %, #IOTAstrong")
        show = msg.exec_()  # this will show our messagebox

    # IMPORATANT: Raspihive needs to be cloned into the "/home"-folder, then restart is necessary.
    def raspihive_update(self):
        #print("Test packages")
        #os.chdir('/tmp')
        #os.system(" cd /tmp && sudo find -name raspihive -exec rm -rf {} +")
        #if path.exists("/home/pi/raspihive") == True:
        print("Update Raspihive")
        #process = subprocess.Popen(os_parse("sudo chown pi:pi -R /home/pi/raspihive "), stdout=subprocess.PIPE, shell = True)
        #os.system("sudo find -name raspihive -exec rm -rf {} +")
        #shutil.rmtree('/home/pi/raspihive')
        p=subprocess.Popen("cd /home && sudo rm -r raspihive && \
        sudo git clone https://github.com/Raspihive/raspihive.git /home/raspihive", stdout=subprocess.PIPE, shell = True)
        #else:
        #print("ELSE-TEST")
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Raspihive", "Raspihive updated. Please close and start Raspihive again, \
            that changes take effect")

    def hornet_update(self):
        self.hornet_progress.update()
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: \
        rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
        msg.setIcon(QMessageBox.Information)
        msg.setText("Hornet Update")
        msg.setInformativeText("Hornet update is running")
        msg.setWindowTitle("Hornet Update")
        msg.setDetailedText("Just close the window\
            if the progress bar reaches 100 %, #IOTAstrong")
        show = msg.exec_()  # this will show our messagebox

    def hornet_install(self):
        if path.exists("/var/lib/hornet/") == True:
            print("Hornet Node is already installed. Please uninstall it first")
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Install Nginx + Certbot")
            msg.setText("Hornet Node is already installed. Please uninstall it first")
            #msg.setInformativeText("informative text, ya!")
            x = msg.exec_()  # this will show our messagebox
        elif path.exists("/var/lib/hornet") == False:
            if self.hornet_progress.install():
                msg = QMessageBox()
                msg.setStyleSheet("background-color: #2B3440 ; color: \
                rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
                msg.setIcon(QMessageBox.Information)
                msg.setText("Install Hornet")
                msg.setInformativeText("Installation of Hornet is running")
                msg.setWindowTitle("Install Hornet")
                msg.setDetailedText("Just close the window\
                    if the progress bar reaches 100 %, #IOTAstrong")
                show = msg.exec_()  # this will show our messagebox
            else:
                self.not_supported()

    def hornet_uninstall(self):
        if path.exists("/var/lib/hornet/") == True:
            self.hornet_progress.uninstall()
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: \
            rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
            msg.setIcon(QMessageBox.Information)
            msg.setText("Uninstall Hornet")
            msg.setInformativeText("Uninstallation of Hornet is running")
            msg.setWindowTitle("Uninstall Hornet")
            msg.setDetailedText("Just close the window\
                if the progress bar reaches 100 %, #IOTAstrong")
            show = msg.exec_()  # this will show our messagebox
        elif path.exists("/var/lib/hornet") == False:
            print("Hornet Node is not installed. Please install it first")
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Install Nginx + Certbot")
            msg.setText("Hornet Node is not installed. Please install it first")
            #msg.setInformativeText("informative text, ya!")
            x = msg.exec_()  # this will show our messagebox

    def install_nginx_certbot(self):
        if path.exists("/etc/nginx/") == True:
            print("Nginx + Certbot is already installed. Please uninstall it first")
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Install Nginx + Certbot")
            msg.setText("Nginx + Certbot is already installed. Please uninstall it first")
            #msg.setInformativeText("informative text, ya!")
            x = msg.exec_()  # this will show our messagebox
        elif path.exists("/etc/nginx/") == False:
            self.nginx_certbot_progress.install()
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: \
            rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
            msg.setIcon(QMessageBox.Information)
            msg.setText("Install Nginx + Certbot")
            msg.setInformativeText("Install Nginx + Certbot is running")
            msg.setWindowTitle("Install Nginx + Certbot")
            msg.setDetailedText("Just close the window\
                if the progress bar reaches 100 %, #IOTAstrong")
            show = msg.exec_()  # this will show our messagebox

        # Nginx configuration
        if path.exists("/etc/nginx/sites-available/") == True:
            os.system("sudo chown $USER:$GROUPS -R /etc/nginx/")
            #os.chown("/etc/nginx/sites-available/default", 100, -1)
            try: # temporarily fix that raspihive does not crash after function call
                f = open("/etc/nginx/sites-available/default", "w")
                f.write("server { \n listen 80 default_server; \
                \n listen [::]:80 default_server; \n server_tokens off;  \
                \n server_name _; \n location /node { \
                \n proxy_pass http://127.0.0.1:14265/; \n } \
                \n \n location /ws {   \n proxy_pass http://127.0.0.1:8081/ws; \
                \n proxy_http_version 1.1; \n proxy_set_header Upgrade $http_upgrade; \
                \n proxy_set_header Connection "'"upgrade"'"; \
                \n proxy_read_timeout 86400; \n } \n \n location / { \
                \n proxy_pass http://127.0.0.1:8081; \n   } \n } \n")
                f.close()
                os.system('sudo systemctl start nginx && sudo systemctl enable nginx')
            except: # occurs because of permission denied error
                print("An exception occurred - Config not written - FAILURE")
        else:
            print("Config not written - FAILURE")
        """
        #Open LX Terminal (Raspberry Pi OS)
        cmd = "lxterminal "
        subprocess.check_output(cmd, shell=True)
        #Open Gnome-Terminal (Ubuntu)
        cmd = "gnome-terminal "
        subprocess.check_output(cmd, shell=True)
        #print("I'm done!")
        print(cmd)
        """

        #os.system(('sudo certbot --nginx'))
        #QMessageBox.about(self, "Certbot", "Certbot")

    def certbot(self):
        os.system("lxterminal") #just opens the terminal
        os.system("gnome-terminal") #just opens the terminal

    def uninstall_nginx_certbot(self):
        if path.exists("/etc/nginx/") == True:
            self.nginx_certbot_progress.uninstall()
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: \
            rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
            msg.setIcon(QMessageBox.Information)
            msg.setText("Uninstall Nginx + Certbot")
            msg.setInformativeText("Uninstall Nginx + Certbot is running")
            msg.setWindowTitle("Uninstall Nginx + Certbot")
            msg.setDetailedText("Just close the window\
                if the progress bar reaches 100 %, #IOTAstrong")
            show = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Install Nginx + Certbot")
            msg.setText("Nginx + Certbot is not installed. Please install it first")
            #msg.setInformativeText("informative text, ya!")
            x = msg.exec_()  # this will show our messagebox
            print("Nginx + Certbot is not installed. Please install it first")

    def enable_automatic_updates(self):

        os.system("pkexec chown $USER:$GROUPS -R /etc/crontab && sudo chown $USER:$GROUPS -R /home/")
        f = open("/home/update.sh", "w") #
        f.write("apt update && apt full-upgrade -y")
        f.close()
        os.chmod('/home/update.sh', stat.S_IEXEC)
        process = subprocess.Popen((' echo "0 20 * * * root /home/update.sh >> /var/log/update_raspihive.log" | tee -a /etc/crontab'), stdout=subprocess.PIPE, shell = True)
        os.system("sudo chown root:root -R /etc/crontab")
        QMessageBox.about(self, "Automatic update", "Automatic updates enabled\nPlease restart Raspihive that changes take effect")

    def disable_automatic_updates(self):
        os.system("pkexec rm -r /home/update.sh ")
        os.system("sudo chown $USER:$GROUPS -R /etc/crontab")
        #p=subprocess.Popen("crontab -e", stdout=subprocess.PIPE, shell = True)
        filename = '/etc/crontab'
        line_to_delete = 23
        line_to_delete2 = 24
        initial_line = 1
        file_lines = {}

        with open(filename) as f:
            content = f.readlines()

        for line in content:
            file_lines[initial_line] = line.strip()
            initial_line += 1

        f = open(filename, "w")
        for line_number, line_content in file_lines.items():
            if ((line_number != line_to_delete) and (line_number != line_to_delete2)):
                f.write('{}\n'.format(line_content))

        f.close()
        os.system("sudo chown root:root -R /etc/crontab")
        #print('Deleted line: {}'.format(line_to_delete))
        #print('Deleted line: {}'.format(line_to_delete2))

        #process = subprocess.Popen((' echo "50 19 * * 3 root /usr/bin/apt update -q -y >> /var/log/apt/automaticupdates.log" | tee -a /etc/crontab'), stdout=subprocess.PIPE, shell = True)

        #f = open("crontab -e", "w") #
        #f.write("0 12 * * * /usr/bin/certbot renew --quiet") #test - quiet
        #f.close()
        QMessageBox.about(self, "Automatic update", "Automatic updates disabled\nPlease restart Raspihive that changes take effect")

    def enable_auto_renew_ssl(self):
        os.system("pkexec chown $USER:$GROUPS -R /var/spool/cron/crontabs/")
        #p=subprocess.Popen("crontab -e", stdout=subprocess.PIPE, shell = True)
        process = subprocess.Popen((' echo "0 12 * * * /usr/bin/certbot renew --quiet" | tee -a /var/spool/cron/crontabs/pi'), stdout=subprocess.PIPE, shell = True)
        #f = open("crontab -e", "w") #
        #f.write("0 12 * * * /usr/bin/certbot renew --quiet") #test - quiet
        #f.close()
        os.system("sudo chown root:root -R /var/spool/cron/crontabs/pi")
        QMessageBox.about(self, "SSL-certificate", "Auto renewing enabled\nPlease restart Raspihive that changes take effect")

    def disable_auto_renew_ssl(self):
        #os.system("pkexec chown $USER:$GROUPS -R /var/spool/cron/crontabs/pi")
        subprocess.Popen("crontab -r", stdout=subprocess.PIPE, shell = True)
        QMessageBox.about(self, "Automatic update", "Auto renewing disabled\nPlease restart Raspihive that changes take effect")

    def start_hornet(self):
        p=subprocess.Popen("pkexec service hornet start", stdout=subprocess.PIPE, shell = True)
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Hornet", "Hornet node started")

    def stop_hornet(self):
        p=subprocess.Popen("pkexec service hornet stop", stdout=subprocess.PIPE, shell = True)
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Hornet", "Hornet node stopped")

    def restart_hornet(self):
        p=subprocess.Popen("pkexec service hornet restart", stdout=subprocess.PIPE, shell = True)
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Hornet", "Hornet node restarted")

    def status_hornet(self):
        self.cams = hornet_status_win()
        self.cams.show()
        #self.close()

    def hornet_log_window(self): # Test
        self.cams = hornet_log_win()
        self.cams.show()
        #self.close()

    def mainnetDB_hornet(self):
        p=subprocess.Popen("pkexec service hornet stop && \
            sudo rm -r /var/lib/hornet/mainnetdb && sudo rm -r /var/lib/hornet/snapshots &&\
            sudo service hornet start", stdout=subprocess.PIPE, shell = True)
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Hornet", "Hornet DB successfully deleted")

    def hornet_dashboard_access(self):
        if path.exists("/etc/letsencrypt/live") == True:
            subprocess.Popen("sudo -upi chromium http://127.0.0.1",shell = True)
            subprocess.Popen("sudo -upi firefox http://127.0.0.1",shell = True)
            #os.system('sudo -upi chromium http://localhost')
            subprocess.Popen("sudo -uubuntu firefox http://127.0.0.1",shell = True)
            #os.system('sudo -uubuntu firefox http://localhost')
            subprocess.Popen("sudo -ubeekeeper firefox http://127.0.0.1",shell = True)
            #os.system('sudo -ubeekeeper firefox http://localhost')
        else:
            subprocess.Popen("sudo -upi chromium http://localhost:8081",shell = True)
            subprocess.Popen("sudo -upi firefox http://localhost:8081",shell = True)
            #os.system('sudo -upi chromium http://localhost')
            subprocess.Popen("sudo -uubuntu firefox http://localhost:8081",shell = True)
            #os.system('sudo -uubuntu firefox http://localhost')
            subprocess.Popen("sudo -ubeekeeper firefox http://localhost:8081",shell = True)
            #os.system('sudo -ubeekeeper firefox http://localhost')

    def hornet_dashboard_username(self):
        # Define search string/pattern
        string1 = "admin"
        string2 = "admin"

        try:
            # opening and reading the text file
            file1 = open("/var/lib/hornet/config.json", "r")  #/var/lib/hornet/config.json
            readfile = file1.read()

            # checking condition for string found or not
            if string1 in readfile:
                #Get permission for config.json
                os.system("pkexec chown $USER:$GROUPS /var/lib/hornet/config.json")             #/var/lib/hornet/config.json

                text1 , pressed = QInputDialog.getText(self, "Input Text", "Set username: ", QLineEdit.Normal, "")
                path = Path("/var/lib/hornet/config.json")      #/var/lib/hornet/config.json
                print('String', string1, 'Found In File')
                text = path.read_text()
                text = text.replace("admin", text1) #text to search / replacement text #replace of user admin
                path.write_text(text)
            elif string2 not in readfile: #does not work right atm
                old =  oldusername , pressed = QInputDialog.getText(self, "Input old username", "Enter old username first: ", QLineEdit.Normal, "")
                new =  newusername , pressed = QInputDialog.getText(self, "Input new username", "Enter new username: ", QLineEdit.Normal, "")

                if old[1]:   #this is because: QInputDialog.gettext() returns a tuple: first value is the text in the inputfield (QLineEdit), the second is bool, True if 'OK' is pressed else False
                    old1 = old[0]
                    new1 = new[0]
                    print("OLD", new1)
                    path = Path("/var/lib/hornet/config.json")
                    text = path.read_text()
                    text = text.replace(old1, new1) #text to search / replacement text #replace of user admin
                    path.write_text(text)
                #file1 = open("test.txt", "a+")
                #file1.write("username" + text1);
                    print("current username replaced")
                else:
                    print('String', string1 , 'Not Found')
            # closing a file
            file1.close()
            os.system("sudo chown hornet:hornet /var/lib/hornet/config.json")
        except OSError as ose:
            print('os err:', ose)
            print('Hornet Not Installed. Please Install Hornet First.')
        except Exception as e:
            print("Other Exception:", e)

    def hornet_dashboard_password(self):
        print("Test")
        try:
            #cmd1 = 'cd /var/lib/hornet && hornet tool pwdhash'
            #os.system(cmd1)
            #subprocess.Popen("cd /var/lib/hornet && hornet tool pwdhash",shell = True)

            #print("Output", password)
            # password1 , pressed = QInputDialog.getText(self, "Set password", "Set password: ", QLineEdit.Normal, "")
            #
            # def my_function(password1):
            #     print(password1 + " IOTA")
            #
            # my_function(password1)

            password1 , pressed = QInputDialog.getText(self, "Set password", "Set password: ", QLineEdit.Normal, "")
            password2 , pressed = QInputDialog.getText(self, "Retype password", "Retype password: ", QLineEdit.Normal, "")

            os.popen('cat /etc/services').read()
            output = subprocess.check_output("cat /etc/services", shell=True)
            value = input("Please enter a string:\n")
            print(f'You entered {password}')
            cmd1 = 'cd /var/lib/hornet && hornet tool pwdhash'
            os.system(cmd1)

            """ GUI stuff

            text1 , pressed = QInputDialog.getText(self, "Input Text", "Set password: ", QLineEdit.Normal, "")
            print("Output: ", text1)

            #show window
            window = QWidget()
            window.setGeometry(400,400,250,250)
            window.setWindowTitle("Raspihive")

            label = QLabel(window)
            label.setText("Password")
            label.move(60,80)

            button = QPushButton(window)
            button.setText("Set password")
            button.clicked.connect(self.hornet_dashboard_user_and_pw)
            button.move(60,120)

            window.show()
            #os.system("hornet tool pwdhash  /var/lib/hornet" )
            """
        except Exception as ex:
            print('ex:', ex)

    def about(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("About")
        msg.setText("The Plug and Play solution for a Raspberry Pi\n\
IOTA Fullnode!\n\n\
Raspihive: Version 2.3\n \n Special thanks to: \n Anistark \n Martin N \n Bernardo \n\n Thanks for testing and bug reporting to\n Olsche from www.easy-passphrase-saver.de")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox

    def preparations(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Preparations")
        msg.setText("The following ports are important for a flawless node\
operation. Allow the following basic ports in your router settings: \n \n 14626 UDP\
- Autopeering port \n \n 15600 TCP - Gossip (neighbors) port \n \n 80 TCP\
- for Certbot \n \n 443 TCP for Certbot")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox

    def report(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Report")
        msg.setText("If you found a bug or experience any issues, please write us \
as at: www.raspihive.org or get directly in touch by sending \
an e-mail to: piota@mail.de \nThanks for your feedback!")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox

    def not_supported(self, msg=__default_message__):
        print(msg)
        # TODO: Display msg in a pop up. Right now, below one is not working.
        # msg = QMessageBox()
        # msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
        # msg.setIcon(QMessageBox.Information)
        # msg.setWindowTitle("Un-Supported")
        # msg.setText(msg)
        # # msg.setInformativeText(msg)
        # x = msg.exec_()

# End Functions
###############################################################################

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
        Outputfileobject=os.popen("service hornet status")     #sudo service hornet status
        Output=Outputfileobject.read()
        Outputfileobject.close()

         #Create label
        labelT = QtWidgets.QLabel(self)
        #Set label text
        Text=labelT.setText(Output)
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

# End of Hornet Status

# Hornet Log
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
        Outputfileobject=os.popen("journalctl -u hornet -n 50")
        Output=Outputfileobject.read()
        Outputfileobject.close()

        #Create label
        labelT = QtWidgets.QLabel(self)
        #Set label text
        Text=labelT.setText(Output)
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

# End of Hornet Log


# Mainwindow
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
    window   = Window1()
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
# End of MainWindow

# Start main programm
###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
# End main programm
