###############################################################################
# libraries
import sys
import os
import time
import subprocess
from PyQt5.QtCore import QThread, pyqtSignal
from os import path
from pathlib import Path
#from .helpers import os_parse
##############################################################################
#Necessary packages for hornet
class MyThread_packages(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(("pkexec apt-get update -y && \
            sudo apt-get install -y build-essential && \
                sudo apt-get install -y git && sudo apt-get install -y snapd \
                    && sudo snap install go --classic"), stdout=subprocess.PIPE, shell=True)

        process.stdout.readline()
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
                    print("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for hornet update
class MyThread_hornet_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(("pkexec service hornet stop && \
            sudo apt-get update && sudo apt-get -y upgrade hornet && \
                sudo systemctl restart hornet"), stdout=subprocess.PIPE, shell=True)

        process.stdout.readline()
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
                    print("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for hornet install
class MyThread_hornet_install(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        process = subprocess.Popen(('pkexec apt-get update -y && sudo apt-get autoremove -y \
            && sudo apt-get install -y build-essential \
            && sudo apt-get install -y git && sudo apt-get install -y snapd \
            && sudo snap install go --classic \
            && sudo apt-get install -y ufw && sudo ufw allow 15600/tcp && \
            sudo ufw allow 14626/udp && \
            sudo ufw enable && sudo apt-get install sshguard -y && sudo wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add - \
            && echo "deb http://ppa.hornet.zone stable main" | sudo tee -a  /etc/apt/sources.list.d/hornet.list \
            && sudo apt-get update \
            && sudo apt-get install hornet && sudo systemctl enable hornet.service \
            && sudo service hornet start '), stdout=subprocess.PIPE, shell=True)
            #&& sudo chown pi:pi /etc/apt/sources.list.d
        #sudo mkdir /etc/apt/sources.list.d
        process.stdout.readline()
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
                    print("CNT 100 erreicht")
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
            && sudo rm -r /etc/apt/sources.list.d/hornet.list "), stdout=subprocess.PIPE, shell=True)

        process.stdout.readline()
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
                    print("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
##############################################################################
#Thread for hornet config reset
class  MyThreadhornetconfigreset(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        if path.exists("/tmp/hornet/") == True:
            print("Test1")
            os.system("pkexec chown $USER:$GROUPS -R /var/lib/hornet/")
            subprocess.Popen(("sudo service hornet stop \
            && sudo chown $USER:$GROUPS -R /tmp/ \
            && sudo rm -r /tmp/hornet/ \
            && sudo wget https://raw.githubusercontent.com/gohornet/hornet/main/config.json /tmp/hornet \
            && sudo mv /tmp/hornet/config.json /var/lib/hornet/ \
            && sudo chown root:root -R /tmp/ \
            && sudo service hornet start"), stdout=subprocess.PIPE, shell=True)
            
            cnt = 5
            while cnt <= 100:
                cnt += 1
                time.sleep(1)
                #line = process.stdout.readline()
                self.change_value.emit(cnt)
                #print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
        elif path.exists("/tmp/hornet/") == False:
            print("Test2")

            os.system("pkexec chown $USER:$GROUPS -R /tmp/")
            subprocess.Popen(("sudo service hornet stop \
            && sudo wget https://raw.githubusercontent.com/gohornet/hornet/main/config.json /tmp/hornet \
            && sudo mv /tmp/hornet/config.json /var/lib/hornet/ \
            && sudo chown root:root -R /tmp/ \
            && sudo service hornet start"), stdout=subprocess.PIPE, shell=True)


            cnt = 1
            while cnt <= 100:
                cnt += 1
                time.sleep(1)
                #line = process.stdout.readline()
                self.change_value.emit(cnt)
                #print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
            #print("Test packages")
            #stdout.readline()
            # Do something else
