# Generated by Django 4.1.4 on 2023-01-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transformapp', '0006_image_data_download_alter_room_max_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]