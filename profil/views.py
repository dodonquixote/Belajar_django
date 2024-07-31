from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
    context = {}
    return render(request, 'profil/profil.html', context)

@login_required(login_url=settings.LOGIN_URL)
def edit_profil(request):
    context = {}
    return render(request, 'profil/edit_profil.html', context)