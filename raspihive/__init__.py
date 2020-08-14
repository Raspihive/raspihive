###############################################################################
# libraries
from guizero import App, Window, Combo, Text, TextBox, CheckBox, ButtonGroup, PushButton, info, Picture, Box, MenuBar, yesno
from subprocess import call, Popen, PIPE
from tkinter import Tk as tk, Menu, FLAT, Label, Entry, Button, W, StringVar, ttk
import subprocess as sp, os, getpass, sys  
import subprocess
import tkinter as tk, time, os, sys, getpass, os.path
import tkinter.simpledialog

import tkinter as tk
import tkinter.ttk as ttk
###############################################################################
# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )
###############################################################################
# start functions

# Function to validate the password 
def password_check(pwd):
    if len(pwd) < 4: 
        print('length should be at least 4') 
        info("Raspberry Pi updat", "invalid password") 
    elif len(pwd) > 4:
        print("now you have root privileges")
        #Starting progress bar
        
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(root, orient="horizontal",
                              mode="determinate", maximum=100, value=0)
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

def update_os_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        #password entered
    #CheckPW    
    if (password_check(pwd)): 
        print("test")
        
    
                       

def update_packages_function2():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        #username entered
        print("now you have root privileges")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(root, orient="horizontal",
                              mode="determinate", maximum=100, value=0)
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
        
       

def Hornet_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        print("now you have root privileges")
        print("Hornet option")
        dirname = os.environ['HOME'] + "/test"
        os.makedirs(dirname)
        cmd='sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.2/HORNET-0.4.2_Linux_x86_64.tar.gz -P /home/pi/hornet && sudo chown pi:pi /home/pi/hornet/HORNET-0.4.2_Linux_x86_64.tar.gz && sudo tar -xzf /home/pi/hornet/HORNET-0.4.2_Linux_x86_64.tar.gz -C /home/pi/hornet/ && sudo chown pi:pi -R /home/pi/hornet/HORNET-0.4.2_Linux_x86_64  '
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("Hornet Node successfully installed")
    info("Hornet installer", "Hornet node succesfully installed")

def Bee_install_function():
    
    info("Bee node installer", "Bee node succesfully installed")

def SSL_reverse_proxy_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        print("now you have root privileges")
        cmd='sudo apt update && sudo apt -y full-upgrade'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("SSL installed - OK")
    info("SSL installer", "SSL successfully installed and configured")



def Ping_function():
    print("Ping")
    process = subprocess.Popen(['ping', '-c 3', 'www.google.com'], 
    stdout=subprocess.PIPE,
    universal_newlines=True)
    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output
            for output in process.stdout.readlines():
                print(output.strip())
            break


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