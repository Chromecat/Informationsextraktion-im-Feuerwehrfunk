import re
import speech_recognition as sr


# Erstellt einen hash aus dem Pfad der NAchricht
def druck(operationpath):
    gui = open(operationpath + "/GUI.html", "r")
    guitxt = gui.read()
    gui.close()
    todo = re.findall("<!-- atemschutzdruck -->.*", guitxt)
    if len(todo) == 0:
        print("Alle Module verarbeitet")
    else:
        for x in range(len(todo)):
            atemschutzbool = ""
            print("atemschutzdruck" + str(todo[x]))

            path = re.sub("<!-- atemschutzdruck --><!-- | -->", "", todo[x])
            audiopath = path + "/audio.wav"

            r = sr.Recognizer()  # Instanz des Recognizer
            audiofile = sr.AudioFile(audiopath)
            with audiofile as source:
                audio = r.record(source)
                try:
                    value = r.recognize_google(audio, language='de-DE')  # der String ist der Wert aus dem Modul
                except Exception:
                    value = "Audiolänge Fehler"

            if "Druck" in value:
                atemschutzbool = "<font color=blue><b>Atemschutzüberwachung</b></font>"
            if "druck" in value:
                atemschutzbool = "<font color=blue><b>Atemschutzüberwachung</b></font>"
            if "niedrigster Druck" in value:
                atemschutzbool = "<font color=blue><b>Atemschutzüberwachung</b></font>"
            if "Niedrigster Druck" in value:
                atemschutzbool = "<font color=blue><b>Atemschutzüberwachung</b></font>"
            guitxt = re.sub("<!-- atemschutzdruck -->", atemschutzbool, guitxt, 1)

        gui = open(operationpath + "/GUI.html", "w")
        gui.write(guitxt)
        gui.close()
