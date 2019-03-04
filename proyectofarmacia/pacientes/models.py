from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    cama = models.CharField(max_length=5, verbose_name="Cama")
    condicion = models.CharField(max_length=50, verbose_name="Condicion")
    dolencia = models.CharField(max_length=200, verbose_name="Dolencia")
    medico = models.CharField(max_length=200, verbose_name="Medico")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "paciente"
        verbose_name_plural = "pacientes"
        # la siguiente linea le inciacomo se presentan los resultados, segun la urgencia y al momento de creacion
        ordering = ['nombre']

    def __str__(self):
        return self.cama + ' - ' + self.nombre