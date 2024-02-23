from django.contrib import admin
from .models import *


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', "name", 'phone']
    list_display_links = ["name", 'phone']
    ordering = ['id']

