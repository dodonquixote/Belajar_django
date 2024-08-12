from django.shortcuts import render, redirect
from .forms import ContactMassageForm  # Import form
from django.contrib import messages

def contact(request):
    form = ContactMassageForm()  # Initialize form
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
    

def sendMassage(request):
    if request.method == 'POST':
        form = ContactMassageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pesan Anda berhasil dikirim")
            return redirect('contact')  # Redirect to a named URL or another view
    else:
        form = ContactMassageForm()
    return render(request, 'contact/contact.html', {'form': form})