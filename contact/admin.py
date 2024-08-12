from django.contrib import admin
from .models import ContactMassage

@admin.register(ContactMassage)
class ContactMassageAdmin(admin.ModelAdmin):
    list_display=['nama']
