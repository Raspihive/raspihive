#sudo pip3 install guizero (auf dem Raspi ausführen - getestet mit Raspi OS Buster) 
# sudo apt-get install python-pip sudo apt-get install python3-pip sudo apt-get install python3-tk

###############################################################################
# Bibliotheken
from guizero import App, Window, Combo, Text, CheckBox, ButtonGroup, PushButton, info, Picture, Box
import tkinter, time, subprocess, os, sys
###############################################################################

# Globale Variablen
localtime = time.asctime( time.localtime(time.time()) )
fullscreen = False
###############################################################################
# Funktionen

def Zeit():   
    text.value = ("Aktuelle lokale Uhrzeit:", localtime)

def ping():
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

def auswahl_linkes_menue():
    what_is_selected_links.value = optionen_links.value
    print(what_is_selected_links.value)
    if what_is_selected_links.value == 'Raspi updaten':
        subprocess.call('echo  | sudo apt update && sudo apt full-upgrade', shell=True)
        print("OK")
    what_is_selected_links.value = optionen_links.value
    if what_is_selected_links.value == 'Hornet Node installieren':
        dirname = os.environ['HOME'] + "/hornet"
        os.makedirs(dirname)
        os.system("sudo apt install build-essential")
        os.system("sudo apt install git")
        os.system("sudo apt install snapd")
        os.system("sudo snap install go --classic")
        os.system("sudo wget -v https://github.com/gohornet/hornet/releases/download/v0.4.1/HORNET-0.4.1_Linux_x86_64.tar.gz")
        os.system("sudo chown paul:paul HORNET-0.4.1_Linux_x86_64.tar.gz")
        os.system("sudo tar -xf HORNET-0.4.1_Linux_x86_64.tar.gz")
        os.system("sudo chown paul:paul -R HORNET-0.4.1_Linux_x86_64")
        print("Hornet successfully installed")

def auswahl_rechtes_menue():
    what_is_selected_rechts.value = optionen_rechts.value
    print(what_is_selected_rechts.value)

###############################################################################

###############################################################################
#Hauptprogramm
# App-Anfang grid = Spalten und Zeilen

app = App(title="Raspihive", bg = (235, 215, 182), width=320, height=480, layout="grid")
text = Text(app, text="Welcome to Raspihive", size=16, font="Times New Roman", color="black", grid=[2,0])
#app.title = ("A different title")

# Klappmenü links
klappmenue_links = Box(app, width="fill", align="top", border=False, grid=[0,0])
optionen_links = Combo(klappmenue_links, options=["Raspi updaten", "Hornet Node installieren", "Nginx installieren", "Livelogs ansehen"], 
align="left")

what_is_selected_links = Text(app, text="nichts ausgewählt", grid=[1,0])

# Klappmenü rechts
klappmenue_rechts = Box(app, width="fill", align="top", border=False, grid=[4,0])
optionen_rechts = Combo(klappmenue_rechts, options=["Raspi neustarten", "Raspi herunterfahren"], 
align="right")

what_is_selected_rechts = Text(app, text="nichts ausgewählt", grid=[5,0])

# auswahl_linkes_menue
button = PushButton(app, command=auswahl_linkes_menue, text="ausführen", grid=[1,1], align="left")

# auswahl_rechtes_menue
button = PushButton(app, command=auswahl_rechtes_menue, text="ausführen rechts", grid=[5,1], align="right")

# Logo (png müsste man mit auf den Pi laden und dann den Pfad angeben...)
#iota = Picture(app, image="/home/paul/Dokumente/iota.gif", grid=[2,2], visible=True)
box = Box(app, layout="grid", grid=[2,1])
button1 = Picture(box, image="/home/paul/Bilder/iota.png", width=310, height=310, grid=[0,0], visible=True)

# zeit
button = PushButton(app, command = Zeit, text="Datum und Uhrzeit", grid=[2,3], align="left")

# ping
button = PushButton(app, command=ping, text="Ping" , grid=[2,3], align="right")







app.display()
#App-Ende
###############################################################################