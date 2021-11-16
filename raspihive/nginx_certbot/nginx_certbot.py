###############################################################################
#!/usr/bin/env python3
"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""
# libraries
import sys
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
                cnt += 0.1
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
