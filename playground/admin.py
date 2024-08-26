
# Register your models here.

from django.contrib import admin
from .models import diagnose

@admin.register(diagnose)
class diagnoseAdmin(admin.ModelAdmin):
    list_display = ('filename', 'images', 'labels', 'create_time')