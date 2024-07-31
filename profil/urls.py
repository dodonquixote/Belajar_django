# login/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.profil, name="profil"),
    path('edit-profile', views.edit_profil, name="edit"),  
]
