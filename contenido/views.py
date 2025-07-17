from django.shortcuts import render

def inicio(request):
    contexto = {
        'titulo': 'Bienvenido a CursosDjango',
        'mensaje': 'Aprende programación con nuestros cursos'
    }
    return render(request, 'inicio.html', contexto)

def cursos(request):
    lista_cursos = [
        {'nombre': 'Python Básico', 'categoria': 'Programación'},
        {'nombre': 'Django', 'categoria': 'Web'},
        {'nombre': 'SQL', 'categoria': 'Base de Datos'},
    ]
    return render(request, 'cursos.html', {'cursos': lista_cursos})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        print(f"Datos recibidos: {nombre}, {email}")
        
    return render(request, 'contacto.html')