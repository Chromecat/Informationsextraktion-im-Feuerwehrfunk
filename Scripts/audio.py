import wave
import numpy as np
import pyaudio

from Scripts import structur

CHUNK = 4096  # number of data points to read at a time
RATE = 44100  # time resolution of the recording device (Hz)
FORMAT = pyaudio.paInt16
THRESHOLD = 60  # level ab dem die Aufnahme startet


# Threshold muss an die technische Gegebenheit angepasst werden


def createaudio(operationpath):
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=1, rate=RATE, input=True, frames_per_buffer=CHUNK)
    peak = 0  # start peakwert
    frames = []
    while peak <= THRESHOLD:  # keine Aufnahme
        data = stream.read(CHUNK)
        level = np.frombuffer(data, dtype=np.int16)
        peak = np.average(np.abs(level))
        print("keine Aufnahme " + str(peak))
    while peak > THRESHOLD:  # Aufnahme
        data = stream.read(CHUNK)
        level = np.frombuffer(data, dtype=np.int16)
        peak = np.average(np.abs(level))
        frames.append(data)
        if peak <= THRESHOLD:  # Verzögerung falls beim Sprechen kurze unterbrechnungen sind.
            for z in range(15):  # Anzahl der Frames nach unterschreitung des Treshhold
                print("delayframe nr " + str(z))
                data = stream.read(CHUNK)
                level = np.frombuffer(data, dtype=np.int16)
                peak = np.average(np.abs(level))
                frames.append(data)
                if peak > THRESHOLD:
                    break
    print("Aufnahme" + str(peak))
    messagepath = structur.createmessagefolder(operationpath)
    wavefile = wave.open(messagepath + "/audio.wav", 'wb')
    wavefile.setnchannels(1)
    wavefile.setsampwidth(audio.get_sample_size(FORMAT))
    wavefile.setframerate(RATE)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()
    print("Audio created")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return messagepath
