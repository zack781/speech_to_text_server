from django import forms
from .models import Audio

class NewAudioForm(forms.ModelForm):

	class Meta:
		model = Audio
		fields = ['audio_file']