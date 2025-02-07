from django.urls import path
from home import views as home_views
from weekly import views as weekly_views
from about import views as about_views

urlpatterns = [
    path('', home_views.home, name='home'),
    path('about/', about_views.about, name='about'),
    path('weekly/', weekly_views.weekly, name='weekly'),
]