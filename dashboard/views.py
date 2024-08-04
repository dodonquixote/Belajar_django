from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from profil.models import DataMahasiswa

# @login_required(login_url=settings.LOGIN_URL)
# def dashboard(request):
#     context = {}
#     return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    datamahasiswa = get_object_or_404(DataMahasiswa, user=request.user)
    return render(request, 'dashboard/dashboard.html', {'datamahasiswa': datamahasiswa})