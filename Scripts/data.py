import re
from datetime import datetime
# Manipuliert die GUI und trägt Nummer, Pfad etc für jede Nachricht


def datainsert(operationpath, messagepath, count):
    gui = open(operationpath + "/GUI.html", "r")
    guitxt = gui.read()
    gui.close()
    guitxt = re.sub("DummyNr", "Nummer: " + str(count), guitxt)
    guitxt = re.sub("DummyTime", "Uhrzeit: " + str(datetime.now().strftime('%H:%M:%S')), guitxt)
    guitxt = re.sub("DummyPath", "Pfad: " + str(messagepath[-21:]), guitxt)
    guitxt = re.sub("MODULPATH", messagepath, guitxt)
    guitxt = re.sub("DummyAudio", messagepath[-21:], guitxt)
    gui = open(operationpath + "/GUI.html", "w")
    gui.write(guitxt)
    gui.close()
