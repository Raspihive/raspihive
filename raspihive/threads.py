###############################################################################
# libraries
import sys, time, os, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QProgressBar, QPushButton, QAction, qApp, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets, Qt, QtGui
from subprocess import Popen, PIPE
from PyQt5.QtWidgets import (QMainWindow, QToolTip, QLabel, QVBoxLayout, QTabWidget, QHBoxLayout)
from PyQt5.QtCore import pyqtSlot, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QFont, QCursor, QImage

##############################################################################
#Thread for OS Update
class MyThread_os_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        p=subprocess.Popen(("sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt clean -y && sudo apt autoclean -y"), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt+=4
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
##############################################################################
#Thread for packages update
class MyThread_packages(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(("sudo apt update -y && sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic"), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt+=4
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
##############################################################################
#Thread for hornet update
class MyThread_hornet_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(("sudo service hornet stop && sudo apt update && sudo apt -y upgrade hornet && sudo systemctl restart hornet"), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt+=4
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
##############################################################################
#Thread for hornet install
class MyThread_hornet_install(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(('sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic && sudo apt update && sudo apt -y upgrade && sudo wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add -  && sudo echo "deb http://ppa.hornet.zone stable main" >> /etc/apt/sources.list.d/hornet.list && sudo apt update && sudo apt install hornet && sudo systemctl enable hornet.service && sudo apt install -y ufw && sudo ufw allow 15600/tcp && sudo ufw allow 14626/udp && sudo ufw limit openssh && sudo ufw enable && sudo apt install sshguard -y && sudo service hornet start'), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt+=4
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
##############################################################################
#Thread for hornet uninstall
class MyThread_hornet_uninstall(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(("sudo systemctl stop hornet && sudo apt -qq purge hornet -y && sudo rm -rf /etc/apt/sources.list.d/hornet.list"), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt+=10
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()

##############################################################################
#Thread for nginx+certbot uninstall
class MyThread_nginx_certbot_uninstall(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(("sudo systemctl stop nginx && sudo systemctl disable nginx && sudo apt -qq purge software-properties-common certbot python3-certbot-nginx -y && sudo apt purge -y nginx"), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt+=4
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            if not line:
                break
            print (line.strip())
            sys.stdout.flush()
