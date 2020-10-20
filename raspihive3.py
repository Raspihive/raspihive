#This Programm is made with love from the IOTA-Community for the IOTA-Community. 
#
###############################################################################
# libraries
from tkinter import Tk as tk, Menu, FLAT, Label, Entry, Button, W, StringVar, ttk
from subprocess import call, Popen, PIPE
import subprocess as sp, os, getpass, sys  
import subprocess, sys, socket, pwd, os, crypt, getpass, spwd
import tkinter as tk, time, os, sys, getpass, os.path
import tkinter.simpledialog
import tkinter.ttk as ttk
from tkinter import messagebox
from functools import partial
# Needed for ping function
from queue import Queue
from ipaddress import ip_address
from threading import Thread
from subprocess import check_output
from tkinter.ttk import (Label, Entry)
from tkinter import (Tk, Button, Text, StringVar, END, Toplevel, BOTH)
import webbrowser

###############################################################################
# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )

##############################################################################
##############################################################################
# start functions
#####################################Start of Window frames############################################

class mainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()
        

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master,  background="lightyellow")
        #self.master.geometry("600x200")

        tk.Label(self, text="Main Page", bg="lightyellow", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        # For page one
        tk.Button(self, text="Update menu", bg="lightyellow",  height = 1,  width = 20,  command=lambda: master.switch_frame(PageOne)).grid(row=1, column=0, padx='10', pady='0')
        # For page two
        tk.Button(self, text="Install menu", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageTwo)).grid(row=1, column=1, padx='10', pady='0')
        # For page three
        tk.Button(self, text="Tools", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageThree)).grid(row=3, column=0, padx='10', pady='0')
        # For page four
        tk.Button(self, text="Help", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageFour)).grid(row=3, column=1, padx='10', pady='0')
        # For page five
        tk.Button(self, text="Node control", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageFive)).grid(row=2, column=0, padx='10', pady='0')
        
        # For page Dashboard Access
        tk.Button(self, text="Dashboard Access", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageSix)).grid(row=2, column=1, padx='10', pady='0')

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="Update menu", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')
        """
        tk.Label(self, text="Update OS").grid(row=1, column=0, padx='0', pady='0')
        tk.Button(self, text="update", command=lambda: master.switch_frame(StartPage)).grid(row=1, column=1, padx='0', pady='0')
        """
        label1 = tk.Label(self, text = "Update OS", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "OS-update", bg="lightblue", height = 1,  width = 20,  command=update_os_function).grid(row=2, column=1, padx='0', pady='0')

        label2 = tk.Label(self, text = "Update packages", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
        button2 = tk.Button(self, text = "P-update", bg="lightblue", height = 1,  width = 20,  command=update_packages_function).grid(row=3, column=1, padx='0', pady='0')

        label3 = tk.Label(self, text = "Update Hornet Node", bg="lightblue", height = 1,  width = 20).grid(row=4, column=0, padx='0', pady='0')
        button3 = tk.Button(self, text = "H-update", bg="lightblue", height = 1,  width = 20, command=update_hornet_node).grid(row=4, column=1, padx='0', pady='0')

        label4 = tk.Label(self, text = "Update Raspihive", bg="lightblue", height = 1,  width = 20).grid(row=5, column=0, padx='0', pady='0')
        button4 = tk.Button(self, text = "R-update", bg="lightblue", height = 1,  width = 20, command=update_raspihive).grid(row=5, column=1, padx='0', pady='0')        


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="Install menu", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

        label1 = tk.Label(self, text = "Install Hornet-Node", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "Install Hornet", bg="lightblue", height = 1,  width = 20, command=Hornet_install_function).grid(row=2, column=1, padx='0', pady='0')

        label1u = tk.Label(self, text = "Uninstall Hornet-Node", bg="lightblue", height = 1,  width = 20).grid(row=2, column=2, padx='0', pady='0')
        button1u = tk.Button(self, text = "Uninstall Hornet", bg="lightblue", height = 1,  width = 20, command=Hornet_uninstall_function).grid(row=2, column=2, padx='0', pady='0')

        label2 = tk.Label(self, text = "Install Bee-Node", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
        button2 = tk.Button(self, text = "Install Bee", bg="lightblue", height = 1,  width = 20, command=Bee_install_function).grid(row=3, column=1, padx='0', pady='0')

        label3 = tk.Label(self, text = "Install rev. proxy + ssl", bg="lightblue", height = 1,  width = 20).grid(row=4, column=0, padx='0', pady='0')
        button3 = tk.Button(self, text = "install RP + SSL", bg="lightblue", height = 1,  width = 20,  command=SSL_reverse_proxy_install_function).grid(row=4, column=1, padx='0', pady='0')


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="Useful tools", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

        label1 = tk.Label(self, text = " Ping test ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "Ping", bg="lightblue", height = 1,  width = 20,  command=Ping_function).grid(row=2, column=1, padx='0', pady='0')

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="Informations", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

        label1 = tk.Label(self, text = " About Raspihive ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "About", bg="lightblue", height = 1,  width = 20, command=about).grid(row=2, column=1, padx='0', pady='0')

        label2 = tk.Label(self, text = "Bug Report", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
        button2 = tk.Button(self, text = "Report", bg="lightblue", height = 1,  width = 20, command=report).grid(row=3, column=1, padx='0', pady='0')

        label3 = tk.Label(self, text = "Preparations", bg="lightblue", height = 1,  width = 20).grid(row=4, column=0, padx='0', pady='0')
        button3 = tk.Button(self, text = "Ports and FW settings", bg="lightblue", height = 1,  width = 20, command=infopreparations).grid(row=4, column=1, padx='0', pady='0')
 
        
class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="Node control", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')
        
        # For page six
        tk.Button(self, text="Hornet Node Control", bg="lightblue", height = 1,  width = 20,  command=lambda: master.switch_frame(PageSix)).grid(row=1, column=0, padx='10', pady='0')
        class PageSix(tk.Frame):
            def __init__(self, master):
                tk.Frame.__init__(self, master, background="lightblue")
                #self.master.geometry("650x200")

                tk.Label(self, text="This is page five", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
                tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

                label1 = tk.Label(self, text = " Start hornet node ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
                button1 = tk.Button(self, text = "Start hornet node", bg="lightblue", height = 1,  width = 20,  command=start_h_function).grid(row=2, column=1, padx='0', pady='0')

                label2 = tk.Label(self, text = " Stop hornet node ", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
                button2 = tk.Button(self, text = "Stop hornet node", bg="lightblue", height = 1,  width = 20,  command=stop_h_function).grid(row=3, column=1, padx='0', pady='0')

                label3 = tk.Label(self, text = " Restart hornet node ", bg="lightblue", height = 1,  width = 20).grid(row=4, column=0, padx='0', pady='0')
                button3 = tk.Button(self, text = "Restart hornet node", bg="lightblue", height = 1,  width = 20,  command=restart_h_function).grid(row=4, column=1, padx='0', pady='0')

                label4 = tk.Label(self, text = " Check hornet status ", bg="lightblue", height = 1,  width = 20).grid(row=5, column=0, padx='0', pady='0')
                button4 = tk.Button(self, text = "Check hornet status", bg="lightblue", height = 1,  width = 20,  command=status_h_function).grid(row=5, column=1, padx='0', pady='0')

                label5 = tk.Label(self, text = " Watch the logs ", bg="lightblue", height = 1,  width = 20).grid(row=6, column=0, padx='0', pady='0')
                button5 = tk.Button(self, text = "Watch the logs", bg="lightblue", height = 1,  width = 20,  command=logs_h_function).grid(row=6, column=1, padx='0', pady='0')

                label6 = tk.Label(self, text = " Remove the mainnetdb ", bg="lightblue", height = 1,  width = 20).grid(row=7, column=0, padx='0', pady='0')
                button6 = tk.Button(self, text = "Remove the mainnnetdb", bg="lightblue", height = 1,  width = 20,  command=mainnetdb_h_function).grid(row=7, column=1, padx='0', pady='0')

class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="Node-Dashboard", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

        label1 = tk.Label(self, text = " Hornet Dashboard ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "Open", bg="lightblue", height = 1,  width = 20,  command=hornet_dashboard).grid(row=2, column=1, padx='0', pady='0')



#####################################End of Window frames############################################
#Start of PW module
def check_pass(username, user_password):
    # username = input("Enter The Username: ")
    try:
        if os.geteuid()==0:
            password = spwd.getspnam(username).sp_pwdp
            if password:
                pw1 = crypt.crypt(user_password, password) == password
                #print("PW1", pw1)
                return pw1
            else:
                return 1
        else:
            print ("User is not root.")
            sys.exit('This script must be run as root!')
    except Exception as e:
        print('eeee:', e)
# End of PW module      

def update_raspihive():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_update_raspihive()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")
 
def validateLogin_update_raspihive(username, password):
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)
    
    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        
        cmd='sudo git pull https://github.com/Raspihive/raspihive.git '
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        
        print("Raspihive updated - ok")
        messagebox.showinfo("Raspihive updated", "Raspihive succesfully updated ") 
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    #return (set later if needed)

def update_os_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_update_os_function()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")



def validateLogin_update_os_function(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)
    
    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()
        cmd='sudo apt update && sudo apt -y full-upgrade && sudo apt -y autoremove'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        while progress_bar['value'] < 100:
            progress_bar['value'] += 10
            #Keep updating the master object to redraw the progress bar
            app.update()
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5) 
        #End progress bar loop
        print("Raspberry Pi updated - OK")
        messagebox.showinfo("Raspberry Pi update", "Raspberry Pi succesfully updated ") 
        progress_bar.destroy()
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    #return (set later if needed)


def update_packages_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_update_packages_function()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")

      

def validateLogin_update_packages_function(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()
        cmd='sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install go --classic'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        while progress_bar['value'] < 100:
            progress_bar['value'] += 10
            #Keep updating the master object to redraw the progress bar
            app.update()
            time.sleep(0.5)
        #End progress bar loop
        print("Packages updated - OK")
        messagebox.showinfo("Packages update", "The packages are succesfully updated") 
        progress_bar.destroy()
    else:
        print("The password you entered is wrong.")
        messagebox.showinfo("Authentication", "The password you entered is wrong") 
    #return (set later if needed)

def update_hornet_node():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_update_hornet_node()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")
  
    
def validateLogin_update_hornet_node(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)
    
    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()
        cmd='sudo service hornet stop && sudo apt-get update && sudo apt-get -y upgrade hornet && sudo service hornet start'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        while progress_bar['value'] < 100:
            progress_bar['value'] += 10
            #Keep updating the master object to redraw the progress bar
            app.update()
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5) 
        #End progress bar loop
        print("Hornet updated - OK")
        messagebox.showinfo("Hornet update", "Hornet Node succesfully updated ") 
        progress_bar.destroy()
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    #return (set later if needed)


def Hornet_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_Hornet_install_function()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")


def validateLogin_Hornet_install_function(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()    
        cmd='sudo apt update && sudo apt upgrade && sudo wget -qO - https://ppa.hornet.zone/pubkey.txt | sudo apt-key add -  && echo "deb http://ppa.hornet.zone stable main" >> /etc/apt/sources.list.d/hornet.list && sudo apt update && sudo apt install hornet && sudo systemctl enable hornet.service && sudo apt-get install -y ufw && sudo ufw allow 15600/tcp && sudo ufw allow 14626/udp && sudo ufw limit openssh && sudo ufw enable && sudo apt-get install sshguard -y && sudo service hornet start'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        while progress_bar['value'] < 100:
            progress_bar['value'] += 10
            #Keep updating the master object to redraw the progress bar
            app.update()
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5)
        #End progress bar loop
        print("Hornet Node installed - OK")
        messagebox.showinfo("Hornet installer", "Hornet Node succesfully installed ") 
        progress_bar.destroy()
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    #return (set later if needed)


def Hornet_uninstall_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_Hornet_uninstall_function()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")

def validateLogin_Hornet_uninstall_function(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()    
        cmd='sudo systemctl stop hornet && sudo apt -qq purge hornet -y'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        while progress_bar['value'] < 100:
            progress_bar['value'] += 10
            #Keep updating the master object to redraw the progress bar
            app.update()
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5)
        #End progress bar loop
        print("Hornet Node installed - OK")
        messagebox.showinfo("Hornet installer", "Hornet Node succesfully uninstalled ") 
        progress_bar.destroy()
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    #return (set later if needed) 


def Bee_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_Bee_install_function()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")
         
      
def validateLogin_Bee_install_function(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        messagebox.showinfo("Bee node installer", "Bee node - coming soon ;)")
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")

def SSL_reverse_proxy_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=validateLogin_SSL_reverse_proxy_install_function()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used") 

#
def validateLogin_SSL_reverse_proxy_install_function(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)
#
    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        #Enter domain name for ssl registration...

        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0) #fix
        progress_bar.grid(row=4, column=0, padx='0', pady='0')
        progress_bar['value'] = 20
        app.update()    
        # Install nginx webserver
        cmd='sudo apt install -y nginx && sudo ufw allow "Nginx Full"'  #sudo apt install -y nginx && sudo ufw allow "Nginx Full"
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        # Nginx configuration
        f = open("/etc/nginx/sites-available/default", "w")
        f.write("server { \n listen 80 default_server; \n listen [::]:80 default_server; \n server_name _; \n location /node { \n proxy_pass http://127.0.0.1:14265/; \n } \n \n location /ws { \n proxy_pass http://127.0.0.1:8081/ws; \n proxy_http_version 1.1; \n proxy_set_header Upgrade $http_upgrade; \n proxy_set_header Connection "'"upgrade"'"; \n proxy_read_timeout 86400; \n } \n \n location / { \n proxy_pass http://127.0.0.1:8081; \n } \n } \n")
        f.close()
        #open and read the file after the appending:
        #f = open("/home/paul/Dokumente/demofile.txt", "r")
        #print(f.read())
        cmd='sudo service nginx reload'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        cmd='sudo apt install software-properties-common -y   && sudo apt update && sudo apt install certbot python3-certbot-nginx -y' #sudo add-apt-repository universe
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        while progress_bar['value'] < 100:
            progress_bar['value'] += 10
            #Keep updating the master object to redraw the progress bar
            app.update()
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5)
        #End progress bar loop
        messagebox.showinfo("SSL installer", "SSL successfully installed and configured") 
        progress_bar.destroy()
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")


# Start of Ping function
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
# End of Ping function

def Time_function():
    print("Time: ", localtime)

def clock():
    t=time.strftime('%I:%M:%S',time.localtime())
    if t!='':
        label1.config(text=t,font='times 12')
    app.after(100,clock)

def report():
    #info for user display message
    messagebox.showinfo("About", " If you found a bug or experience any issues, please write as at: https://raspihive.org/")

def about():
    #info for user display message
    messagebox.showinfo("Report a bug", " The Plug and Play solution for a Raspberry Pi IOTA Fullnode with userfriendly UI and extensions ")

def infopreparations():
    #info for user display message
    messagebox.showinfo("Preparations", "Allow basic ports in your router settings. The following ports are important for a flawless node operation. \n \n 14626 UDP - Autopeering port \n \n 15600 TCP - Gossip (neighbors) port \n \n 80 TCP - for Certbot \n \n 443 TCP for Certbot ")


#Hornet operations
def start_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=starthornet()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")


def starthornet(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)
    
    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        cmd='sudo service hornet start'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #os.system('sudo service hornet start')
        #call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #info for user display message
        messagebox.showinfo("Hornet", "Hornet node started ")
        #time.sleep(2)
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    

def stop_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=stophornet()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")

def stophornet(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        cmd='sudo service hornet stop'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #os.system('sudo service hornet stop')
        #call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #info for user display message
        messagebox.showinfo("Hornet", "Hornet node stopped ")
        #time.sleep(2)
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    

def restart_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=restarthornet()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")

def restarthornet(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        cmd='sudo service hornet restart'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #os.system('sudo service hornet restart')
        #call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #info for user display message
        messagebox.showinfo("Hornet", "Hornet node restarted ")
        #time.sleep(2)
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
    

def status_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=statushornet()
                #window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")

def statushornet(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    #print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        # For hornet node status
        Outputfileobject=os.popen("sudo service hornet status")    
        Output=Outputfileobject.read()
        Outputfileobject.close()
        #Gui log for hornet node status
        root = tk.Tk()
        root.title("Hornet Node Status")
        Text=Label(root,text=Output).grid()
        root.mainloop()
        #End of Gui log for hornet node status
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")

def logs_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  
      

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=logshornet()
                #window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")

#Logui for hornet logs
def log():
    p = subprocess.run("sudo journalctl -u hornet -n 20 ", shell=True, stdout=subprocess.PIPE)
    print(p.stdout.decode())

def logshornet(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        # For hornet node logs
        Outputfileobject=os.popen("sudo journalctl -u hornet -n 10")     
        Output=Outputfileobject.read()
        Outputfileobject.close()
        #Gui log for hornet node status
        root = tk.Tk()
        root.title("Hornet Node Logs")
        Text=Label(root,text=Output).grid()
        root.mainloop()
        #End of Gui log for hornet node status
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")
  

def mainnetdb_h_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(window, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(window, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  

        passwordLabel = Label(window,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(window, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')
      
        #loginButton = Button(window, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=2, padx='0', pady='0')

        loginButton = Button(window, text="Authentication", command=lambda: fun(1))
        loginButton.grid(row=3, column=2, padx='0', pady='0')
        #b2 = Button(window, text="Quit2", command=lambda: fun(2))
        #b2.grid()

        def fun(arg):
            if arg == 1:
                #tkinter.messagebox.showinfo("button 1", "button 1 used")
                command=mainnetdbhornet()
                window.destroy()
            #elif arg == 2:
                #tkinter.messagebox.showinfo("button 2", "button 2 used")

def mainnetdbhornet(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        cmd='sudo rm -r /var/lib/hornet/mainnetdb'
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #os.system('sudo rm -r /var/lib/hornet/mainnetdb')
        #call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        #info for user display message
        messagebox.showinfo("Hornet", "Hornet mainnetdb removed ")
        #time.sleep(2)
    else:
        print("You entered a wrong username or password")
        messagebox.showinfo("Authentication", "The password you entered is wrong")

def hornet_dashboard():
    url = '127.0.0.1:8081'
    webbrowser.open(url)
#Test


###############################################################################
# end functions
###############################################################################
###############################################################################
# Start main programm
###############################################################################

if __name__ == "__main__":
    app = mainWindow()
    app.title("Raspihive")
    app.geometry("")
    #app.geometry("600x130")
    #app.configure(bg='white')
    app['bg'] = 'black'
    

    #app.columnconfigure(0, weight=1)

    # Label for Clock
    label1=Label(app)
    label1.grid(row=0, column=1, padx='40', pady='0')
    clock()


    #Start PW check
    username = StringVar()
    password = StringVar()
    validateLogin_update_os_function = partial(validateLogin_update_os_function, username, password)
    validateLogin_update_packages_function = partial(validateLogin_update_packages_function, username, password)
    validateLogin_update_hornet_node = partial(validateLogin_update_hornet_node, username, password)

    validateLogin_Hornet_install_function = partial(validateLogin_Hornet_install_function, username, password)
    validateLogin_Hornet_uninstall_function = partial(validateLogin_Hornet_uninstall_function, username, password)

    validateLogin_Bee_install_function = partial(validateLogin_Bee_install_function, username, password)
    validateLogin_SSL_reverse_proxy_install_function = partial(validateLogin_SSL_reverse_proxy_install_function, username, password)
    validateLogin_update_raspihive = partial(validateLogin_update_raspihive, username, password)
    
    #Hornet Operations
    starthornet = partial(starthornet, username, password)
    stophornet = partial(stophornet, username, password)
    restarthornet = partial(restarthornet, username, password)
    statushornet = partial(statushornet, username, password)
    logshornet = partial(logshornet, username, password)
    mainnetdbhornet = partial(mainnetdbhornet, username, password)


    app.mainloop()
###############################################################################
# End main programm