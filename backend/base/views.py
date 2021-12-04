from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import os
import os.path

from base.templates import write_wav


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

def getArray(request):
    if request.method == "POST":
        write_wav(request.data)
        

    



