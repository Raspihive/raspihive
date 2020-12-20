#!/usr/bin/env python3
#!-*- coding: utf-8 -*-
#This Programm is made with love from the IOTA-Community for the IOTA-Community. 
#

###############################################################################
# libraries
import sys, time, os
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QProgressBar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt, QtWidgets, QtGui
from subprocess import Popen, PIPE
import subprocess

#from .helpers import os_parse
###############################################################################
# Check for root
#if not os.geteuid() == 0:
#    messagebox.showinfo("Raspberry Pi Authentication", "You need sudo privileges to start raspihive")
#    sys.exit("\n Only root can run this script \n")
###############################################################################
# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )

##############################################################################

#####################################Start of Window frames############################################

class MainWindow1(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.mainWindow1()

    def mainWindow1(self):
        #Window size
    
        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Raspihive')
        
        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Raspihive menu') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: #e5dede; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label
      
        # creating a push button Update menu
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(20, 60, 150, 40) 
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #353535; color : white;') #rgb(150,150,150)
        #Setting button text
        self.pushButton.setText('Update menu')
        # adding action to a button 
        self.pushButton.clicked.connect(self.Window2)
        # End of creating a push button Update menu


        # creating a push button Install menu
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(220, 60, 150, 40) 
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        #Setting button text
        self.pushButton.setText('Install menu')
        # adding action to a button 
        self.pushButton.clicked.connect(self.Window3)
        # End of creating a push button Install menu

        # creating a push button Node control
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(20, 120, 150, 40) 
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        #Setting button text
        self.pushButton.setText('Node control')
        # adding action to a button 
        self.pushButton.clicked.connect(self.Window4)
        # End of creating a push button Node control

        # creating a push button dashboard access
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(220, 120, 150, 40) 
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        #Setting button text
        self.pushButton.setText('dashboard access')
        # adding action to a button 
        self.pushButton.clicked.connect(self.Window6)
        # End of creating a push button dashboard access

        # creating a push button tools
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(20, 180, 150, 40) 
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        #Setting button text
        self.pushButton.setText('Tools')
        # adding action to a button 
        self.pushButton.clicked.connect(self.Window7)
        # End of creating a push button tools

        # creating a push button help
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(220, 180, 150, 40) 
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        #Setting button text
        self.pushButton.setText('Help')
        # adding action to a button 
        self.pushButton.clicked.connect(self.Window8)
        # End of creating a push button help

        # creating a quit button
        self.pushButton = Qt.QPushButton(self)
        # setting geometry of button x, y, width, height
        self.pushButton.setGeometry(220, 240, 150, 40) 
        #Setting background color or transparency
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        #Setting button text
        self.pushButton.setText('Quit Raspihive')
        # adding action to a button 
        self.pushButton.clicked.connect(self.close)
        # End of creating a quit button

        

        
    def Window2(self): # Update menu
        self.cams = MainWindow2()
        self.cams.show()
        self.close()
    
    def Window3(self): # Install menu
        self.cams = MainWindow3()
        self.cams.show()
        self.close()
    
    def Window4(self): # Node control
        self.cams = MainWindow4()
        self.cams.show()
        self.close()

    def Window6(self): # Dashboard access
        self.cams = MainWindow6()
        self.cams.show()
        self.close()

    def Window7(self): # Tools
        self.cams = MainWindow7()
        self.cams.show()
        self.close()

    def Window8(self): # Help
        self.cams = MainWindow8()
        self.cams.show()
        self.close()

    
    

class MainWindow2(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Update menu')

        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Update menu') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: white; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label

        #Button System-update
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')  #rgb(255,0,0)
        self.pushButton.setText('System-update')
        self.pushButton.clicked.connect(self.os_update)
        #End of button System-update

        #Button Packages-update
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Packages-update')
        self.pushButton.clicked.connect(self.packages_update)
        #End of button Packages-update

        #Button Hornet-update
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Hornet-update')
        self.pushButton.clicked.connect(self.hornet_update)
        #End of button Hornet-update

        #Button Raspihive-update
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Raspihive-update')
        self.pushButton.clicked.connect(self.raspihive_update)
        #End of button Raspihive-update

        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 200, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page

        #Start progress bar

        """
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.progressBar.setRange(0, 0)
        self.progressBar.setFixedSize(300, 30)
        self.progressBar.setTextVisible(True)
        """

        """
        self.MainWindow2 = Qt.QProgressBar()
        self.MainWindow2.setRange(0, 100)
        self.MainWindow2.setValue(50) #SETTINGS THIS TO 50 FOR EXAMPLE
        self.MainWindow2.show()
        """
        #End progress bar

    #Functions
    def os_update(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            #p=subprocess for progress bar needed...- Getting progress message from a subprocess
            p=subprocess.Popen("sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt clean -y && sudo apt autoclean -y", stdout=subprocess.PIPE, shell = True)
            #Getting progress message from a subprocess
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
                #End of Getting progress message from a subprocess
            QMessageBox.about(self, "OS Update", "OS successfully updated")

    def packages_update(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            p=subprocess.Popen("sudo apt update -y && sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic", stdout=subprocess.PIPE, shell = True)
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
            QMessageBox.about(self,  "Packages Update", "Packages successfully updated")

    def hornet_update(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            p=subprocess.Popen("sudo service hornet stop && sudo apt-get update && sudo apt-get -y upgrade hornet && sudo systemctl restart hornet", stdout=subprocess.PIPE, shell = True)
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
            QMessageBox.about(self,  "Hornet Update", "Hornet Node successfully updated")

    def raspihive_update(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            p=subprocess.Popen("cd /var/lib/ && sudo rm -r raspihive && sudo git clone https://github.com/Raspihive/raspihive.git /var/lib/raspihive", stdout=subprocess.PIPE, shell = True)
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
            QMessageBox.about(self,  "Raspihive Update", "Raspihive successfully updated")        

    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close()     

class MainWindow3(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Install Menu')

        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Install menu') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: white; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label

        #Button Install-hornet
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white') #rgb(255,0,0)
        self.pushButton.setText('Install Hornet')
        self.pushButton.clicked.connect(self.hornet_install)
        #End of button Install-hornet

        #Button Uninstall-hornet
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Uninstall Hornet')
        self.pushButton.clicked.connect(self.hornet_uninstall)
        #End of button Uninstall hornet

        #Button Install Nginx + Certbot
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Install Nginx + Certbot')
        self.pushButton.clicked.connect(self.install_nginx_certbot)
        #End of button Nginx + Certbot

        #Button Remove Nginx + Certbot
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Remove Nginx + Certbot')
        self.pushButton.clicked.connect(self.uninstall_nginx_certbot)
        #End of button Remove Nginx + Certbot


        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 200, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page


    def hornet_install(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            p=subprocess.Popen('sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic && sudo apt update && sudo apt -y upgrade && sudo wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add -  && sudo echo "deb http://ppa.hornet.zone stable main" >> /etc/apt/sources.list.d/hornet.list && sudo apt update && sudo apt install hornet && sudo systemctl enable hornet.service && sudo apt-get install -y ufw && sudo ufw allow 15600/tcp && sudo ufw allow 14626/udp && sudo ufw limit openssh && sudo ufw enable && sudo apt-get install sshguard -y && sudo service hornet start', stdout=subprocess.PIPE, shell = True)
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
            QMessageBox.about(self,  "Hornet install", "Hornet node successfully installed")  

    def hornet_uninstall(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            p=subprocess.Popen("sudo systemctl stop hornet && sudo apt -qq purge hornet -y && sudo rm -rf /etc/apt/sources.list.d/hornet.list", stdout=subprocess.PIPE, shell = True)
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
            QMessageBox.about(self, "Hornet install", "Hornet node successfully uninstalled")
          
    def install_nginx_certbot(self):
        os.system('sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get install -y nginx && sudo ufw allow "Nginx Full" && sudo apt-get install -y apache2-utils && sudo htpasswd -c /etc/nginx/.htpasswd Raspihive')
        # Nginx configuration
        f = open("/etc/nginx/sites-available/default", "w")
        f.write("server { \n listen 80 default_server; \n listen [::]:80 default_server; \n server_tokens off;  \n server_name _; \n location /node { \n proxy_pass http://127.0.0.1:14265/; \n } \n \n location /ws {   \n proxy_pass http://127.0.0.1:8081/ws; \n proxy_http_version 1.1; \n proxy_set_header Upgrade $http_upgrade; \n proxy_set_header Connection "'"upgrade"'"; \n proxy_read_timeout 86400; \n } \n \n location / { \n proxy_pass http://127.0.0.1:8081; \n auth_basic “Dashboard”; \n  auth_basic_user_file /etc/nginx/.htpasswd;  } \n } \n")
        f.close()
        os.system('sudo systemctl start nginx && sudo systemctl enable nginx')
        p=subprocess.Popen("sudo apt install software-properties-common -y && sudo apt update && sudo apt install certbot python3-certbot-nginx -y", stdout=subprocess.PIPE, shell = True)
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Nginx + Certbot install", "Nginx + Certbot successfully installed")

    def uninstall_nginx_certbot(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            p=subprocess.Popen("sudo systemctl stop nginx && sudo systemctl disable nginx && sudo apt -qq purge software-properties-common certbot python3-certbot-nginx -y && sudo apt-get purge -y nginx", stdout=subprocess.PIPE, shell = True)
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
            QMessageBox.about(self, "Nginx + Certbot install", "Nginx + Certbot successfully uninstalled")

    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close()        

class MainWindow4(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Node control')

        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Node control') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: white; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label

        #Button Hornet Node Control
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535 ; color: white')  #rgb(255,0,0)
        self.pushButton.setText('Hornet Node Control')
        self.pushButton.clicked.connect(self.Hornet_Node_Control)
        #End of button Hornet Node Control

        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535 ; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page

    def Hornet_Node_Control(self):
        self.cams = MainWindow5()
        self.cams.show()
        self.close()  

    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close()  

class MainWindow5(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Hornet Node Control Center')

        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Hornet Node Control Center') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: white; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label

        #Button Start Hornet
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535 ; color: white')  #rgb(255,0,0)
        self.pushButton.setText('Start Hornet')
        self.pushButton.clicked.connect(self.start_hornet)
        #End of button Start Hornet

        #Button Stop Hornet
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Stop Hornet')
        self.pushButton.clicked.connect(self.stop_hornet)
        #End of button Stop Hornet

        #Button Restart Hornet
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Restart hornet')
        self.pushButton.clicked.connect(self.restart_hornet)
        #End of button Restart Hornet

        #Button Check Hornet Status
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Check status')
        self.pushButton.clicked.connect(self.status_hornet)
        #End of button Check Hornet Status
        
        # creating a push button Hornet Log Window
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 200, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Watch the logs')
        self.pushButton.clicked.connect(self.hornet_log_window)
        # End of creating a push button Hornet Log Window

        #Button Remove the mainnetDB
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 200, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Remove mainnet DB')
        self.pushButton.clicked.connect(self.mainnetDB_hornet)
        #End of button Remove the mainnetDB

        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 270, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page

    def start_hornet(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet start ') 
            p=subprocess.Popen("sudo service hornet start", stdout=subprocess.PIPE, shell = True)
            while True:
                #print ("Looping")
                line = p.stdout.readline()
                if not line:
                    break
                print (line.strip())
                sys.stdout.flush()
            QMessageBox.about(self, "Hornet", "Hornet node started")

    def stop_hornet(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet stop ') 
            p=subprocess.Popen("sudo service hornet stop", stdout=subprocess.PIPE, shell = True)
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Hornet", "Hornet node stopped")

    def restart_hornet(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges")
        if os.geteuid()==0:
            #os.system('sudo service hornet restart ') 
            p=subprocess.Popen("sudo service hornet restart", stdout=subprocess.PIPE, shell = True)
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
        self.close()

    def hornet_log_window(self): # Test
        self.cams = hornet_log_win()
        self.cams.show()
        self.close()
        

    def mainnetDB_hornet(self):
        if os.geteuid() != 0:
            print("You need to have root privileges") 
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges") 
        if os.geteuid()==0:
            #os.system('sudo service hornet stop && sudo rm -r /var/lib/hornet/mainnetdb && sudo service hornet start ') 
            p=subprocess.Popen("sudo service hornet stop && sudo rm -r /var/lib/hornet/mainnetdb && sudo service hornet start", stdout=subprocess.PIPE, shell = True)
        while True:
            #print ("Looping")
            line = p.stdout.readline()
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
        QMessageBox.about(self, "Hornet", "Hornet node restarted")

    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close() 

class MainWindow6(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Dashboard access')

        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Dashboard access') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: white; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label

        #Button dashboard access
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535 ; color: white')  #rgb(255,0,0)
        self.pushButton.setText('Open dashboard')
        self.pushButton.clicked.connect(self.hornet_dashboard_access)
        #End of button dashboard access

        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page

    def hornet_dashboard_access(self):
        subprocess.Popen("sudo -upi chromium http://localhost",shell = True)
        subprocess.Popen("sudo -upi firefox http://localhost",shell = True)
        #os.system('sudo -upi chromium http://localhost') 
        subprocess.Popen("sudo -uubuntu firefox http://localhost",shell = True)
        #os.system('sudo -uubuntu firefox http://localhost') 
        subprocess.Popen("sudo -ubeekeeper firefox http://localhost",shell = True)
        #os.system('sudo -ubeekeeper firefox http://localhost') 
        

        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(250, 300, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page

    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close() 

class MainWindow7(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Tools')

        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Tools') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: white; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label

        #Button mountDB beta
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535 ; color: white') #rgb(255,0,0)
        self.pushButton.setText('Mount hornet DB')
        self.pushButton.clicked.connect(self.mountDB)
        #End of button mount DB beta

        #Button Restart SSD fix
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 120, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('SSD-fix')
        self.pushButton.clicked.connect(self.ssd_fix)
        #End of button SSD fix
    
        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 120, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page

    def mountDB(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges") 
        if os.geteuid()==0:
            os.system('sudo mkdir /media/hornetdb && sudo mount /dev/sdb1 /media/hornetdb && sudo chmod 775 /media/hornetdb && sudo echo "/dev/sdb1 /media/hornetdb ext4 defaults  1 1" >> /etc/fstab && sudo cp -fr --preserve /var/lib/hornet/mainnetdb /media/hornetdb/ && sudo mv var/lib/hornet/mainnetdb /var/lib/hornet/mainnetdb.old && sudo ln -sf /media/hornetdb /var/lib/hornet/mainnetdb')
            QMessageBox.about(self, "Hornet DB", "Hornet DB mounted")
    
    def ssd_fix(self):
        if os.geteuid() != 0:
            print("You need to have root privileges")  
            QMessageBox.about(self, "Raspberry Pi Authentication", "You need to have root privileges") 
        if os.geteuid()==0:
            os.system('sudo echo -e "blacklist uas \n blacklist sg" > /etc/modprobe.d/disable_uas.conf')
            QMessageBox.about(self, "SSD fix", "SSD fix executed")
          
    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close() 
    

class MainWindow8(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Help')

        #Create label
        self.labelA = QtWidgets.QLabel(self) 
        #Set label text      
        self.labelA.setText('Help menu') 
        #Set label font
        self.labelA.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Black))
        # setting up background and text color 
        self.labelA.setStyleSheet("background-color: #0B3861; color: white; border: 0px solid black") 
        #Setting position x y
        self.labelA.move(20, 20)
        #Setting label width
        self.labelA.setFixedWidth(150)
        #End label

        #Button report
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535 ; color: white')  #rgb(255,0,0)
        self.pushButton.setText('Report')
        self.pushButton.clicked.connect(self.report)
        #End of button report

        #Button About
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 60, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('About')
        self.pushButton.clicked.connect(self.about)
        #End of button About

        #Button Preparations
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(20, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Preparations')
        self.pushButton.clicked.connect(self.preparations)
        #End of button Preparations

        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(220, 130, 150, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page


    def report(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #0B3861 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Report")
        msg.setText("If you found a bug or experience any issues, please write as at: www.raspihive.org Thanks for your feedback!")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox

    def about(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #0B3861 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("About")
        msg.setText("The Plug and Play solution for a Raspberry Pi IOTA Fullnode! Raspihive: Version beta 1.0")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox
        
    def preparations(self):
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #0B3861 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Preparations")
        msg.setText("The following ports are important for a flawless node operation. Allow basic ports in your router settings: \n \n 14626 UDP - Autopeering port \n \n 15600 TCP - Gossip (neighbors) port \n \n 80 TCP - for Certbot \n \n 443 TCP for Certbot")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox
     
    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close() 

class hornet_status_win(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Hornet-Status')

        #Test
        # For hornet node status
        Outputfileobject=os.popen("sudo service hornet status")     #sudo service hornet status
        Output=Outputfileobject.read()
        Outputfileobject.close()

         #Create label
        labelT = QtWidgets.QLabel(self) 
        #Set label text      
        Text=labelT.setText(Output) 
        #Set label font
        labelT.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
        # setting up background and text color 
        labelT.setStyleSheet("background-color: #353535; color: white; border: 0px solid black") 
        #Setting position x y
        labelT.move(20, 20)
        #Setting label width
        labelT.setFixedWidth(350)
        labelT.setFixedHeight(250)
        #End label


        # Button return to MainWindow 5 
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(250, 300, 250, 40) 
        self.pushButton.setStyleSheet('background-color: #353535 ; color: white') #rgb(0,0,255)
        self.pushButton.setText('Return to Hornet Node Control Center')
        self.pushButton.clicked.connect(self.MainWindow5)
        # End og button return to MainWindow 5 

    def MainWindow5(self):
        self.cams = MainWindow5()
        self.cams.show()
        self.close()

class hornet_log_win(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Hornet-Logs')

        # For hornet node logs
        Outputfileobject=os.popen("sudo journalctl -u hornet -n 50")     #sudo journalctl -u hornet -n 50
        Output=Outputfileobject.read()
        Outputfileobject.close()

         #Create label
        labelT = QtWidgets.QLabel(self) 
        #Set label text      
        Text=labelT.setText(Output) 
        #Set label font
        labelT.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
        # setting up background and text color 
        labelT.setStyleSheet("background-color: #353535 ; color: white; border: 0px solid black") 
        #Setting position x y
        labelT.move(20, 20)
        #Setting label width
        labelT.setFixedWidth(350)
        labelT.setFixedHeight(250)
        #End label

        # Button return to MainWindow 5 
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(250, 300, 250, 40) 
        self.pushButton.setStyleSheet('background-color: #353535; color: white')
        self.pushButton.setText('Return to Hornet Node Control Center')
        self.pushButton.clicked.connect(self.MainWindow5)
        # End og button return to MainWindow5

    def MainWindow5(self):
        self.cams = MainWindow5()
        self.cams.show()
        self.close()


"""
class MainWindow9(Qt.QMainWindow):
    def __init__(self):
        Qt.QMainWindow.__init__(self)

        self.setFixedSize(500, 500)
        self.setStyleSheet('background-color: #0B3861') #rgb(255,255,255);
        self.setWindowTitle('Help')


        # Button return to start page
        self.pushButton = Qt.QPushButton(self)
        self.pushButton.setGeometry(250, 300, 130, 40) 
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #0B3861')
        self.pushButton.setText('Return to start page')
        self.pushButton.clicked.connect(self.return_to_start_page)
        # End og button return to start page

    def return_to_start_page(self):
        self.cams = MainWindow1()
        self.cams.show()
        self.close()
"""
#
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
    w   = MainWindow1()
    # show the window is disabled by default 
    if (rect.width()*rect.height()<=614400): # 7 inch Display = Fullscreen
        w.showMaximized() 
        print("Fullscreen mode")
    else: 
        (rect.width()*rect.height()<=2073600) # > 7 inch Display no Fullscreen
        print("No Fullscreen mode", rect.width())
        w.show()
    
    # start the app 
    sys.exit(app.exec_())

# Start main programm
###############################################################################
if __name__ == '__main__':
    main()
###############################################################################
#End main programm