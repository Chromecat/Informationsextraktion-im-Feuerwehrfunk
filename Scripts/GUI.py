import re
import time
from datetime import datetime

# Initiale erstellung der GUI aus Dummygui
def creategui(operationpath):
    guiframe = open("HTML/Operation.html", "r")
    guiframetxt = guiframe.read()
    guiframe.close()
    gui = open(operationpath + "/GUI.html", "w")
    guiframetxt = re.sub("<!-- Einsatzpfad -->", operationpath, guiframetxt)
    gui.write(guiframetxt)
    gui.close()


# Aktualisiert die Uhrzeit und fügt eine neue Nachricht hinzu
def reloadgui(operationpath):
    time.sleep(1)
    gui = open(operationpath + "/GUI.html", "r")
    guitxt = gui.read()
    gui.close()
    gui = open(operationpath + "/GUI.html", "w")
    guitxt = re.sub("<!-- Liveuhrzeit -->.*", "<!-- Liveuhrzeit -->Letzte Aktualisierung: " + datetime.now().strftime('%H:%M:%S'), guitxt)

    message = open("HTML/Message.html", "r")
    messagetxt = message.read()
    message.close()
    guitxt = re.sub("<!-- DummyOperation -->", messagetxt, guitxt)

    gui.write(guitxt)
    gui.close()
