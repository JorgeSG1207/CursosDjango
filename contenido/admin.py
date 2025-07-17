from django.contrib import admin
from .models import Curso, SolicitudInformacion

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'descripcion')

@admin.register(SolicitudInformacion)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'curso', 'fecha_solicitud', 'atendido')
    list_filter = ('atendido', 'curso')
    search_fields = ('nombre', 'email', 'comentarios')