from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .models import *
from .forms import ProfilMahasiswaForm

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
    profilmahasiswa = get_object_or_404(ProfilMahasiswa, user=request.user)
    return render(request, 'profil/profil.html', {'profilmahasiswa': profilmahasiswa})

@login_required(login_url=settings.LOGIN_URL)
def edit_profil(request):
    profilmahasiswa = get_object_or_404(ProfilMahasiswa, user=request.user)
    return render(request, 'profil/edit_profil.html', {'profilmahasiswa': profilmahasiswa})

def updated_profil(request):
    profilmahasiswa = ProfilMahasiswa.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfilMahasiswaForm(request.POST, instance=profilmahasiswa)
        if form.is_valid():
            form.save()
            return redirect('profil')  # Redirect ke halaman profil setelah update
    else:
        form = ProfilMahasiswaForm(instance=profilmahasiswa)

    return render(request, 'profil/edit_profil.html', {'form': form})

# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         form = UpdateProfilForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()  # Simpan perubahan
#             return redirect('profil')  # Arahkan pengguna ke halaman profil
#         else:
#             form = UpdateProfilForm(instance=request.user)
#     context = {
#         'form': form
#     }
#     return render(request, 'profil/profil.html', context)

