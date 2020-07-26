from django.db import models
from ambitos.models import Ambito
from ckeditor.fields import RichTextField


class Caracteristica(models.Model):
    nombre = models.CharField(verbose_name='Nombre de Caracteristica', max_length=100)
    denominacion = models.CharField(verbose_name='Denomiación', max_length=250, null=True, blank=True)
    ambito = models.ForeignKey(Ambito, verbose_name="Ámbito", on_delete=models.CASCADE)
    descripcion = RichTextField(verbose_name='Description')
    TIPO_CHOICES = (
        ('OBLIGATORIA', 'OBLIGATORIA'),
        ('NO OBLIGATORIA', 'NO OBLIGATORIA')
    )
    tipo = models.CharField(verbose_name="Tipo de caracteristica", choices=TIPO_CHOICES, max_length=15, null=True, blank=True)
    numero = models.FloatField(verbose_name='Número de Característica')
    fecha = models.DateField(verbose_name='Fecha de documento', default='2018-11-13')
    encargado = models.CharField(verbose_name='Encargado de Caracteristica', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Característica'
        verbose_name_plural = 'Características'
        ordering = ['ambito', 'numero']

    def __str__(self):
        return self.nombre


