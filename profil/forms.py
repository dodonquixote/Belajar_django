from django import forms
from .models import ProfilMahasiswa

class ProfilMahasiswaForm(forms.ModelForm):
    class Meta:
        model = ProfilMahasiswa
        fields = ['email', 'nomor', 'alamat']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nomor': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control'}),
        }