
from django.contrib import admin
from django.urls import path, include
from contenido import views
from cursos import views as views_cursos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('cursos/', views_cursos.lista_cursos, name='cursos'),
    path('nuevo/', views_cursos.nuevo_curso, name='nuevo_curso'),
    path('editar/<int:id>/', views_cursos.editar_curso, name='editar_curso'),
    path('eliminar/<int:id>/', views_cursos.eliminar_curso, name='eliminar_curso'),
]