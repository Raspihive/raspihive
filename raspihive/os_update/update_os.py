#!/usr/bin/env python3
"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""
# libraries
import sys
import time
import os
import subprocess
import stat
from PyQt5.QtCore import QThread, pyqtSignal
#from .helpers import os_parse

##############################################################################
class MyThread_os_update(QThread):
    change_value = pyqtSignal(int)
    def run(self):
        process = subprocess.Popen(("pkexec apt-get update -y && \
            sudo apt-get full-upgrade -y && sudo apt-get autoremove -y \
                && sudo apt-get clean -y && sudo apt autoclean -y"), \
                    stdout=subprocess.PIPE, shell=True)

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
# Hornet enable automatic system updates
def enable_automatic_system_updates():
    os.system("pkexec chown $USER:$GROUPS -R /etc/crontab &&\
        sudo chown $USER:$GROUPS -R /home/")
    f = open("/home/update.sh", "w")
    f.write("apt-get update && apt-get full-upgrade -y")
    f.close()
    os.chmod('/home/update.sh', stat.S_IEXEC)
    subprocess.Popen((' echo "0 20 * * * root /home/update.sh >>\
         /var/log/update_raspihive.log" |\
            tee -a /etc/crontab'), stdout=subprocess.PIPE, shell=True)
    os.system("sudo chown root:root -R /etc/crontab")

##############################################################################
# Hornet disable automatic system updates
def disable_automatic_system_updates():
    os.system("pkexec rm -r /home/update.sh ")
    os.system("sudo chown $USER:$GROUPS -R /etc/crontab")
    #p=subprocess.Popen("crontab -e", stdout=subprocess.PIPE, shell = True)
    filename = '/etc/crontab'
    line_to_delete = 23
    line_to_delete2 = 24
    initial_line = 1
    file_lines = {}
    with open(filename) as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open(filename, "w")
    for line_number, line_content in file_lines.items():
        if ((line_number != line_to_delete) and (line_number != line_to_delete2)):
            f.write('{}\n'.format(line_content))
    f.close()
    os.system("sudo chown root:root -R /etc/crontab")
##############################################################################
