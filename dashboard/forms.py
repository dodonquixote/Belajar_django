from django import forms
from .models import BiodataMahasiswa

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
