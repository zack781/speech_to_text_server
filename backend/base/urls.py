from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('file', views.getFileName, name="file"),
    path('upload', views.getAudio, name="get_audio"),
    path('post', views.getArray, name="get_array"),
    path('get', views.getText, name="get_text"),
]