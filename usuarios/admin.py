from django.contrib import admin
from django.utils.html import format_html
from .models import Usuario, UsuarioType, Documento

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo', 'celular', 'instid')

@admin.register(UsuarioType)
class UsuarioTypeAdmin(admin.ModelAdmin):
    list_display = ('uid', 'tipo')

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('uid', 'tipo', 'archivo_link')

    def archivo_link(self, obj):
        if obj.url:
            if obj.url.url.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.url.url)
            else:
                return format_html('<a href="{}" target="_blank">Ver archivo</a>', obj.url.url)
        return "-"
    archivo_link.short_description = 'Archivo'
