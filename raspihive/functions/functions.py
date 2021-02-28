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

ICON_IMAGE_URL = "https://raw.githubusercontent.com/Raspihive/raspihiveWebsite/master/public/favicon.ico"


def system_update():
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

def packages_update():
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

#IMPORATANT: Raspihive needs to be cloned into the "/home"-folder, then restart is necessary.
def raspihive_update():
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

def hornet_update():
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

def hornet_install():
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

def hornet_uninstall():
    if path.exists("/var/lib/hornet/") == True:
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
    elif path.exists("/var/lib/hornet") == False:
        print("Hornet Node is not installed. Please install it first")
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Install Nginx + Certbot")
        msg.setText("Hornet Node is not installed. Please install it first")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox

def install_nginx_certbot():
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

    # Nginx configuration
    if path.exists("/etc/nginx/sites-available/") == True:
        os.system("sudo chown pi:pi -R /etc/nginx/")
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

def certbot():
    os.system("lxterminal") #just opens the terminal
    os.system("gnome-terminal") #just opens the terminal

def uninstall_nginx_certbot():
    if path.exists("/etc/nginx/") == True:
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
    else:
        msg = QMessageBox()
        msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Install Nginx + Certbot")
        msg.setText("Nginx + Certbot is not installed. Please install it first")
        #msg.setInformativeText("informative text, ya!")
        x = msg.exec_()  # this will show our messagebox
        print("Nginx + Certbot is not installed. Please install it first")

def start_hornet():
    p=subprocess.Popen("pkexec service hornet start", stdout=subprocess.PIPE, shell = True)
    while True:
        #print ("Looping")
        line = p.stdout.readline()
        if not line:
            break
        print (line.strip())
        sys.stdout.flush()
    QMessageBox.about(self, "Hornet", "Hornet node started")

def stop_hornet():
    p=subprocess.Popen("pkexec service hornet stop", stdout=subprocess.PIPE, shell = True)
    while True:
        #print ("Looping")
        line = p.stdout.readline()
        if not line:
            break
        print (line.strip())
        sys.stdout.flush()
    QMessageBox.about(self, "Hornet", "Hornet node stopped")

def restart_hornet():
    p=subprocess.Popen("pkexec service hornet restart", stdout=subprocess.PIPE, shell = True)
    while True:
        #print ("Looping")
        line = p.stdout.readline()
        if not line:
            break
        print (line.strip())
        sys.stdout.flush()
    QMessageBox.about(self, "Hornet", "Hornet node restarted")

def mainnetDB_hornet():
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

def hornet_dashboard_access():
    subprocess.Popen("sudo -upi chromium http://localhost",shell = True)
    subprocess.Popen("sudo -upi firefox http://localhost",shell = True)
    #os.system('sudo -upi chromium http://localhost')
    subprocess.Popen("sudo -uubuntu firefox http://localhost",shell = True)
    #os.system('sudo -uubuntu firefox http://localhost')
    subprocess.Popen("sudo -ubeekeeper firefox http://localhost",shell = True)
    #os.system('sudo -ubeekeeper firefox http://localhost')

def about():
    msg = QMessageBox()
    msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("About")
    msg.setText("The Plug and Play solution for a Raspberry Pi\n\
    IOTA Fullnode!\n\n\
    Raspihive: Version 2.0\n \n Special thanks to: \n Anistark \n Martin N \n Bernardo \n\n Thanks for testing and bug reporting to\n Olsche from www.easy-passphrase-saver.de")
    #msg.setInformativeText("informative text, ya!")
    x = msg.exec_()  # this will show our messagebox

def preparations():
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

def report():
    msg = QMessageBox()
    msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)")
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Report")
    msg.setText("If you found a bug or experience any issues, please write us \
        as at: www.raspihive.org or get directly in touch by sending \
        an e-mail to: piota@mail.de \nThanks for your feedback!")
    #msg.setInformativeText("informative text, ya!")
    x = msg.exec_()  # this will show our messagebox
