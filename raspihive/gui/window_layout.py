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
from raspihive.progress_bars import *
from raspihive.helpers import os_parse
from raspihive.hornet.log_win import hornet_log_win
from raspihive.hornet.status_win import hornet_status_win
from raspihive.functions import functions

ICON_IMAGE_URL = "https://raw.githubusercontent.com/Raspihive/raspihiveWebsite/master/public/favicon.ico"

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

    # Pages
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
        button.clicked.connect(functions.system_update)
        #End button 1

        #Start button 2
        button = QPushButton('Update packages', main)
        #Hover text
        button.setToolTip('Update necessary packages')
        #button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(220, 50, 180, 60)
        #button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        #add action to the button
        button.clicked.connect(functions.packages_update)
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
        button.clicked.connect(functions.raspihive_update)
        QMessageBox.about(self, "Raspihive", "Raspihive updated. Please close and start Raspihive again, \
            that changes take effect")
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
        button.clicked.connect(functions.hornet_update)
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
        button.clicked.connect(functions.hornet_install)
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
        button.clicked.connect(functions.hornet_uninstall)
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
        button.clicked.connect(functions.install_nginx_certbot)
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
        button.clicked.connect(functions.certbot)
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
        button.clicked.connect(functions.uninstall_nginx_certbot)
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
        button.clicked.connect(functions.packages_update)
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
        button.clicked.connect(functions.start_hornet)
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
        button.clicked.connect(functions.stop_hornet)
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
        button.clicked.connect(functions.restart_hornet)
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
        button.clicked.connect(functions.mainnetDB_hornet)
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

    # Dashboard access
    def ui5(self):
        main = QWidget()
        main.setWindowOpacity(1.0)
        main.setStyleSheet('background-color:  #137394 ') #rgb(255,255,255); ##137394
        # Background Image + button image


        # Start button 1
        button = QPushButton(' Hornet Dashboard ', main)
        # Hover text
        button.setToolTip(' Open Hornet Dashboard ')
        # button.move(10,50)
        # setting geometry of button x, y, width, height
        button.setGeometry(40, 50, 180, 60)
        # button regular state
        button.setStyleSheet('QPushButton {background-color: #2e3031; color: white; }')
        # add action to the button
        button.clicked.connect(functions.hornet_dashboard_access)
        # End button 1

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
        button.clicked.connect(functions.hornet_uninstall)
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
        button.clicked.connect(functions.about)
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
        button.clicked.connect(functions.preparations)
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
        button.clicked.connect(functions.report)
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
        button.clicked.connect(functions.hornet_uninstall)
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

    def status_hornet():
        self.cams = hornet_status_win()
        self.cams.show()
        #self.close()

    def hornet_log_window(): # Test
        self.cams = hornet_log_win()
        self.cams.show()
        #self.close()
