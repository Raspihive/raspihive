#!/usr/bin/env python3
#!-*- coding: utf-8 -*-

###############################################################################
# libraries
import sys, time, os, requests, pwd, grp
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QAction,
    qApp
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
from .progress_bars import *
from .helpers import os_parse
###########################################################################
#Global variables
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

    def set_window_icon_from_response(self, http_response):
        pixmap = QPixmap()
        pixmap.loadFromData(http_response.readAll())
        icon = QIcon(pixmap)
        self.setWindowIcon(icon)
    #End of icon in the taskbar
    
        #Start Toolbar
        #Toolbar Icon 1
        Act = QAction(QIcon('toolbar_raspihive_icons/raspihive_icon1.jpg'),\
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
        Act = QAction(QIcon('toolbar_raspihive_icons/close_icon2.png'), 'Close Raspihive', self)
        Act.setShortcut('Ctrl+Q')
        Act.triggered.connect(qApp.quit) #qApp.quit
        self.toolbar = self.addToolBar('Exit')
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
        self.statusBar().showMessage('Raspihive Version 2.0')
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

#Update menu tab
    def ui1(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); #137394 this
        #Background Image + button image


        #Start button 1
        button = QPushButton('Update OS', main)
        #Hover text
        button.setToolTip('Update operating system')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(20, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.system_update)
        #End button 1

        #Start button 2
        #Hover text
        button.setGeometry(220, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.packages_update)
        #End button 2

        #Start button 3
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
        #End button 3

        #Start button 4
        button = QPushButton('Update Hornet', main)
        #Hover text
        button.setToolTip('Update Hornet')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 130, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_update)
        #End button 4

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
#End of update menu tab

#Install menu
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
        button.setGeometry(220, 50, 180, 60)
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
        button.setGeometry(20, 150, 180, 60)
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
        button.setGeometry(220, 150, 180, 60)
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
        button.setGeometry(420, 150, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.uninstall_nginx_certbot)
        #End button 5

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
#End of install menu

#Node Control Center
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
#End of Node Control Center

#Invisible Hornet Node Control Center
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
        button.setGeometry(220, 50, 180, 60)
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
        button.setGeometry(420, 50, 180, 60)
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
        button.setGeometry(20, 150, 180, 60)
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
        button.setGeometry(220, 150, 180, 60)
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
        button.setGeometry(420, 150, 180, 60)
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
#End of invisible Hornet Node Control Center

#Dashboard access
    def ui5(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); ##137394
        #Background Image + button image


        #Start button 1
        button = QPushButton(' Hornet Dashboard ', main)
        #Hover text
        button.setToolTip(' Open Hornet Dashboard ')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(40, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(self.hornet_dashboard_access)
        #End button 1

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
#End of Dashboard access

#Help menu
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
#End of Help menu

# Quit button
    def ui7(self):
        main = QWidget()

        return main
#End of Quit-button

#End pages
##############################################################################

##############################################################################
#Start Functions
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

    def raspihive_update(self):
        app = Window_raspihive_update()
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: \
        rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
        msg.setIcon(QMessageBox.Information)
        msg.setText("Raspihive Update")
        msg.setInformativeText("Raspihive update is running")
        msg.setWindowTitle("Raspihive Update")
        msg.setDetailedText("Just close the window\
            if the progress bar reaches 100 %, #IOTAstrong")
        show = msg.exec_()  # this will show our messagebox

    def hornet_update(self):
        app = Window_hornet_update()
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
        app = Window_hornet_install()
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

    def hornet_uninstall(self):
        app = Window_hornet_uninstall()
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

    def install_nginx_certbot(self):
        app = Window_nginx_certbot_install()
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

    def certbot(self):
        os.system("lxterminal") #just opens the terminal
        os.system("gnome-terminal") #just opens the terminal

        # Nginx configuration
        if path.exists("/etc/nginx/sites-available/") == True:
            os.system("sudo chown pi:pi -R /etc/nginx/ ")
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
                \n proxy_pass http://127.0.0.1:8081; \n auth_basic “Dashboard”; \
                \n  auth_basic_user_file /etc/nginx/.htpasswd;  } \n } \n")
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

    def uninstall_nginx_certbot(self):
        app = Window_nginx_certbot_uninstall()
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
            sudo rm -r /var/lib/hornet/mainnetdb && \
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
        subprocess.Popen("sudo -upi chromium http://localhost",shell = True)
        subprocess.Popen("sudo -upi firefox http://localhost",shell = True)
        #os.system('sudo -upi chromium http://localhost')
        subprocess.Popen("sudo -uubuntu firefox http://localhost",shell = True)
        #os.system('sudo -uubuntu firefox http://localhost')
        subprocess.Popen("sudo -ubeekeeper firefox http://localhost",shell = True)
        #os.system('sudo -ubeekeeper firefox http://localhost')

    def about(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("About")
        msg.setText("The Plug and Play solution for a Raspberry Pi\n\
IOTA Fullnode!\n\n\
Raspihive: Version 2.0\n \n Special thanks to: \n Anistark \n Martin N \n Bernardo ")
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
a e-mail to: piota@mail.de \nThanks for your feedback!")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox

#End Functions
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

#End of Hornet Status

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

#End of Hornet Log

#Mainwindow
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
#End of MainWindow

# Start main programm
###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
#End main programm
