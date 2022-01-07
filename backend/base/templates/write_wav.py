from scipy.io.wavfile import write
import speech_recognition as sr
import numpy as np
from ..models import Audio

import tempfile

#from playsound import playsound

##samplerate = 44100; fs = 100
##t = np.linspace(0., 1., samplerate)
##amplitude = np.iinfo(np.int16).max
##data = amplitude * np.sin(2. * np.pi * fs * t)
##write("example.wav", samplerate, data.astype(np.int16))

def wav_file(audio_str):
    audio_arr = audio_str.split(",")

    audio_arr = audio_arr[0:-1]
    print("length = ", len(audio_arr))
    for i in range(len(audio_arr)):
        audio_arr[i] = int(float(audio_arr[i]))

    data = np.asarray(audio_arr, dtype=np.int16)
    
    tempWavFile = tempfile.mktemp('.wav')
    filename = tempWavFile.replace("\\", "/")
    write(filename, 8000, data)
    return filename
    #playsound('example2.wav')
