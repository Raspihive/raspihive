###############################################################################
# libraries
import sys, time, os, subprocess
from PyQt5.QtCore import QThread, pyqtSignal

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

from .helpers import os_parse
##############################################################################
#Thread for OS Update
class MyThread_os_update(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    """
    def getPassword(self):
        text, okPressed = QInputDialog.getText(self, "Root Password","Your system password:", QLineEdit.Password, "")
        if okPressed and text != '':
            return text
        return None
    """
    def run(self):
        print("geteuid:", os.geteuid())
        pre_cmd = ""
        if os.geteuid() != 0:
            print("Raspihive-Update - You need to have root privileges")

        def getPassword(self):
            text, okPressed = QInputDialog.getText(self, "Root Password","Your system password:", QLineEdit.Password, "")
            if okPressed and text != '':
                return text
            return None
            # Ask Password.
            password = self.getPassword()
            if password is None:
                msg = QMessageBox()
                msg.setStyleSheet("background-color: #2B3440 ; color: rgb(255, 255, 255)") #rgb(0, 0, 0)
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Raspberry Pi Authentication")
                msg.setText("You need to have root privileges")
                #msg.setInformativeText("informative text, ya!")
                x = msg.exec_()  # this will show our messagebox
                return
            else:
                pre_cmd = f"echo {password} | sudo -S "

        # os.system('sudo service hornet start ')
        cmd = pre_cmd+"apt update"
        # cmd = pre_cmd + "echo Worked"
        # print("cmd:", cmd)
        p=subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            print(line.strip())
            sys.stdout.flush()
            if cnt == 100:
                print ("CNT 100 erreicht")
                sys.stdout.flush()
                break
            sys.stdout.flush()


        """
        p=subprocess.Popen(os_parse("sudo apt update -y && \
            sudo apt full-upgrade -y && sudo apt autoremove -y \
                && sudo apt clean -y && sudo apt autoclean -y"), \
                    stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            print(line.strip())
            sys.stdout.flush()
            if cnt == 100:
                print ("CNT 100 erreicht")
                sys.stdout.flush()
                break
            sys.stdout.flush()
        """

##############################################################################
#Thread for packages update
class MyThread_packages(QThread):
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(os_parse("sudo apt update -y && \
            sudo apt install -y build-essential && \
                sudo apt install -y git && sudo apt install -y snapd \
                    && sudo snap install go --classic"), \
                        stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
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
        p=subprocess.Popen(os_parse("sudo service hornet stop && \
            sudo apt update && sudo apt -y upgrade hornet && \
                sudo systemctl restart hornet"), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
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
        p=subprocess.Popen(os_parse('sudo apt install -y build-essential \
            && sudo apt install -y git && sudo apt install -y snapd \
            && sudo snap install go --classic && sudo apt update \
            && sudo apt -y upgrade && \
            sudo wget -qO - https://ppa.hornet.zone/pubkey.txt | \
            sudo apt-key add -  && \
            sudo echo "deb http://ppa.hornet.zone stable main" >> \
            /etc/apt/sources.list.d/hornet.list && \sudo apt update \
            && sudo apt install hornet && sudo systemctl enable hornet.service \
            && sudo apt install -y ufw && sudo ufw allow 15600/tcp && \
            sudo ufw allow 14626/udp && sudo ufw limit openssh && \
            sudo ufw enable && sudo apt install sshguard -y \
            && sudo service hornet start'), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
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
        p=subprocess.Popen(os_parse("sudo systemctl stop hornet \
        && sudo apt -qq purge hornet -y && \
        sudo rm -rf /etc/apt/sources.list.d/hornet.list"), \
            stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
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
        p=subprocess.Popen(os_parse("sudo apt update \
        && sudo apt -y upgrade && sudo apt install -y nginx \
        && sudo ufw allow 'Nginx Full' && sudo apt install -y apache2-utils \
        && sudo htpasswd -c /etc/nginx/.htpasswd Raspihive && \
        sudo apt install software-properties-common -y && sudo apt update \
        && sudo apt install certbot python3-certbot-nginx -y \
        && sudo certbot --nginx"), stdout=subprocess.PIPE, shell = True)
        # Nginx configuration
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
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
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
        #print("Test packages")
        p=subprocess.Popen(os_parse("sudo systemctl stop nginx && \
        sudo systemctl disable nginx && \
        sudo apt -qq purge software-properties-common certbot python3-certbot-nginx -y \
        && sudo apt purge -y nginx"), stdout=subprocess.PIPE, shell = True)
        cnt = 0
        while cnt <= 100:
            cnt += 2
            time.sleep(0.1)
            line = p.stdout.readline()
            self.change_value.emit(cnt)
            print(line.strip())
            sys.stdout.flush()
            if cnt == 100:
                print ("CNT 100 erreicht")
                sys.stdout.flush()
                break
            sys.stdout.flush()
