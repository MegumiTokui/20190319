
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hand-home'),
    path('about', views.about,name='hand-about'),
]
