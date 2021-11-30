###############################################################################
#!/usr/bin/env python3
# libraries
import sys
import os
import time
import subprocess
from os import path
from PyQt5.QtCore import QThread, pyqtSignal

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
        "), stdout=subprocess.PIPE, shell=True)

        process.stdout.readline()
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
        else:
            print("STARTING")
            cnt = 1
            while cnt <= 100:
                cnt += 0.3
                time.sleep(0.1)
                line = process.stdout.readline()
                self.change_value.emit(cnt)
                print(line.strip())
                sys.stdout.flush()
                if cnt == 100:
                    print("CNT 100 erreicht")
                    sys.stdout.flush()
                sys.stdout.flush()
        
        # Nginx configuration
        if path.exists("/etc/nginx/sites-available/") == True:
            os.system("sudo chown $USER:$GROUPS -R /etc/nginx/")
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
                \n proxy_pass http://127.0.0.1:8081; \n   } \n } \n")
                f.close()
                os.system('sudo systemctl start nginx && sudo systemctl enable nginx')
            except: # occurs because of permission denied error
                print("An exception occurred - Config not written - FAILURE")
        else:
            print("Config not written - FAILURE")
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
                "), stdout=subprocess.PIPE, shell=True)

            process.stdout.readline()
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
                        print("CNT 100 erreicht")
                        sys.stdout.flush()
                    sys.stdout.flush()
        else:
            print("Nginx not installed")

##############################################################################
# Activate automatic renewing ssl cert
def enable_auto_ssl():
    os.system("pkexec chown $USER:$GROUPS -R /var/spool/cron/crontabs/")
    #p=subprocess.Popen("crontab -e", stdout=subprocess.PIPE, shell = True)
    subprocess.Popen((' echo "0 12 * * * /usr/bin/certbot renew --quiet" |\
        tee -a /var/spool/cron/crontabs/$USER'), stdout=subprocess.PIPE, shell=True)
    os.system("sudo chown root:root -R /var/spool/cron/crontabs/$USER")

##############################################################################
# Deactivate automatic renewing ssl cert
def disable_auto_ssl():
    #os.system("pkexec chown $USER:$GROUPS -R /var/spool/cron/crontabs/pi")
    subprocess.Popen("crontab -r", stdout=subprocess.PIPE, shell=True)

