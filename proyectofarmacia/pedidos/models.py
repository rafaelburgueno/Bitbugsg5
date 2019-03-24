from datetime import datetime
from django.db import models


class Pedidos(models.Model):
    paciente = models.CharField(verbose_name="Paciente", max_length=200)
    cama = models.CharField(verbose_name="Cama", max_length=100)
    insumos = models.TextField(verbose_name="Insumos")
    solicitante = models.CharField(verbose_name="Solicitante", max_length=200)
    procesante = models.CharField(verbose_name="Procesante", max_length=200, blank=True)
    retirante = models.CharField(verbose_name="Retirante", max_length=200, blank=True)
    urgencia = models.CharField(verbose_name="Urgencia", max_length=100)
    estado = models.CharField(verbose_name="Estado", max_length=100, default='pendiente')
    id_modificado = models.CharField(verbose_name="modificado", max_length=50, default='no')
    
    created = models.CharField(verbose_name="Fecha de creación", max_length=100, blank=True, default=datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    fecha_procesamiento = models.CharField(verbose_name="Fecha de procesamiento", max_length=100, blank=True, default='0000')
    fecha_despachable = models.CharField(verbose_name="Fecha despachable", max_length=100, blank=True, default='0000')
    fecha_despacho = models.CharField(verbose_name="Fecha de despacho", max_length=100, blank=True, default='0000')

    class Meta:
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        # la siguiente linea le inciacomo se presentan los resultados, segun la urgencia y al momento de creacion
        ordering = ['-urgencia', 'created']

    def __str__(self):
        return self.insumos

    # metodo para dividir el string de insumos
    def insumos_as_list(self):
        return self.insumos.split(';')
    
    # metodo para actualizar la fecha
    #def actualizar_fecha(self):
        #return self.insumos.split(';')