from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Image, Rate, Room


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')


admin.site.register(User, UserAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Rate)
admin.site.register(Room)

