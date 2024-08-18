from django import forms
from .models import BiodataMahasiswa, JadwalKuliah, MataKuliah, NilaiMahasiswa

class BiodataMahasiswaForm(forms.ModelForm):
    class Meta:
        model = BiodataMahasiswa
        fields = ['nik', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'foto']
        widgets = {
            'nik': forms.EmailInput(attrs={'class': 'form-control'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-control'}),
            'foto' : forms.ClearableFileInput(attrs={'class' : 'form-control'})
        }

class JadwalKuliahForm(forms.ModelForm):
    class Meta:
        model = JadwalKuliah
        fields = ['matkul', 'hari', 'jam']  # Hapus 'dosen' jika tidak ada di model
        widgets = {
            'hari': forms.Select(attrs={'class': 'form-control'}),  # Menggunakan Select untuk choices
            'jam': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MataKuliahForm(forms.ModelForm):
    class Meta:
        model = MataKuliah
        fields = ['matkul', 'dosen', 'sks']
        widgets = {
            'matkul': forms.TextInput(attrs={'class': 'form-control'}),
            'dosen': forms.TextInput(attrs={'class': 'form-control'}),
            'sks': forms.Select(attrs={'class': 'form-control'}),  # Menggunakan Select untuk choices
        }


class NilaiMahasiswaForm(forms.ModelForm):
    class Meta:
        model = NilaiMahasiswa 
        fields = ['matkul', 'nilai_huruf'] 
        widgets = {
            'matkul': forms.Select(attrs={'class': 'form-control'}),  # Menggunakan Select untuk ForeignKey
            'nilai_huruf': forms.Select(attrs={'class': 'form-control'}),  # Menggunakan Select untuk choices
        }
