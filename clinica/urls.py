from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("hospital.urls"), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
