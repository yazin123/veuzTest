from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('findLogged.urls')),  # Include logger app URLs
    path('admin/', admin.site.urls),
]
