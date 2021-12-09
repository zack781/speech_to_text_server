from django.db import models

class Audio(models.Model):
    
    file_name = models.TextField(default = "example")

    audio_file = models.FileField(blank=True, null=True, default="dark.wav")
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.file_name

class AudioDataStr(models.Model):
    data = models.TextField()

    