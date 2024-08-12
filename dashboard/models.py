from django.contrib.auth.models import User
from django.db import models

class BiodataMahasiswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nik = models.CharField(max_length=100, unique=True)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    foto = models.ImageField(upload_to='templates/img', default='default.jpg')
    JENIS_KELAMIN_CHOICES = (
        ('laki-laki', 'Laki-laki'),
        ('perempuan', 'Perempuan')
    )
    jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)

    @property
    def nama(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.nama