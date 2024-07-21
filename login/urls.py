# login/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_views, name="login"),
    path('logout', views.logout_view, name="logout"),
    
]
