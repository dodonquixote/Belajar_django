from django.contrib import admin
from profil.models import *

# Register your models here.
@admin.register(DataMahasiswa)
class DataMahasiswaAdmin(admin.ModelAdmin):
    list_display=['user']

@admin.register(ProfilMahasiswa)
class DataMahasiswaAdmin(admin.ModelAdmin):
    list_display=['user']