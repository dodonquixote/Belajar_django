# login/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profil, name="profil"),    
]
