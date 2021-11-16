#!/usr/bin/env python3
"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""
# libraries
import sys
import time
import subprocess
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
