# Generated by Django 4.1.4 on 2023-01-19 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformapp', '0010_alter_image_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(null=True, upload_to='', verbose_name='Ваша фотография'),
        ),
    ]
