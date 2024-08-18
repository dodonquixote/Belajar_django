from django.contrib import admin
from dashboard.models import *

# Register your models here.
@admin.register(BiodataMahasiswa)
class BiodataMahasiswaAdmin(admin.ModelAdmin):
    list_display=['user']

@admin.register(JadwalKuliah)
class JadwalKuliahAdmin(admin.ModelAdmin):
    list_display=['matkul']

@admin.register(NilaiMahasiswa)
class NilaiMahasiswaAdmin(admin.ModelAdmin):
    list_display=['user', 'matkul']

@admin.register(MataKuliah)
class MataKuliahAdmin(admin.ModelAdmin):
    list_display=['matkul']