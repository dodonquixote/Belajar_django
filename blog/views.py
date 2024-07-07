from django.shortcuts import render

# Create your views here.
def blog(request):
    context = {
        'nama': 'Blog saya'
    }
    return render(request, 'blog.html', context)