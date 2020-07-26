from django.contrib import admin
from .models import Documento

# Register your models here.
class DocumentoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('tipo', 'version', 'fecha_documento', 'archivo')
    readonly_fields = ('created', 'updated')

admin.site.register(Documento, DocumentoAdmin)