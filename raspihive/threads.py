###############################################################################
# libraries
import sys, time, os, subprocess
from PyQt5.QtCore import QThread, pyqtSignal
from .helpers import os_parse
##############################################################################
#Thread for OS Update
class MyThread_os_update(QThread):
    print("OS - You need to have root privileges")
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        process=subprocess.Popen(os_parse("pkexec apt update -y && \
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
            cnt = 0
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
#Thread for packages update
class MyThread_packages(QThread):
    print("OS - You need to have root privileges")
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(os_parse("sudo apt update -y && \
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
            cnt = 0
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
#Thread for raspihive update
class MyThread_raspihive_update(QThread):
    print("OS - You need to have root privileges")
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(os_parse("sudo rm -r raspihive && \
            sudo git clone https://github.com/Raspihive/raspihive.git"), \
                        stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 0
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
    print("OS - You need to have root privileges")
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(os_parse("sudo service hornet stop && \
            sudo apt update && sudo apt -y upgrade hornet && \
                sudo systemctl restart hornet"), stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 0
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
    print("OS - You need to have root privileges")
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

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 0
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
#Thread for hornet uninstall
class MyThread_hornet_uninstall(QThread):
    print("OS - You need to have root privileges")
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(os_parse("sudo systemctl stop hornet \
        && sudo apt -qq purge hornet -y && \
        sudo rm -rf /etc/apt/sources.list.d/hornet.list"), \
            stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 0
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
    print("OS - You need to have root privileges")
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

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 0
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
#Thread for nginx+certbot uninstall
class MyThread_nginx_certbot_uninstall(QThread):
    print("OS - You need to have root privileges")
    # Create a counter thread
    change_value = pyqtSignal(int)
    def run(self):
        #print("Test packages")
        p=subprocess.Popen(os_parse("sudo systemctl stop nginx && \
        sudo systemctl disable nginx && \
        sudo apt -qq purge software-properties-common certbot python3-certbot-nginx -y \
        && sudo apt purge -y nginx"), stdout=subprocess.PIPE, shell = True)

        p = process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 0
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
