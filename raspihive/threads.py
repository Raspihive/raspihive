###############################################################################
# libraries
import sys, time, os, subprocess, os.path, shutil
from os import path
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QAction,
    qApp
)
from PyQt5.QtCore import QThread, pyqtSignal
#from .helpers import os_parse
##############################################################################
#Thread for OS Update
class MyThread_os_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        process = subprocess.Popen(("pkexec apt-get update -y && \
            sudo apt-get full-upgrade -y && sudo apt-get autoremove -y \
                && sudo apt-get clean -y && sudo apt autoclean -y"), \
                    stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 1
            while cnt <= 100:
                cnt += 0.1
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for packages update
class MyThread_packages(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(("pkexec apt-get update -y && \
            sudo apt-get install -y build-essential && \
                sudo apt-get install -y git && sudo apt-get install -y snapd \
                    && sudo snap install go --classic"), \
                        stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 1
            while cnt <= 100:
                cnt += 0.2
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################

##############################################################################
#Thread for hornet update
class MyThread_hornet_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(("pkexec service hornet stop && \
            sudo apt-get update && sudo apt-get -y upgrade hornet && \
                sudo systemctl restart hornet"), stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 5
            while cnt <= 100:
                cnt += 1
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for hornet install
class MyThread_hornet_install(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(('pkexec apt-get update -y && sudo apt-get autoremove -y && sudo apt-get install -y build-essential \
            && sudo apt-get install -y git && sudo apt-get install -y snapd \
            && sudo snap install go --classic \
            && sudo apt-get install -y ufw && sudo ufw allow 15600/tcp && \
            sudo ufw allow 14626/udp && sudo ufw limit openssh && \
            sudo ufw enable && sudo apt-get install sshguard -y && sudo wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add - \
            && echo "deb http://ppa.hornet.zone stable main" | sudo tee -a  /etc/apt/sources.list.d/hornet.list \
            && sudo apt-get update \
            && sudo apt-get install hornet && sudo systemctl enable hornet.service \
            && sudo service hornet start '), stdout=subprocess.PIPE, shell = True)
        

            #&& sudo chown pi:pi /etc/apt/sources.list.d
        #sudo mkdir /etc/apt/sources.list.d
        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 1
            while cnt <= 100:
                cnt += 0.4
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for hornet uninstall
class MyThread_hornet_uninstall(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(("pkexec apt-get -qq purge hornet -y  \
            && sudo rm -r /etc/apt/sources.list.d/hornet.list "), \
            stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 5
            while cnt <= 100:
                cnt += 5
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for nginx+certbot install
class MyThread_nginx_certbot_install(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(("pkexec apt-get update -y \
        && sudo apt-get -y upgrade && sudo apt-get install -y nginx \
        && sudo apt-get install -y ufw && sudo ufw allow 'Nginx Full' && sudo apt-get install -y apache2-utils \
        && sudo apt-get install software-properties-common -y && sudo apt-get update \
        && sudo apt-get install certbot python3-certbot-nginx -y \
        "), stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 1
            while cnt <= 100:
                cnt += 0.1
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for nginx+certbot uninstall
class MyThread_nginx_certbot_uninstall(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        if path.exists("/etc/nginx/") == True:
            #print("Test packages")
            process = subprocess.Popen(("pkexec apt-get update -y && \
            sudo apt-get purge -y nginx nginx-common && sudo apt-get purge -y --auto-remove apache2-utils \
            && sudo apt-get -qq purge software-properties-common certbot python3-certbot-nginx -y \
            && sudo apt-get autoremove -y\
                "), stdout=subprocess.PIPE, shell = True)

            p = process.stdout.readline()
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                print('RETURN CODE', return_code)
            else:
                print("STARTING")
                cnt = 1
                while cnt <= 100:
                    cnt += 0.5
                    time.sleep(0.1)
                    line = process.stdout.readline()
                    self.change_value.emit(cnt)
                    print(line.strip())
                    sys.stdout.flush()
                    if cnt == 100:
                        print ("CNT 100 erreicht")
                        sys.stdout.flush()
                    sys.stdout.flush()
        else:
            print("Nginx not installed")
