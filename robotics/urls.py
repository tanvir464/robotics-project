from django.urls import path, include
from django.contrib import admin
from django_distill import distill_url

from home import views as home_views
from about import views as about_views
from weekly import views as weekly_views

urlpatterns = [
    path('admin/', admin.site.urls),
    distill_url('', home_views.home, name='home'),
    distill_url('about/', about_views.about, name='about'),
    distill_url('contact/', weekly_views.weekly, name='weekly'),
    path('', include('base.urls')),
]
