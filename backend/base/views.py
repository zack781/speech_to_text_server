from django.shortcuts import render
from django.http import JsonResponse
import os
import os.path

from base.templates import write_wav
from base.templates import speech_to_text

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse

from .models import Audio
import boto3

import environ

env = environ.Env()
environ.Env.read_env()

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

def getText(request):
    res = speech_to_text.processing_file()
    return HttpResponse(res);


@csrf_exempt
def getArray(request):
    session = boto3.Session( 
         aws_access_key_id=env("AWS_ACCESS_KEY_ID"),
         aws_secret_access_key=env("AWS_SECRET_ACCESS_KEY"))

         

    if request.method == "POST":

        s3client = boto3.client('s3')

        fileobj = s3client.get_object(
            Bucket=env("AWS_STORAGE_BUCKET_NAME"),
            Key='helloworld.txt'
        )

        filedata = fileobj['Body'].read()

        contents = filedata.decode('utf-8')

        if (list(request.POST.lists())[0][0][-4::] == "DONE"):
            #audio_str = str(list(request.POST.lists())[0][0])
            audio_str = str(contents)
            print(audio_str)
            res_file = write_wav.wav_file(audio_str)

            session = boto3.Session( 
            aws_access_key_id=env("AWS_ACCESS_KEY_ID"), 
            aws_secret_access_key=env("AWS_SECRET_ACCESS_KEY"))
            s3 = session.resource('s3')
            
            mybucket = s3.Bucket(env("AWS_STORAGE_BUCKET_NAME"))
            new_content = ""
            mybucket.put_object(Key="helloworld.txt", Body=new_content)

            s3.meta.client.upload_file(Filename=res_file, Bucket=env("AWS_STORAGE_BUCKET_NAME"), Key='static/audio_data.wav')
        else:
            session = boto3.Session( 
            aws_access_key_id=env("AWS_ACCESS_KEY_ID"), 
            aws_secret_access_key=env("AWS_SECRET_ACCESS_KEY"))
    
            s3 = session.resource('s3')

            mybucket = s3.Bucket(env("AWS_STORAGE_BUCKET_NAME"))
            new_content = str(contents) + str(list(request.POST.lists())[0][0])
            mybucket.put_object(Key="helloworld.txt", Body=new_content)
            
    return HttpResponse("Successful!");


        

    



