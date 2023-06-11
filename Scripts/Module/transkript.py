import re
import speech_recognition as sr


# Ruft den Google stt auf und erstellt ein Transkript
def transkript(operationpath):
    gui = open(operationpath + "/GUI.html", "r")
    guitxt = gui.read()
    gui.close()
    todo = re.findall("<!-- transkript -->.*", guitxt)
    if len(todo) == 0:
        print("Alle Module verarbeitet")
    else:
        for x in range(len(todo)):
            print("transript" + str(todo[x]))
            path = re.sub("<!-- transkript --><!-- | -->", "", todo[x])
            audiopath = path + "/audio.wav"

            r = sr.Recognizer()  # Instanz des Recognizer
            audiofile = sr.AudioFile(audiopath)
            with audiofile as source:
                audio = r.record(source)
                try:
                    value = r.recognize_google(audio, language='de-DE')  # der String ist der Wert aus dem Modul
                except Exception:
                    value = "Audiolänge Fehler"

            guitxt = re.sub("<!-- transkript -->", "Transkript =  " + str(value), guitxt, 1)

        gui = open(operationpath + "/GUI.html", "w")
        gui.write(guitxt)
        gui.close()
