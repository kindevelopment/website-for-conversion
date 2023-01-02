from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import slugify


class Image(models.Model):
    title = models.CharField('Название вашего изображения', max_length=30, blank=True)
    img = models.ImageField('Ваша фотография', )
    slug = models.SlugField(unique=True, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображении'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Rate(models.Model):
    name = models.CharField('Название тарифа', max_length=30)
    price = models.DecimalField('Цена тарифа', max_digits=4, decimal_places=0)
    download_limit = models.PositiveSmallIntegerField('Лимит на загрузку', )
    time_limit = models.PositiveSmallIntegerField('Лимит тарифа по времени', )

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.name


class User(AbstractUser):
    rate = models.ForeignKey(Rate, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Room(models.Model):
    name = models.CharField('Название комнаты', max_length=150)
    slug = models.SlugField(unique=True)
    max_people = models.PositiveSmallIntegerField('Количество людей в комнате', default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.name
