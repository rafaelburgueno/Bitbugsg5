from django.contrib import admin

from .models import Pedidos

# Register your models here.
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('urgencia', 'created','paciente','estado','insumos')

admin.site.register(Pedidos, PedidosAdmin)