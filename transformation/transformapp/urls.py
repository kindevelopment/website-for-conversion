from django.contrib import admin
from django.urls import path, include

from transformapp.views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('add-image/', TransformAdd.as_view(), name='form_add'),
]