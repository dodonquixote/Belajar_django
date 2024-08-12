from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import BiodataMahasiswa

@receiver(post_save, sender=User)
def create_user_related_data(sender, instance, created, **kwargs):
    if created:
        # membuat Biodata Mahasiswa ketika User baru dibuat
        BiodataMahasiswa.objects.create(user=instance)

