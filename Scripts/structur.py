import os
import sys
from datetime import datetime


# erstellt den Einsatzordner
def createoperationfolder():  # Einsatzordner erstellen
    operation = (datetime.now().strftime("%d.%m.%Y - %H:%M"))  # Uhrzeit in DD,MM,YYYY - HH:MM
    operationpath = os.path.abspath(operation)  # Erstellung des Path
    try:
        os.mkdir(operationpath)  # Erstellen wenn er nicht schon Existiert
    except FileExistsError:
        sys.exit("Operationfolder already exists")
    return operationpath  # übergabe des Ordnerpfades


# erstellt den Nachrichtenordner
def createmessagefolder(operationpath):  # s.Oben
    message = (datetime.now().strftime("%d.%m.%Y - %H:%M:%S"))
    messagepath = operationpath + "/" + message
    try:
        os.mkdir(messagepath)
    except FileExistsError:
        sys.exit("Messagefolder already exists")
    return messagepath
