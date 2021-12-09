from scipy.io.wavfile import write
import numpy as np
import os, boto3
from boto3 import s3
import sounddevice as sd
from minio import Minio
import io
import wave
from ..models import Audio
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
    #sd.play(data, 8000)
    write("example4.wav", 8000, data)
    #playsound('example4.wav')
