from django.db import models
from caracteristicas.models import Caracteristica
from ckeditor.fields import RichTextField

# MODELO PARA DOCUMENTOS.
# CADA UNO DE LOS DOCUMENTOS ESTAN RELACIONADOS A SOLO UNA CARACTERÍSTICAS.
class Documento(models.Model):
    caracteristica = models.ForeignKey(Caracteristica, verbose_name="Caracteristica", on_delete=models.CASCADE)
    TIPO_CHOICES = (
        ('INDICADOR', 'INDICADOR'),
        ('NOMBRAMIENTO', 'NOMBRAMIENTO'),
        ('PROTOCOLO', 'PROTOCOLO')
    )
    tipo = models.CharField(verbose_name="Tipo de documento", choices=TIPO_CHOICES, max_length=20, null=True, blank=True)
    version =  models.FloatField(verbose_name="Versión de documento", null=True, blank=True)
    fecha_documento = models.DateField(verbose_name="Fecha documento")
    archivo = models.FileField(verbose_name='Archivo', null=True, blank=True, upload_to='documentos')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['fecha_documento']

