from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('faceOff/', include('faceOff.urls')),
    path('admin/', admin.site.urls)
]