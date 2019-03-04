from django.db import models

# Create your models here.
class Insumo(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    stock = models.SmallIntegerField(verbose_name="Stock", default=9)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "insumo"
        verbose_name_plural = "insumos"
        
        ordering = ['nombre']

    def __str__(self):
        return self.nombre