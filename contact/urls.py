from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contact"),
    path('send-massage', views.sendMassage, name="sendmassage")
]