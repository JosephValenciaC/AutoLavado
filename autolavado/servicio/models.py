from django.db import models

class Servicios(models.Model):
    id = models.AutoField(primary_key=True)
    clave = models.CharField(max_length=20)
    nombreCliente = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    TipServ = models.CharField(max_length=200, verbose_name='Tipo de servicio')
    costo = models.IntegerField()
    FechaSer = models.CharField(max_length=20, verbose_name='Fecha del servicio')
    imagen = models.ImageField(null=True, upload_to='fotos', verbose_name='Imagen del servicio')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']
        
    def __str__(self):
        return self.nombreCliente