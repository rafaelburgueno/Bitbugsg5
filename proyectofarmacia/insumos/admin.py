from django.contrib import admin
from .models import Insumo

# Register your models here.
class InsumoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Insumo, InsumoAdmin)