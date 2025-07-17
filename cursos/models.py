from django.db import models
from django.utils import timezone

class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso', max_length=100)
    descripcion = models.TextField('Descripción')
    precio = models.DecimalField('Precio', max_digits=6, decimal_places=2)
    duracion = models.IntegerField('Duración (horas)')
    disponible = models.BooleanField('Disponible', default=True)
    nivel = models.CharField('Nivel', max_length=20, choices=[
        ('B', 'Básico'),
        ('I', 'Intermedio'),
        ('A', 'Avanzado')
    ])
    imagen = models.ImageField('Imagen del Curso', upload_to='cursos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField('Fecha de Creación', default=timezone.now)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Convocatoria'  
        verbose_name_plural = 'Convocatorias'  
        ordering = ['fecha_creacion'] 