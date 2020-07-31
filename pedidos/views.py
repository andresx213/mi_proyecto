from django.shortcuts import render
from django.http import HttpResponse
from pedidos.models import Articulo
# Create your views here.
def busqueda_productos(request):
    return render(request, "pedidos/busquedas.html") 

def buscar(request):
    if request.GET["prd"]:
        #mensaje="articulos buscado %r" %request.GET["prd"]  
        producto=request.GET["prd"]
        articulos=Articulo.objects.filter(nombre__icontains=producto)
        return render(request, "pedidos/resultado.html",{"articulos":articulos, "query":producto})

    else:
        mensaje="no has introducido nada" 
        
    return HttpResponse(mensaje)