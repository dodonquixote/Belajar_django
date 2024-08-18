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
    
class MataKuliah(models.Model):
    matkul = models.CharField(max_length=50)
    dosen = models.CharField(max_length=50)
    
    SKS_MATKUL = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    sks = models.CharField(max_length=2, choices=SKS_MATKUL)

    def __str__(self):
        return self.matkul

class NilaiMahasiswa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    matkul = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)

    NILAI_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]
    nilai_huruf = models.CharField(max_length=1, choices=NILAI_CHOICES)

    @property
    def mutu_nilai(self):
        mutu_mapping = {
            'A': 4,
            'B': 3,
            'C': 2,
            'D': 1,
            'E': 0,
        }
        return mutu_mapping.get(self.nilai_huruf, 0)
    
    @property
    def nilai_mutu(self):
        return int(self.matkul.sks) * self.mutu_nilai
    
    @staticmethod
    def total_sks(user):
        return sum(int(n.matkul.sks) for n in NilaiMahasiswa.objects.filter(user=user))

    @staticmethod
    def total_mutu(user):
        return sum(n.nilai_mutu for n in NilaiMahasiswa.objects.filter(user=user))

    @staticmethod
    def ipk(user):
        total_sks = NilaiMahasiswa.total_sks(user)
        if total_sks == 0:
            return 0
        total_mutu = NilaiMahasiswa.total_mutu(user)
        return round(total_mutu / total_sks, 2)


    
    def __str__(self):
        return f"{self.user.username} - {self.matkul}: {self.nilai_huruf} ({self.mutu_nilai})"

class JadwalKuliah(models.Model):
    matkul = models.OneToOneField(MataKuliah, on_delete=models.CASCADE)
    
    HARI_CHOICES = [
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', "Jumat"),
        ('sabtu', 'Sabtu'),
        ('minggu', 'Minggu'),
    ]
    hari = models.CharField(max_length=10, choices=HARI_CHOICES)
    jam = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.matkul} - {self.hari} at {self.jam}"


