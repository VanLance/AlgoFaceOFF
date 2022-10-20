from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('battle/', include('battle.urls')),
    path('admin/', admin.site.urls),
]