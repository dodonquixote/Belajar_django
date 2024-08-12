from django import forms
from .models import ContactMassage

class ContactMassageForm(forms.ModelForm):
    class Meta:
        model = ContactMassage
        fields = ['nama', 'email', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'pesan': forms.Textarea(attrs={'class': 'form-control'}),
        }
