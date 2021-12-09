from django import forms
from .models import Audio
class AudioUpload(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('file',)
        def save(self):
            audio = super(AudioUpload, self).save()
            return audio