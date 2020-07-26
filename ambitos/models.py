from django.db import models
from ckeditor.fields import RichTextField


class Ambito(models.Model):
    nombre = models.CharField(verbose_name='Nombre de Ámbito', max_length=100)
    descripcion = RichTextField(verbose_name='Description')
    sigla = models.CharField(verbose_name="Sigla", max_length=3, null=True, blank=True)
    numero = models.PositiveSmallIntegerField(verbose_name='Número de Ámbito')
    encargado = models.CharField(verbose_name='Encargado de Ámbito', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Ámbito'
        verbose_name_plural = 'Ámbitos'
        ordering = ['numero']

    def __str__(self):
        return self.nombre
