from django.db import models
from caracteristicas.models import Caracteristica

# Create your models here.
class Indicador(models.Model):
    nombre = models.CharField(verbose_name='Nombre de indicador', null=True, blank=True)
    caracteristica = models.ForeignKey(Caracteristica, verbose_name='Característica', on_delete=models.CASCADE)
    version = models.FloatField(verbose_name='Versión')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'
        ordering = ['nombre']
