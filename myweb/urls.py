from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('about.urls')),
    path('blog/',include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('login/', include('login.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('profil/', include('profil.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
