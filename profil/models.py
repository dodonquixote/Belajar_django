from django.db import models

from django.contrib.auth.models import User
from django.db import models

class DataMahasiswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kelas = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=100)

    @property
    def nama(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.nama
    
class ProfilMahasiswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    nomor = models.CharField(max_length=100)
    alamat = models.CharField(max_length=100)

    @property
    def nama(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.nama