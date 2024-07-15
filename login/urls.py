from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_views, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
]