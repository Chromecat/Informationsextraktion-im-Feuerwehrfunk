from Scripts import GUI, structur, audio, data
from Scripts.Module import messageID

operationpath = structur.createoperationfolder()  # erstellt den initialen Einsatzordner
print(operationpath)

currentoperation = open("currentoperation.txt", "w")  # schreibt den Pfad des aktuellen Einsatzes in die txt
currentoperation.write(operationpath)
currentoperation.close()

GUI.creategui(operationpath)  # Erstellt die initiale HTML als leere GUI

count = 0  # Zähler für die Anzahl der Nachrichten

while True:  # Hauptschleife
    count = count + 1
    messagepath = audio.createaudio(operationpath)
    GUI.reloadgui(operationpath)
    data.datainsert(operationpath, messagepath, count)


