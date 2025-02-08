from django.urls import path, include
from django.contrib import admin
from django_distill import distill_path

from home import views as home_views
from about import views as about_views
from weekly import views as weekly_views

urlpatterns = [
    path('admin/', admin.site.urls),
    distill_path('', home_views.home, name='home'),
    distill_path('about/', about_views.about, name='about'),
    distill_path('contact/', weekly_views.weekly, name='weekly'),
    path('', include('base.urls')),
]
