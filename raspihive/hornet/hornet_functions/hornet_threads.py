###############################################################################
# libraries
import sys
import os
import time
import subprocess
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
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
##############################################################################
# Hornet config reset
def Hornet_config_reset():
    if path.exists("/tmp/hornet/") == True:
        os.system("pkexec chown $USER:$GROUPS -R /var/lib/hornet/")
        subprocess.Popen(("sudo service hornet stop \
        && sudo chown $USER:$GROUPS -R /tmp/ \
        && sudo rm -r /tmp/hornet/ \
        && sudo wget https://raw.githubusercontent.com/gohornet/hornet/main/config.json -P /tmp/hornet \
        && sudo mv /tmp/hornet/config.json /var/lib/hornet/ \
        && sudo chown root:root -R /tmp/ \
        && sudo service hornet start"), stdout=subprocess.PIPE, shell=True)
        #QMessageBox.about(self, "Hornet config", "Hornet config successfully reset")
    elif path.exists("/tmp/hornet/") == False:
        os.system("pkexec chown $USER:$GROUPS -R /tmp/")
        subprocess.Popen(("sudo service hornet stop \
        && sudo wget https://raw.githubusercontent.com/gohornet/hornet/main/config.json -P /tmp/hornet \
        && sudo mv /tmp/hornet/config.json /var/lib/hornet/ \
        && sudo chown root:root -R /tmp/ \
        && sudo service hornet start"), stdout=subprocess.PIPE, shell=True)
        #QMessageBox.about(self, "Hornet config", "Hornet config successfully reset")
##############################################################################
# Hornet activation autopeering
def Hornet_activation_autopeering():
    # Define search string/pattern
    string1 = "Spammer"
    try:
        #Get permission for config.json
        os.system("pkexec chown $USER:$GROUPS /var/lib/hornet/config.json")             #/var/lib/hornet/config.json
        # opening and reading the text file
        file1 = open("/var/lib/hornet/config.json", "r")  #/var/lib/hornet/config.json
        readfile = file1.read()
        # checking condition for string found or not
        if string1 in readfile:
            path = Path("/var/lib/hornet/config.json")      #/var/lib/hornet/config.json
            #print('String', string1, 'Found In File')
            text = path.read_text()
            text = text.replace("Spammer", "autopeering") #text to search / replacement text #replace text
            path.write_text(text)
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("About")
            msg.setText("Autopeering activated")
            #msg.setInformativeText("informative text, ya!")
            msg.exec_()  # this will show our messagebox
        elif string1 not in readfile:
            print("Error - autopeering could not be enabled")
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("About")
            msg.setText("Autopeering could not be activated")
            #msg.setInformativeText("informative text, ya!")
            msg.exec_()  # this will show our messagebox
        # closing a file
        file1.close()
        os.system("sudo chown hornet:hornet /var/lib/hornet/config.json")
    except OSError as ose:
        print('os err:', ose)
    except Exception as e:
        print("Other Exception:", e)


