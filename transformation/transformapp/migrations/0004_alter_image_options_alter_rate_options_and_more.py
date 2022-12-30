# Generated by Django 4.1.4 on 2022-12-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformapp', '0003_alter_image_img_alter_image_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображении'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Тариф', 'verbose_name_plural': 'Тарифы'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Комната', 'verbose_name_plural': 'Комнаты'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='rate',
            name='download_limit',
            field=models.PositiveSmallIntegerField(verbose_name='Лимит на загрузку'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Название тарифа'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=4, verbose_name='Цена тарифа'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='time_limit',
            field=models.PositiveSmallIntegerField(verbose_name='Лимит тарифа по времени'),
        ),
        migrations.AlterField(
            model_name='room',
            name='max_people',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Количество людей в комнате'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название комнаты'),
        ),
    ]
