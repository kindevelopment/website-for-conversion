from django import forms
from django.contrib.auth import get_user_model
from transformapp.models import Image, Room
from django.contrib.auth.forms import UserCreationForm


class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-image__item'

    class Meta:
        model = Image
        fields = ['title', 'img', ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', ]


class AddRoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddRoomForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-image__item'

    class Meta:
        model = Room
        fields = ['name', 'max_people']
