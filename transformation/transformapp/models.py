from django.contrib.auth.models import User
from django.db import models


class Image(models.Model):
    img = models.ImageField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Rate(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=4, decimal_places=0)
    download_limit = models.PositiveSmallIntegerField()
    time_limit = models.PositiveSmallIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    max_people = models.PositiveSmallIntegerField()
