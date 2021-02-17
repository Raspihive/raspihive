###############################################################################
# libraries
import sys, time, os, subprocess, os.path
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
from .helpers import os_parse
##############################################################################
#Thread for OS Update
class MyThread_os_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        process = subprocess.Popen(os_parse("pkexec apt update -y && \
            sudo apt full-upgrade -y && sudo apt autoremove -y \
                && sudo apt clean -y && sudo apt autoclean -y"), \
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
                    break
                sys.stdout.flush()
##############################################################################
#Thread for packages update
class MyThread_packages(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(os_parse("pkexec apt update -y && \
            sudo apt install -y build-essential && \
                sudo apt install -y git && sudo apt install -y snapd \
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
                    break
                sys.stdout.flush()
##############################################################################
#Thread for raspihive update
class MyThread_raspihive_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(os_parse("pkexec rm -r raspihive && \
            sudo git clone https://github.com/Raspihive/raspihive.git"), \
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
                cnt += 1
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                    break
                sys.stdout.flush()
##############################################################################
#Thread for hornet update
class MyThread_hornet_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(os_parse("pkexec service hornet stop && \
            sudo apt update && sudo apt -y upgrade hornet && \
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
                    break
                sys.stdout.flush()
##############################################################################
#Thread for hornet install
class MyThread_hornet_install(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(os_parse('pkexec apt update -y && sudo apt autoremove -y && sudo apt install -y build-essential \
            && sudo apt install -y git && sudo apt install -y snapd \
            && sudo snap install go --classic \
            && sudo apt install -y ufw && sudo ufw allow 15600/tcp && \
            sudo ufw allow 14626/udp && sudo ufw limit openssh && \
            sudo ufw enable && sudo apt install sshguard -y \
            && wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add - \
            && sudo chown pi:pi /etc/apt/sources.list.d && sudo echo "deb http://ppa.hornet.zone stable main" >> \
            /etc/apt/sources.list.d/hornet.list && sudo apt update \
            && sudo apt install hornet && sudo systemctl enable hornet.service \
            && sudo service hornet start'), stdout=subprocess.PIPE, shell = True)
        
        #sudo mkdir /etc/apt/sources.list.d
        """
        process = subprocess.Popen(('pkexec wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add - \
            && sudo echo "deb http://ppa.hornet.zone stable main" >> \
            /etc/apt/sources.list.d/hornet.list && sudo apt update \
            && sudo apt install hornet && sudo systemctl enable hornet.service \
            && sudo service hornet start'), stdout=subprocess.PIPE, shell = True)
        """

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 5
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
                    break
                sys.stdout.flush()
##############################################################################
#Thread for hornet uninstall
class MyThread_hornet_uninstall(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(os_parse("pkexec apt -qq purge hornet -y  \
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
                cnt += 1
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print ("CNT 100 erreicht")
                    sys.stdout.flush()
                    break
                sys.stdout.flush()
##############################################################################
#Thread for nginx+certbot install
class MyThread_nginx_certbot_install(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(os_parse("pkexec apt update -y \
        && sudo apt -y upgrade && sudo apt install -y nginx \
        && sudo apt install -y ufw && sudo ufw allow 'Nginx Full' && sudo apt install -y apache2-utils \
        && sudo htpasswd -c /etc/nginx/.htpasswd Raspihive && \
        sudo apt install software-properties-common -y && sudo apt update \
        && sudo apt install certbot python3-certbot-nginx -y \
        "), stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 5
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
                    break
                sys.stdout.flush()
##############################################################################
#Thread for nginx+certbot uninstall
class MyThread_nginx_certbot_uninstall(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        if path.exists("/etc/nginx/") == True:
            #print("Test packages")
            process = subprocess.Popen(os_parse("pkexec apt update -y && \
            sudo apt purge -y nginx nginx-common && sudo apt purge -y --auto-remove apache2-utils \
            && sudo apt -qq purge software-properties-common certbot python3-certbot-nginx -y \
            && sudo apt autoremove -y\
                "), stdout=subprocess.PIPE, shell = True)

            p = process.stdout.readline()
            # Do something else
            return_code = process.poll()
            if return_code is not None:
                print('RETURN CODE', return_code)
            else:
                print("STARTING")
                cnt = 5
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
                        break
                    sys.stdout.flush()
        else:
            print("Nginx not installed")
