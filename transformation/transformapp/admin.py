from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Image, Rate, Room

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'data_download')


admin.site.register(User, UserAdmin)
admin.site.register(Rate)
admin.site.register(Room)

