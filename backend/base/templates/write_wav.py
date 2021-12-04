from scipy.io.wavfile import write
import numpy as np

##samplerate = 44100; fs = 100
##t = np.linspace(0., 1., samplerate)
##amplitude = np.iinfo(np.int16).max
##data = amplitude * np.sin(2. * np.pi * fs * t)
##write("example.wav", samplerate, data.astype(np.int16))

def write_wav(audio_str):

    audio_arr = audio_str.split(",")

    audio_arr = audio_arr[0:-1]

    samplerate = 8000
    write("res.wav", samplerate, audio_arr)
        
