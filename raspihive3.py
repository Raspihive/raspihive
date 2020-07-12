###############################################################################
# libraries
from guizero import App, Window, Combo, Text, CheckBox, ButtonGroup, PushButton, info, Picture, Box, MenuBar, yesno
import tkinter, time, subprocess, os, sys
###############################################################################

# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )

###############################################################################
# start functions

def file_function():
    print("Update Raspberry Pi")
    subprocess.call('echo  | sudo apt update && sudo apt full-upgrade', shell=True)
    print("Raspberry Pi updated - OK")

def file_function2():
    print("Update packages")
    os.system("sudo apt install -y build-essential")
    os.system("sudo apt install -y git")
    os.system("sudo apt install -y snapd")
    os.system("sudo snap install -y go --classic")
    print("Packages updated - OK")

def Hornet_function():
    print("Hornet option")
    os.system("sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.1/HORNET-0.4.1_Linux_x86_64.tar.gz")
    os.system("sudo chown pi:pi HORNET-0.4.1_Linux_x86_64.tar.gz")
    os.system("sudo tar -xf HORNET-0.4.1_Linux_x86_64.tar.gz")
    os.system("sudo chown pi:pi -R HORNET-0.4.1_Linux_x86_64")
    print("Hornet Node successfully installed")


def GoShimmer_function():
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
    


# Ask the user if they really want to close the window
def do_this_when_closed():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()

###############################################################################
# end functions


###############################################################################
# Start main programm - App-Anfang grid = Spalten und Zeilen

app = App(title="Raspihive", bg = (235, 215, 182), width=320, height=480, layout="grid")
text = Text(app, text="Welcome to Raspihive", size=16, font="Times New Roman", color="black", grid=[2,0])
#app.title = ("A different title")

menubar = MenuBar(app,
                  toplevel=["Auswahl", "Node installer", "Tools"],
                  options=[
                      [ ["Update Raspberry Pi", file_function], ["Update packages", file_function2] ],
                      [ ["Install Hornet Node", Hornet_function], ["Install GoShimmer", GoShimmer_function] ],
                      [ ["Ping", Ping_function], ["Show system time", Time_function] ]
                  ])



















# When the user tries to close the window, run the function do_this_when_closed()
app.when_closed = do_this_when_closed

app.display()
###############################################################################
# End main programm 