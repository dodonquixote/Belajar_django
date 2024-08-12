from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import DataMahasiswa, ProfilMahasiswa

@receiver(post_save, sender=User)
def create_user_related_data(sender, instance, created, **kwargs):
    if created:
        # membuat DataMahasiswa and ProfilMahasiswa ketika User baru dibuat
        DataMahasiswa.objects.create(user=instance)
        ProfilMahasiswa.objects.create(user=instance)

