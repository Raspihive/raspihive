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

def report():
    print ("hello!")
    #Test for user display
    info("info", " If you found a bug or experience any issues, please write as at: https://raspihive.org/ ")

def about():
    info("info", "The Plug and Play solution for a Raspberry Pi IOTA Fullnode with userfriendly UI and extensions ")

def update_os_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        print("now you have root privileges")
        cmd='sudo apt update && sudo apt -y full-upgrade'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("Raspberry Pi updated - OK")
        #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
        #exit("Raspberry Pi updated - OK \n  Exiting.")

def update_packages_function2():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        print("now you have root privileges")
        cmd='sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install -y go --classic'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("Packages updated - OK")
        

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
        cmd='sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.1/HORNET-0.4.1_Linux_x86_64.tar.gz -P /home/pi/hornet && sudo chown pi:pi /home/pi/hornet/HORNET-0.4.1_Linux_x86_64.tar.gz && sudo tar -xzf /home/pi/hornet/HORNET-0.4.1_Linux_x86_64.tar.gz -C /home/pi/hornet/ && sudo chown pi:pi -R /home/pi/hornet/HORNET-0.4.1_Linux_x86_64  '
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("Hornet Node successfully installed")
   

def GoShimmer_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")
        tk.Tk().withdraw()
        #username = getpass.getuser()
        pwd = tkinter.simpledialog.askstring("[sudo] password for user:", "Enter password:", show='*') 
        print("now you have root privileges")
        dirname = os.environ['HOME'] + "/goshimmer"
        os.makedirs(dirname)
        cmd='sudo git clone -v https://github.com/iotaledger/goshimmer.git /home/pi/goshimmer'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("GoShimmer Node successfully installed")
        

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
        label1.config(text=t,font='times 25')
    root.after(100,clock)

def showPass():
    passwordClear.set(password.get())   

def update_progress_bar():
    x = barVar.get()
    if x < 100:
        barVar.set(x+0.5)
        root.after(50, update_progress_bar)
    else:
        print("Complete")
    
###############################################################################
# end functions

###############################################################################
# Start main programm - App-Anfang grid = Spalten und Zeilen


app=App(title='Raspihive',bg=(53, 60, 81), layout="grid")
root = app.tk #MainWindow = root

label1=Label(root)
label1.grid(row=8, column=8)
clock()

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
editmenu.add_command(label="Install GoShimmer", command=GoShimmer_function)
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



#Test for user display
password = StringVar()
passwordClear = StringVar()

label_1 = ttk.Label(root, text='Type your password: ')
label_1.grid(row=1,column=1)
entry_1 = ttk.Entry(root, textvariable=password, width=6, show='*')
entry_1.grid(row=2, column=1)
label_2 = ttk.Label(root, text='Your password is: ')
label_2.grid(row=3, column=1)
label_3 = ttk.Label(root, textvariable=passwordClear)
label_3.grid(row=4, column=1)
button_1 = ttk.Button(root, text='show', command=showPass, width=5)
button_1.grid(row=5,column=1)


barVar = tk.DoubleVar()
barVar.set(0)
bar = ttk.Progressbar(root, length=200, style='black.Horizontal.TProgressbar', variable=barVar, mode='determinate')
bar.grid(row=1, column=0)
button= tk.Button(root, text='Click', command=update_progress_bar)
button.grid(row=0, column=0)



app.display()