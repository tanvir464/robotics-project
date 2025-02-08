from django.urls import path, include
from django.contrib import admin
from django_distill import distill_path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    distill_path('', views.home, name='home'),
]