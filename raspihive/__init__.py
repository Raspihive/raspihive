###############################################################################
# libraries
from guizero import App, Window, Combo, Text, TextBox, CheckBox, ButtonGroup, PushButton, info, Picture, Box, MenuBar, yesno
from subprocess import call, Popen, PIPE
from tkinter import Tk as tk, Menu, FLAT, Label, Entry, Button, W, StringVar, ttk
import subprocess as sp, os, getpass, sys  
import subprocess
import getpass
import tkinter as tk, time, os, sys, getpass, os.path
import tkinter.simpledialog
import tkinter as tk
import tkinter.ttk as ttk

import crypt, getpass, spwd

# importing pwd module  
import pwd 
import sys
import os

#Test
import sys
import socket
from queue import Queue
from ipaddress import ip_address
from threading import Thread
from subprocess import check_output
from tkinter.ttk import (
    Label, Entry,
    )
from tkinter import (
    Tk, Button, Text, StringVar, END,
    Toplevel, BOTH
)
# from tkinter.messagebox import showinfo
# we need to make our own showinfo widget
###############################################################################
# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )
###############################################################################
# start functions

#Test

#Endtest

def update_os_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        #while True:
            #user = getpass.getpass("User Name : ",user)
        #pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        pwd = tkinter.simpledialog.askstring(getpass.getuser(), "Enter password:", show='*')        

    #password entered
    #CheckPW    
    if pwd == 'beekeeper': # Needs to match with user password on the system --> beekeeper
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(root, orient="horizontal",
            mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=1, column=0, padx='0', pady='0')
        progress_bar['value'] = 0
        root.update()
    
        while progress_bar['value'] < 100:
            progress_bar['value'] += 50
            #Keep updating the master object to redraw the progress bar
            root.update()
            cmd='sudo apt update && sudo apt -y full-upgrade'
            call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
            print("Raspberry Pi updated - OK")
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5)
        #End progress bar loop
        info("Raspberry Pi update", "Raspberry Pi succesfully updated ")
    else:
        print("The password you entered is wrong.")
        info("Raspberry Pi update", "The password you entered is wrong")

"""
    if len(pwd) < 4: 
        print('length should be at least 4') 
        info("Raspberry Pi update", "invalid password") 
    elif len(pwd) > 4:
        print("now you have root privileges")   
"""                      

def update_packages_function2():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        #while True:
            #user = getpass.getpass("User Name : ",user)
        #pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        pwd = tkinter.simpledialog.askstring(getpass.getuser(), "Enter password:", show='*')        
     
    #password entered
    #CheckPW    
    if pwd == 'beekeeper': # Needs to match with user password on the system --> beekeeper
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", maximum=100, value=0)
        progress_bar.grid(row=0, column=1)
        progress_bar['value'] = 0
        root.update()
 
        while progress_bar['value'] < 100:
            progress_bar['value'] += 50
            #Keep updating the master object to redraw the progress bar
            root.update()
            cmd='sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install -y go --classic'
            call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
            print("Packages updated - OK")
            time.sleep(0.5)
        #End progress bar loop
        info("Packages update", "The packages are succesfully updated")
    else:
        print("The password you entered is wrong.")
        info("Raspberry Pi update", "The password you entered is wrong")



def Hornet_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 

    #password entered
    #CheckPW    
    if pwd == 'beekeeper': # Needs to match with user password on the system --> beekeeper
        print("You are in!")
        dirname = os.environ['HOME'] + "/test"
        os.makedirs(dirname)
        cmd='sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.2/HORNET-0.4.2_Linux_x86_64.tar.gz -P /home/pi/hornet && sudo chown pi:pi /home/pi/hornet/HORNET-0.4.2_Linux_x86_64.tar.gz && sudo tar -xzf /home/pi/hornet/HORNET-0.4.2_Linux_x86_64.tar.gz -C /home/pi/hornet/ && sudo chown pi:pi -R /home/pi/hornet/HORNET-0.4.2_Linux_x86_64  '
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("Hornet Node successfully installed")
        info("Hornet installer", "Hornet node succesfully installed")
    else:
        print("The password you entered is wrong.")
        info("Raspberry Pi update", "The password you entered is wrong")



def Bee_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 

    #password entered
    #CheckPW    
    if pwd == 'beekeeper': # Needs to match with user password on the system --> beekeeper
        print("You are in!")
        info("Bee node installer", "Bee node succesfully installed")
    else:
        print("The password you entered is wrong.")
        info("Raspberry Pi update", "The password you entered is wrong")


def SSL_reverse_proxy_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 

    #password entered
    #CheckPW    
    if pwd == 'beekeeper': # Needs to match with user password on the system --> beekeeper
        print("You are in!")
        cmd='sudo apt update && sudo apt -y full-upgrade'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("SSL installed - OK")
        info("SSL installer", "SSL successfully installed and configured")
    else:
        print("The password you entered is wrong.")
        info("Raspberry Pi update", "The password you entered is wrong")


def Ping_function():

    def validate_ip(ip):
        """
        Validate an ip address
        if the address is a valid ipv4 or ipv6 address
        the functions returns True, otherwise
        it returns False
        """
        try:
            ip_address(ip)
        except:
            return False
        else:
            return True
 
    class Showinfo(Toplevel):
        """
        Spawns a new Toplevel window.
        """
        def __init__(self, *, title, msg, width, height):
            super().__init__(width=width, height=height)
            self.title(title)
            Label(self, text=msg).pack(fill=BOTH)
            Button(self, text="Ok", command=self.destroy).pack(fill=BOTH)
 
    class App(Tk):
        def __init__(self):
            super().__init__()
            self.title('My Ping GUI')
            self.geometry('250x250')
            self.ping_active = False
            self.validation_queue = Queue()
            self.validation_loop()
            self.ip = StringVar(self)
            self.ip.trace_add("write", self.validate)
            self.setup()

        def setup(self):
            Label(self, text="Enter target IP or host as required.").pack()
            Entry(self, textvariable=self.ip).pack()
            ping_button = Button(self, text="Ping Test", command=self.ping)
            ping_button.pack()
            self.ping_button = ping_button
            self.textbox = Text(self, width=150, height=10)
            self.textbox.pack(fill=BOTH)
            Button(self, text="Exit", command=self.destroy).pack()
 
        def validate(self, *args):
            self.validation_queue.put(self.ip.get())
 
        def validation_loop(self):
            self._validation_loop = Thread(target=self._validation_worker, daemon=True)
            self._validation_loop.start()
 
        def set_ping_color(self, color):
            self.ping_button['activebackground'] = color
            self.ping_button['bg'] = color
            self.ping_button['highlightbackground'] = color
 
        def _validation_worker(self):
            while True:
                ip_or_host = self.validation_queue.get()
                is_ip = validate_ip(ip_or_host)
                if is_ip:
                    self.set_ping_color("green")
                else:
                    self.set_ping_color("red")
                # is useful if you want to join a queu
                # then join blocks, until all tasks are done
                self.validation_queue.task_done()
 
        def ping(self):
            if not self.ping_active:
                self.ping_active = True
                self.textbox.delete(1.0, END)
                ip = self.ip.get()
                thread = Thread(target=self.ping_thread)
                thread.start()
 
        def ping_thread(self):
            # code tested on linux
            # ping on windows has different options
            stdout = check_output(['ping', '-c', '3', self.ip.get()], encoding="utf8")
            # print(stdout)
            self.textbox.insert(END, stdout)
            Showinfo(title='Results', msg=stdout, width=200, height=100)
            self.ping_active = False
 
    App().mainloop()
         

def Time_function():
    print("Time: ", localtime)

def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 12')
    root.after(100,clock)

def report():
    #info for user display message
    info("Report a bug", " If you found a bug or experience any issues, please write as at: https://raspihive.org/ ")

def about():
    #info for user display message
    info("About", "The Plug and Play solution for a Raspberry Pi IOTA Fullnode with userfriendly UI and extensions ")


###############################################################################
# end functions

###############################################################################
# Start main programm - App-Anfang grid = Spalten und Zeilen
app=App(title='Raspihive',bg=(53, 60, 81), layout="grid")
root = app.tk #MainWindow = root

#creates menubar
menubar = Menu(root,relief=FLAT,bd=0)

# Sets menubar background color and active select but does not remove 3d  effect/padding
menubar.config(bg = "GREEN",fg='white',activebackground='red',activeforeground='pink',relief=FLAT)

# First item on menubar and creates sub options
filemenu = Menu(menubar, tearoff=0,relief=FLAT, font=("Verdana", 12),activebackground='red')
filemenu.config(bg = "GREEN") 
filemenu.add_command(label="Update Raspberry Pi", command=update_os_function)
filemenu.add_command(label="Update packages", command=update_packages_function2)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Update-menu", menu=filemenu)

# Adds to menubar and creates sub options
editmenu = Menu(menubar, tearoff=0, relief=FLAT, font=("Verdana", 12),activebackground='red')
editmenu.config(bg = "GREEN") 
editmenu.add_command(label="Install Hornet Node", command=Hornet_install_function)
editmenu.add_command(label="Install Bee Node", command=Bee_install_function)
editmenu.add_command(label="Install ssl for trinity and secured dashboard access", command=SSL_reverse_proxy_install_function)
menubar.add_cascade(label="Node installer", menu=editmenu)

pingmenu = Menu(menubar, tearoff=0,bg='green',fg='blue')
pingmenu.add_command(label="Ping", command=Ping_function)
pingmenu.add_command(label="Show system time", command=Time_function)
menubar.add_cascade(label="Tools", menu=pingmenu)
pingmenu.activebackground='red'


helpmenu = Menu(menubar, tearoff=0,bg='green',fg='blue')
helpmenu.add_command(label="Report bug", command=report)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.activebackground='red'

root.config(menu=menubar)
#end of menu

# Necessary, as the root object needs to draw the progressbar widget
# Otherwise, it will not be visible on the screen
root.update()

# Label for Status
label_1 = tk.Label(root, text="Status")
# Use the grid manager
label_1.grid(row=0, column=0, padx='0', pady='0')

# Label for Clock
label1=Label(root)
label1.grid(row=0, column=1, padx='250', pady='0')
clock()



app.display()