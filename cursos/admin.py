from django.contrib import admin
from .models import Curso, Actividad

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'precio', 'duracion', 'disponible', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('nivel', 'disponible', 'fecha_creacion')
    list_editable = ('precio', 'disponible')
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'imagen')
        }),
        ('Detalles del Curso', {
            'fields': ('precio', 'duracion', 'nivel', 'disponible')
        }),
        ('Información Automática', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)
        }),
    )
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'nombre':
            field.label = 'Título del Curso'
        elif db_field.name == 'descripcion':
            field.label = 'Descripción Completa'
        return field

admin.site.register(Curso, CursoAdmin)

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('clave', 'nombre', 'curso', 'fecha_creacion')
    list_filter = ('curso',)
    search_fields = ('clave', 'nombre', 'descripcion')
    fieldsets = (
        ('Información Básica', {
            'fields': ('clave', 'curso', 'nombre')
        }),
        ('Descripción', {
            'fields': ('descripcion',),
            'description': 'Ingresa todos los detalles de la actividad'
        }),
    )
    
admin.site.register(Actividad, ActividadAdmin)  
