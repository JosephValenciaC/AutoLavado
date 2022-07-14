from typing import Sequence
from django.contrib import admin
from .models import Servicios

class AdministrarServicio(admin.ModelAdmin):
    readonly_fields: Sequence[str] = ('created', 'updated')
    
admin.site.register(Servicios, AdministrarServicio)