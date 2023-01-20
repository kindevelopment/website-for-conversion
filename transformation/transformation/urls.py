from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from transformapp.views import registerPage

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', registerPage, name='register'),
    path('admin/', admin.site.urls),
    path('', include('transformapp.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
