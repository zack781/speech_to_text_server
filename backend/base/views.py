from django.shortcuts import render
from django.http import JsonResponse
import os
import os.path

from base.templates import write_wav
from base.templates import speech_to_text

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from scipy.io.wavfile import write

import boto3

from .models import Audio


# Create your views here.
def getRoutes(request):
    return render(request, 'index.html') 

def getFileName(request):
    return JsonResponse('file name', safe=False)

def getAudio(request):
    audio = Audio.objects.create()
    if audio.is_valid():
            audio.audio_file=request.FILES
            audio.save()

@csrf_exempt
def getArray(request):
    res = ''
    if request.method == "POST":
        audio_str = str(list(request.POST.lists())[0][0])
        write_wav.wav_file(audio_str)
        res = speech_to_text.processing("example4.wav")
        #print(str(list(request.POST.lists())[0][0]))
    return HttpResponse(res, content_type="text/plain")
        

    



