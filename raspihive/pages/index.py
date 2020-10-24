
from tkinter import Tk as tk, Menu, FLAT, Label, Entry, Button, W, StringVar, ttk

from helpers import *
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

        label2 = tk.Label(self, text = " Mount Hornet DB to SSD", bg="lightblue", height = 1,  width = 20).grid(row=3, column=0, padx='0', pady='0')
        button2 = tk.Button(self, text = "mount", bg="lightblue", height = 1,  width = 20,  command=mounthornetDBtoextDrive).grid(row=3, column=1, padx='0', pady='0')

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