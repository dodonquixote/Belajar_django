# Generated by Django 5.0.6 on 2024-08-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmassage',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
