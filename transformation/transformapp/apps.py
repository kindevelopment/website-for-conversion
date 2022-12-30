from django.apps import AppConfig


class TransformappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'transformapp'
    verbose_name = 'Приложение для конвертирования'