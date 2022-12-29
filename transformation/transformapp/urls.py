from django.contrib import admin
from django.urls import path, include

from transformapp.views import *

urlpatterns = [
    path('', TransformHome.as_view(), name='home')
]