from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'Student Site'
    }
    return render(request, 'index.html', context)