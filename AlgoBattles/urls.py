from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('battles/', include('battles.urls')),
    path('admin/', admin.site.urls),
]