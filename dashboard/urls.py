from django.urls import path
from . import views
from profil import views as vprofil
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('biodata', views.biodata, name="biodata"),
    path('biodata/update', views.updateBiodata, name="update_biodata"),
    path('nilai-mahasiswa', views.nilaiMahasiswa, name="nilai"),
    path('jadwal-kuliah', views.jadwalKuliah, name="jadwal"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
