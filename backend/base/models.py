from django.db import models

class Audio(models.Model):
    
    file_name = models.TextField(default = "default")

    audio_file = models.FileField(blank=True, null=True, default="Coldplay - Adventure Of A Lifetime.wav")
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.file_name