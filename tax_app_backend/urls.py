from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tax.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('auth/', include('_auth.urls')),
]
