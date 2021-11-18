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
#Def activation hornet autopeering
def MyThread_hornet_autopeering():
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
            #QMessageBox.about("Activation autopeering", "Autopeering is now enabled\nPlease restart Hornet.")
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: \
            rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
            msg.setIcon(QMessageBox.Information)
            msg.setText("Hornet autopeering activated")
            #msg.setInformativeText("Hornet autopeering")
            msg.setWindowTitle("Hornet autopeering")
            #msg.setDetailedText("Just close the window\
            #    if the progress bar reaches 100 %, #IOTAstrong")
            msg.exec_()  # this will show our messagebox
        elif string1 not in readfile:
            print("Error - autopeering could not be enabled")
            msg = QMessageBox()
            msg.setStyleSheet("background-color: #2B3440 ; color: \
            rgb(255, 255, 255)") #rgb(0, 0, 0)   #0B3861
            msg.setIcon(QMessageBox.Information)
            msg.setText("Hornet autopeering could not be activated\n\
                Probably already set")
            #msg.setInformativeText("Hornet autopeering")
            msg.setWindowTitle("Hornet autopeering")
            #msg.setDetailedText("Just close the window\
            #    if the progress bar reaches 100 %, #IOTAstrong")
            msg.exec_()  # this will show our messagebox
        # closing a file
        file1.close()
        os.system("sudo chown hornet:hornet /var/lib/hornet/config.json")
    except OSError as ose:
        print('os err:', ose)
    except Exception as e:
        print("Other Exception:", e)
##############################################################################
#Dashboard access
def dashboard_access():
    if path.exists("/etc/letsencrypt/live") == True:
        subprocess.Popen("sudo -upi chromium http://127.0.0.1", shell=True)
        subprocess.Popen("sudo -upi firefox http://127.0.0.1", shell=True)
        #os.system('sudo -upi chromium http://localhost')
        subprocess.Popen("sudo -uubuntu firefox http://127.0.0.1", shell=True)
        #os.system('sudo -uubuntu firefox http://localhost')
        #subprocess.Popen("sudo -ubeekeeper firefox http://127.0.0.1", shell=True)
        #os.system('sudo -ubeekeeper firefox http://localhost')
    else:
        subprocess.Popen("sudo -upi chromium http://localhost:8081", shell=True)
        subprocess.Popen("sudo -upi firefox http://localhost:8081", shell=True)
        #os.system('sudo -upi chromium http://localhost')
        subprocess.Popen("sudo -uubuntu firefox http://localhost:8081", shell=True)
        #os.system('sudo -uubuntu firefox http://localhost')
        #subprocess.Popen("sudo -ubeekeeper firefox http://localhost:8081", shell=True)
        #os.system('sudo -ubeekeeper firefox http://localhost')

#Dashboard access
def sethornetusername():
# Define search string/pattern
    string1 = "admin"
    string2 = "admin"

    try:
        #Get permission for config.json
        os.system("pkexec chown $USER:$GROUPS /var/lib/hornet/config.json")             #/var/lib/hornet/config.json
        # opening and reading the text file
        file1 = open("/var/lib/hornet/config.json", "r")  #/var/lib/hornet/config.json
        readfile = file1.read()

        # checking condition for string found or not
        if string1 in readfile:
            text1, pressed = QInputDialog.getText(self, "Input Text", "Set username: ", QLineEdit.Normal, "")
            path = Path("/var/lib/hornet/config.json")      #/var/lib/hornet/config.json
            #print('String', string1, 'Found In File')
            text = path.read_text()
            text = text.replace("admin", text1) #text to search / replacement text #replace of user admin
            path.write_text(text)
            QMessageBox.about(self, "Set username", "Username was set\nPlease set the password.")
        elif string2 not in readfile: 
            os.system("pkexec chown $USER:$GROUPS /var/lib/hornet/config.json")
            old = oldusername, pressed = QInputDialog.getText(self, "Input old username", "Enter old username first: ", QLineEdit.Normal, "")
            new = newusername, pressed = QInputDialog.getText(self, "Input new username", "Enter new username: ", QLineEdit.Normal, "")
            if old[1]:   #this is because: QInputDialog.gettext() returns a tuple: first value is the text in the inputfield (QLineEdit), the second is bool, True if 'OK' is pressed else False
                old1 = old[0]
                new1 = new[0]
                #print("OLD", new1)
                path = Path("/var/lib/hornet/config.json")
                text = path.read_text()
                text = text.replace(old1, new1) #text to search / replacement text #replace of user admin
                path.write_text(text)
                #file1 = open("test.txt", "a+")
                #file1.write("username" + text1);
                print("current username replaced")
                QMessageBox.about(self, "Set username", "New username was set")
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


#Dashboard access
def sethornetpasswort():
    try:
        #Get permission for config.json
        os.system("pkexec chown $USER:$GROUPS /var/lib/hornet/config.json")             #/var/lib/hornet/config.json
        # Define search string/pattern
        old_pw_hashvalue = "0000000000000000000000000000000000000000000000000000000000000000"
        # opening and reading the text file
        file2 = open("/var/lib/hornet/config.json", "r")  #/var/lib/hornet/config.json
        readfile = file2.read()
        if old_pw_hashvalue in readfile:
            password = password1 , pressed = QInputDialog.getText(self, "Set password", "Set password: ", QLineEdit.Normal, "")
            password2 = password[0]
            child = pexpect.spawn("hornet tools pwd-hash", timeout=None)
            #Get permission for home
            os.system("sudo chown $USER:$GROUPS /home")
            fout = open('/home/passwd.txt', 'wb')  #'/home/pi/Documents/passwd.txt'
            child.logfile = fout
            child.expect("password:")
            child.sendline(password2)
            child.expect("Re-enter your password:")
            child.sendline(password2)
            child.interact()
            child.close()
            # read pw hash from passwd file
            with open("/home/passwd.txt", 'r') as file:
                for line in file.readlines():
                    # python can do regexes, but this is for s fixed string only
                    if "salt:" in line:
                        idx1 = line.find(':')
                        idx2 = line.find('"', idx1)
                        field = line[idx1+2:idx2]
                        #print(field)
            # opening and reading the text file
            #read input file
            path = Path("/var/lib/hornet/config.json")
            text = path.read_text()
            text = text.replace(old_pw_hashvalue, field) #text to search / replacement text #replace of user admin
            path.write_text(text)
            os.system("sudo chown hornet:hornet /var/lib/hornet/config.json")
            #Define search string/pattern - for salt
            old_salt_hashvalue = field+'",'
            #print(old_salt_hashvalue)
            # opening and reading the text file
            file2 = open("/var/lib/hornet/config.json", "r")  #/var/lib/hornet/config.json
            readfile = file2.read()
            if old_salt_hashvalue in readfile:
                #Get permission for config.json
                os.system("sudo chown $USER:$GROUPS /var/lib/hornet/config.json")
                # read pw hash from file
                with open("/home/passwd.txt", 'r') as file:
                    for line in file.readlines():
                        # python can do regexes, but this is for s fixed string only
                        if "hash:" in line:
                            idx1 = line.find(':')
                            idx2 = line.find('"', idx1)
                            field = line[idx1+2:idx2]
                            field = field + '",'
                            #print(field)
                # opening and reading the text file
                #read input file
                path = Path("/var/lib/hornet/config.json")      #/var/lib/hornet/config.json
                text = path.read_text()
                text = text.replace(old_salt_hashvalue, field) #text to search / replacement text #replace of user admin
                path.write_text(text)
                os.system("sudo chown hornet:hornet /var/lib/hornet/config.json")
                #Rm passwd file - (important for security)
                os.system("sudo rm /home/passwd.txt")
                os.system("sudo chown root:root /home")
                QMessageBox.about(self, "Set password", "Password was set\n\
                    Please restart Hornet and you can login into your dashboard")
    except Exception as ex:
        print('ex:', ex)
######################################################################################################################################


