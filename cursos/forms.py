from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'imagen', 'precio', 'duracion', 'nivel', 'disponible']
