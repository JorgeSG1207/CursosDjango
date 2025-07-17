from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50, choices=[
        ('DB', 'Base de Datos'),
        ('PROG', 'Programación'),
        ('WEB', 'Desarrollo Web'),
        ('DS', 'Ciencia de Datos'),
    ])
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class SolicitudInformacion(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    comentarios = models.TextField()
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f"Solicitud de {self.nombre} sobre {self.curso.nombre}"