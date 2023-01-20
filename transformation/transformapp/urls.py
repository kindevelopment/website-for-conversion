from django.contrib import admin
from django.urls import path, include

from transformapp.views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('download/', ListFile.as_view(), name='download'),
    path('add-image/', TransformAdd.as_view(), name='image_add'),
    path('add-room/', CreateRoom.as_view(), name='room_add'),
]

