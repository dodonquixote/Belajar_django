# Generated by Django 5.0.6 on 2024-08-10 04:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BiodataMahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=100, unique=True)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tanggal_lahir', models.DateField()),
                ('jenis_kelamin', models.CharField(choices=[('laki-laki', 'Laki-laki'), ('perempuan', 'Perempuan')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]