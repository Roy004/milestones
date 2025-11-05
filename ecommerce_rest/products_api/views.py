from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request):
    '''
    Vista de bienvenida
    '''
    return HttpResponse('<h1>Bienvenido a la tienda.</h1>')

def listar_productos(request):
    from .models import Producto
    productos=Producto.objects.all()

    contexto={
        'productos': productos,
        'titulo': 'Listado de productos',
    }

    return render(request, 'listar_productos.html', contexto)

# Create your views here.
