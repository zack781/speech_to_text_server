import speech_recognition as sr
import boto3
from smart_open import smart_open
from io import BytesIO
import io
import wavio

import boto3
import tempfile

import environ

env = environ.Env()
environ.Env.read_env()

def processing_file():
    session = boto3.Session( 
         aws_access_key_id=env("AWS_ACCESS_KEY_ID"), 
         aws_secret_access_key=env("AWS_SECRET_ACCESS_KEY"))
    
    s3 = session.resource('s3')

    my_bucket = s3.Bucket(env("AWS_STORAGE_BUCKET_NAME"))

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)




    tempWavFile = tempfile.mktemp('.wav')
    print("tenpn = ", tempWavFile)

    my_bucket.download_file("static/audio_data.wav", tempWavFile)
    print(tempWavFile)


    filename = tempWavFile.replace("\\", "/")
    print(filename)

    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)



    #s3_client = boto3.client('s3')

    #response = s3_client.get_object(Bucket="radgroup12", Key="static/static/audio_data.wav")
    #r = sr.Recognizer()
    #with smart_open('s3://radgroup12/static/static/audio_data.wav', 'rb') as s3_source:
    #    temp_file = BytesIO(s3_source.read())



    #filename = fn
    #with pt.AudioFile(filename) as source:
    #    audio_data = r.record(source)
    #    text = r.recognize_google(audio_data)
    print("Hello World")
    return text
