#This Programm is made with love from the IOTA-Community for the IOTA-Community. 

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
# Test
from tkinter import Frame


# from tkinter.messagebox import showinfo
# we need to make our own showinfo widget
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

        tk.Label(self, text="This is the start page", bg="lightyellow", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        # For page one
        tk.Button(self, text="Update menu", bg="lightyellow",  height = 1,  width = 20,  command=lambda: master.switch_frame(PageOne)).grid(row=1, column=0, padx='10', pady='0')
        # For page two
        tk.Button(self, text="Node menu", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageTwo)).grid(row=1, column=1, padx='10', pady='0')
        # For page three
        tk.Button(self, text="Tools", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageThree)).grid(row=2, column=0, padx='10', pady='0')
        # For page four
        tk.Button(self, text="Help", bg="lightyellow", height = 1,  width = 20,  command=lambda: master.switch_frame(PageFour)).grid(row=2, column=1, padx='10', pady='0')

        

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="Update menu Page One", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')
        """
        tk.Label(self, text="Update OS").grid(row=1, column=0, padx='0', pady='0')
        tk.Button(self, text="update", command=lambda: master.switch_frame(StartPage)).grid(row=1, column=1, padx='0', pady='0')
        """
        label1 = tk.Label(self, text = "Update OS", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "os-update", bg="lightblue", height = 1,  width = 20,  command=update_os_function).grid(row=2, column=1, padx='0', pady='0')

        label2 = tk.Label(self, text = "Update packages", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
        button2 = tk.Button(self, text = "p-update", bg="lightblue", height = 1,  width = 20,  command=update_packages_function).grid(row=3, column=1, padx='0', pady='0')

        label3 = tk.Label(self, text = "Update hornet node", bg="lightblue", height = 1,  width = 20).grid(row=4, column=0, padx='0', pady='0')
        button3 = tk.Button(self, text = "h-update", bg="lightblue", height = 1,  width = 20, command=update_hornet_node).grid(row=4, column=1, padx='0', pady='0')


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="This is page two", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

        label1 = tk.Label(self, text = "Install Hornet-Node", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "install hornet", bg="lightblue", height = 1,  width = 20, command=Hornet_install_function).grid(row=2, column=1, padx='0', pady='0')

        label2 = tk.Label(self, text = "Install Bee-Node", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
        button2 = tk.Button(self, text = "install bee", bg="lightblue", height = 1,  width = 20, command=Bee_install_function).grid(row=3, column=1, padx='0', pady='0')

        label3 = tk.Label(self, text = "Install rev. proxy + ssl", bg="lightblue", height = 1,  width = 20).grid(row=4, column=0, padx='0', pady='0')
        button3 = tk.Button(self, text = "install rp + ssl", bg="lightblue", height = 1,  width = 20,  command=SSL_reverse_proxy_install_function).grid(row=4, column=1, padx='0', pady='0')

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="This is page three", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

        label1 = tk.Label(self, text = " Host connectivity test ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "open ping function", bg="lightblue", height = 1,  width = 20,  command=Ping_function).grid(row=2, column=1, padx='0', pady='0')

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master, background="lightblue")
        #self.master.geometry("650x200")

        tk.Label(self, text="This is page four", bg="lightblue", height = 1,  width = 20).grid(row=0, column=0, padx='0', pady='0')
        tk.Button(self, text="Return to start page", bg="lightblue", height = 1,  width = 20, command=lambda: master.switch_frame(StartPage)).grid(row=3, column=2, padx='0', pady='0')

        label1 = tk.Label(self, text = " About Raspihive ", bg="lightblue", height = 1,  width = 20).grid(row=2, column=0, padx='0', pady='0')
        button1 = tk.Button(self, text = "About", bg="lightblue", height = 1,  width = 20, command=about).grid(row=2, column=1, padx='0', pady='0')

        label2 = tk.Label(self, text = "Bug Report", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
        button2 = tk.Button(self, text = "report", bg="lightblue", height = 1,  width = 20, command=report).grid(row=3, column=1, padx='0', pady='0')
 
        



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
        progress_bar['value'] = 0
        app.update()
    
        while progress_bar['value'] < 100:
            progress_bar['value'] += 50
            #Keep updating the master object to redraw the progress bar
            app.update()
            cmd='sudo apt update && sudo apt -y full-upgrade'
            call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
            print("Raspberry Pi updated - OK")
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5)
        #End progress bar loop
        messagebox.showinfo("Raspberry Pi update", "Raspberry Pi succesfully updated ") 
    else:
        print("You entered a wrong username or password")
    #return (set later if needed)


def update_packages_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges") 
        sys.exit
    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(app, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(app, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  

        passwordLabel = Label(app,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(app, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')

        #loginButton = Button(app, text="Authentication", command=validateLogin_update_packages_function)
        #loginButton.grid(row=3, column=1, padx='0', pady='0') 

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
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        #Starting progress bar
        # Create a progressbar widget
        progress_bar = ttk.Progressbar(app, orient="horizontal", mode="determinate", maximum=100, value=0)
        progress_bar.grid(row=4, column=1)
        progress_bar['value'] = 0
        app.update()
 
        while progress_bar['value'] < 100:
            progress_bar['value'] += 50
            #Keep updating the master object to redraw the progress bar
            app.update()
            cmd='sudo apt install -y build-essential && sudo apt install -y git && sudo apt install -y snapd && sudo snap install -y go --classic'
            call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
            print("Packages updated - OK")
            time.sleep(0.5)
        #End progress bar loop
        messagebox.showinfo("Packages update", "The packages are succesfully updated") 
    else:
        print("The password you entered is wrong.")
        messagebox.showinfo("Raspberry Pi update", "The password you entered is wrong") 
    #return (set later if needed)

def update_hornet_node():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges") 
        sys.exit

    
    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(app, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(app, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  

        passwordLabel = Label(app,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(app, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')

        #loginButton = Button(app, text="Authentication", command=validateLogin_update_os_function)
        #loginButton.grid(row=3, column=1, padx='0', pady='0')

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
        progress_bar['value'] = 0
        app.update()
    
        while progress_bar['value'] < 100:
            progress_bar['value'] += 50
            #Keep updating the master object to redraw the progress bar
            app.update()
            cmd='sudo apt-get update && sudo apt-get upgrade hornet'
            call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
            print("Raspberry Pi updated - OK")
            #sys.exit("Raspberry Pi updated - OK \n  Exiting.")
            #exit("Raspberry Pi updated - OK \n  Exiting.")
            time.sleep(0.5)
        #End progress bar loop
        messagebox.showinfo("Raspberry Pi update", "Raspberry Pi succesfully updated ") 
    else:
        print("You entered a wrong username or password")
    #return (set later if needed)

def Hornet_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges") 
        sys.exit

    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(app, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(app, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  

        passwordLabel = Label(app,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(app, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')

        #loginButton = Button(app, text="Authentication", command=validateLogin_Hornet_install_function)
        #loginButton.grid(row=3, column=1, padx='0', pady='0')

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
        dirname = os.environ['HOME'] + "/test"
        os.makedirs(dirname)
        cmd='sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.2/HORNET-0.4.2_Linux_x86_64.tar.gz -P /home/pi/hornet && sudo chown pi:pi /home/pi/hornet/HORNET-0.4.2_Linux_x86_64.tar.gz && sudo tar -xzf /home/pi/hornet/HORNET-0.4.2_Linux_x86_64.tar.gz -C /home/pi/hornet/ && sudo chown pi:pi -R /home/pi/hornet/HORNET-0.4.2_Linux_x86_64  '
        call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)
        print("Hornet Node successfully installed")
        messagebox.showinfo("Hornet installer", "Hornet node succesfully installed") 
    else:
        print("The password you entered is wrong.")
        messagebox.showinfo("Raspberry Pi update", "The password you entered is wrong") 


def Bee_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges")  
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges")
        sys.exit

    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(app, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(app, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  

        passwordLabel = Label(app,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(app, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')

        #loginButton = Button(app, text="Authentication", command=validateLogin_Bee_install_function)
        #loginButton.grid(row=3, column=1, padx='0', pady='0')

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
        messagebox.showinfo("Bee node installer", "Bee node succesfully installed")
    else:
        print("The password you entered is wrong.")
        messagebox.showinfo("Raspberry Pi update", "The password you entered is wrong") 

def SSL_reverse_proxy_install_function():
    if os.geteuid() != 0:
        print("You need to have root privileges") 
        messagebox.showinfo("Raspberry Pi Authentication", "You need to have root privileges") 
        sys.exit

    if os.geteuid()==0:
        #PW function in new window
        window = tk.Toplevel(app)

        usernameLabel = Label(app, text="User Name")
        usernameLabel.grid(row=1, column=1, padx='0', pady='0')
        usernameEntry = Entry(app, textvariable=username)
        usernameEntry.grid(row=1, column=2, padx='0', pady='0')  

        passwordLabel = Label(app,text="Password")
        passwordLabel.grid(row=2, column=1, padx='0', pady='0')  
        passwordEntry = Entry(app, textvariable=password, show='*')
        passwordEntry.grid(row=2, column=2, padx='0', pady='0')

        loginButton = Button(app, text="Authentication", command=validateLogin_SSL_reverse_proxy_install_function)
        loginButton.grid(row=3, column=1, padx='0', pady='0') 


def validateLogin_SSL_reverse_proxy_install_function(username, password):
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    print('password check:', check_pass(username.get(), password.get()))
    pwd = check_pass(username.get(), password.get())
    #print("PW2", pw2)

    if pwd == True: # Needs to match with user password on the system 
        print("You are in!")
        print("SSL installed - OK")
        messagebox.showinfo("SSL installer", "SSL successfully installed and configured") 
    else:
        print("The password you entered is wrong.")
        messagebox.showinfo("Raspberry Pi update", "The password you entered is wrong")


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

###############################################################################
# end functions
###############################################################################
###############################################################################
# Start main programm
###############################################################################

if __name__ == "__main__":
    app = mainWindow()
    app.title("Raspihive")
    app.geometry("600x130")
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
    validateLogin_Hornet_install_function = partial(validateLogin_Hornet_install_function, username, password)
    validateLogin_Bee_install_function = partial(validateLogin_Bee_install_function, username, password)
    validateLogin_SSL_reverse_proxy_install_function = partial(validateLogin_SSL_reverse_proxy_install_function, username, password)

    app.mainloop()

###############################################################################
# End main programm