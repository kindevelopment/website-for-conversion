from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

from transformapp.models import Image
from django.contrib.auth.forms import UserCreationForm


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'img', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', ]
