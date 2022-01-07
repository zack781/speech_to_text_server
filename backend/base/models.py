from django.db import models
from django.core.files import File
import os

class Audio(models.Model):

    audio_file = models.FileField(upload_to="")

    #def __str__(self):
    #    with open("example2.wav", 'rb') as f:
    #        self.audio_file.save("audio_data.wav", File(f))
    #    return self.audio_file

class AudioDataStr(models.Model):
    data = models.TextField()

    