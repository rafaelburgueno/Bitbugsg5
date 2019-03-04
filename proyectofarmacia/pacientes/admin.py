from django.contrib import admin
from .models import Paciente

# Register your models here.
class PacienteAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Paciente, PacienteAdmin)