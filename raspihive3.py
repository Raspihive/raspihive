###############################################################################
# libraries
from guizero import App, Window, Combo, Text, TextBox, CheckBox, ButtonGroup, PushButton, info, Picture, Box, MenuBar, yesno
import tkinter, time, subprocess, os, sys, getpass, os.path
import tkinter as tk
from subprocess import call, Popen, PIPE
from tkinter import Tk as tk 
import tkinter.simpledialog
import subprocess as sp, os, getpass, sys  
import subprocess
import tkinter as tk
import tkinter.simpledialog
###############################################################################

# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )
###############################################################################
# start functions

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
    print("Time: ")
    text.value = ("Local time is:", localtime)
    

def entertext():
    displaytext.value = gettext.value
    print(displaytext.value)


# Ask the user if they really want to close the window
def do_this_when_closed():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()

###############################################################################
# end functions


###############################################################################
# Start main programm - App-Anfang grid = Spalten und Zeilen

app = App(title="Raspihive", bg = (235, 215, 182), width=320, height=480, layout="grid")
text = Text(app, text="", size=16, font="Times New Roman", color="black", grid=[2,0], align="top")
#app.title = ("A different title")

menubar = MenuBar(app,
                  toplevel=["Update-menu", "Node installer", "Tools"],
                  options=[
                      [ ["Update Raspberry Pi", update_os_function], ["Update packages", update_packages_function2] ],
                      [ ["Install Hornet Node", Hornet_install_function], ["Install GoShimmer", GoShimmer_function] ],
                      [ ["Ping", Ping_function], ["Show system time", Time_function] ]
                  ])




# insert logo here
#picture1 = Picture(app, image="/home/paul/Dokumente/Raspihive-Projekt-akt/Python_Codeschnipsel/iota.gif", grid=[0,0])


displaytext = Text(app, text="Welcome to Raspihive", size=12, font="Times New Roman", color="black", grid=[0,0])
gettext = TextBox(app, width=10, grid=[2,0])
update_text = PushButton(app, command=entertext, text="enter", grid=[6,0])






# When the user tries to close the window, run the function do_this_when_closed()
app.when_closed = do_this_when_closed

app.display()
###############################################################################
# End main programm 