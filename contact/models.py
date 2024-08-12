from django.db import models

class ContactMassage(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)  # Use EmailField for email addresses
    pesan = models.CharField(max_length=500)

    def __str__(self):
        return self.nama  # Optional: to make it easier to identify instances
