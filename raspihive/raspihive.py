#This Programm is made with love from the IOTA-Community for the IOTA-Community. 
#
###############################################################################
# libraries
from tkinter import Tk as tk, Menu, FLAT, Label, Entry, Button, W, StringVar, ttk
import tkinter as tk, time, os, sys, getpass, os.path
from functools import partial

from pages.index import mainWindow
from helpers import *
###############################################################################
# Globale Variable

localtime = time.asctime( time.localtime(time.time()) )
##############################################################################


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
    clock(app, label1)


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