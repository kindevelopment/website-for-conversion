from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from transformapp.forms import ImageForm, CreateUserForm, AddRoomForm
from transformapp.models import Image, Room
from transformapp.tasks import transform


class MainPage(ListView):
    model = Image
    template_name = 'transformapp/index.html'


class TransformAdd(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'transformapp/add_image.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.img = transform(form.cleaned_data['img'])
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main')


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

class CreateRoom(LoginRequiredMixin, CreateView):
    model = Room
    form_class = AddRoomForm
    template_name = 'transformapp/add_room.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main')


