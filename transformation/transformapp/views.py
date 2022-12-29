from django.shortcuts import render
from django.views.generic import View


class TransformHome(View):
    template_name = 'transformapp/base.html'

