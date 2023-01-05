from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView
from transformapp.forms import ImageForm, CreateUserForm
from transformapp.models import Image


class MainPage(ListView):
    model = Image
    template_name = 'transformapp/base.html'


class TransformAdd(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'transformapp/push_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
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
    return render(request, 'accounts/register.html', context)




