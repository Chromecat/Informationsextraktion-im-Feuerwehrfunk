import re
import speech_recognition as sr


# Erstellt einen hash aus dem Pfad der NAchricht
def mayday(operationpath):
    gui = open(operationpath + "/GUI.html", "r")
    guitxt = gui.read()
    gui.close()
    todo = re.findall("<!-- mayday -->.*", guitxt)
    if len(todo) == 0:
        print("Alle Module verarbeitet")
    else:
        for x in range(len(todo)):
            maydaybool = ""
            print("mayday" + str(todo[x]))

            path = re.sub("<!-- mayday --><!-- | -->", "", todo[x])
            audiopath = path + "/audio.wav"

            r = sr.Recognizer()  # Instanz des Recognizer
            audiofile = sr.AudioFile(audiopath)
            with audiofile as source:
                audio = r.record(source)
                try:
                    value = r.recognize_google(audio, language='de-DE')  # der String ist der Wert aus dem Modul
                except Exception:
                    value = "Audiolänge Fehler"

            if "mayday" in value:
                maydaybool = "<font color=red><b>Mayday!</b></font>"
            if "Mayday" in value:
                maydaybool = "<font color=red><b>Mayday!</b></font>"
            guitxt = re.sub("<!-- mayday -->", maydaybool, guitxt, 1)

        gui = open(operationpath + "/GUI.html", "w")
        gui.write(guitxt)
        gui.close()
