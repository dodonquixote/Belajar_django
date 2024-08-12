from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from profil.models import DataMahasiswa, ProfilMahasiswa
from profil.forms import ProfilMahasiswaForm
from .models import BiodataMahasiswa
from .forms import BiodataMahasiswaForm
from django.contrib import messages


# render data dalam dashboard page
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    datamahasiswa = get_object_or_404(DataMahasiswa, user=request.user)
    return render(request, 'dashboard/dashboard.html', {'datamahasiswa': datamahasiswa})

# render data dalam biodata page
@login_required(login_url=settings.LOGIN_URL)
def biodata(request):
    data = get_object_or_404(DataMahasiswa, user=request.user)
    profil = get_object_or_404(ProfilMahasiswa, user=request.user)
    biodata = get_object_or_404(BiodataMahasiswa, user=request.user)
    return render(request, 'dashboard/biodata.html', {'datamahasiswa': data, 'biodatamahasiswa': biodata, 'profilmahasiswa':profil})

# update biodata dalam biodata page
@login_required(login_url=settings.LOGIN_URL)
def updateBiodata(request):
    data = get_object_or_404(DataMahasiswa, user=request.user)
    profil = get_object_or_404(ProfilMahasiswa, user=request.user)
    biodatamahasiswa = get_object_or_404(BiodataMahasiswa, user=request.user)

    if request.method == 'POST':
        bio_form = BiodataMahasiswaForm(request.POST, request.FILES, instance=biodatamahasiswa)
        profil_form = ProfilMahasiswaForm(request.POST, instance=profil)
        if bio_form.is_valid and profil_form.is_valid():
            bio_form.save()
            profil_form.save()
            messages.success(request, 'Biodata Anda telah diperbarui.')
            return redirect('biodata')  # Redirect ke halaman biodata setelah update
    else:
        bio_form = BiodataMahasiswaForm(instance=biodatamahasiswa)
        profil_form = ProfilMahasiswaForm(instance=profil)
    return render(request, 'dashboard/edit_biodata.html', {
        'bio_form': bio_form,
        'profil_form': profil_form,
        'datamahasiswa': data,
        'biodatamahasiswa': biodatamahasiswa,
        'profilmahasiswa': profil
    })

# render data dalam nilai page
@login_required(login_url=settings.LOGIN_URL)
def nilaiMahasiswa(request):
    context={}
    return render(request, 'dashboard/nilai_mahasiswa.html', context)