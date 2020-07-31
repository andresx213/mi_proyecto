from django.shortcuts import render
from django.http import HttpResponse
from pedidos.models import Articulo
from django.core.mail import send_mail
from django.conf import settings
from pedidos.forms import formulario
# Create your views here.
def busqueda_productos(request):
    return render(request, "pedidos/busquedas.html") 

def buscar(request):
    if request.GET["prd"]:
        #mensaje="articulos buscado %r" %request.GET["prd"]  
        producto=request.GET["prd"]
        if len(producto)>20:
           
           mensaje="Texto de busqueda demaciado largo"

        else:

            articulos=Articulo.objects.filter(nombre__icontains=producto)

            return render(request, "pedidos/resultado.html",{"articulos":articulos, "query":producto})
   
    else:

        mensaje="no has introducido nada" 
        
    return HttpResponse(mensaje)

def contacto(request):

    if request.method=="POST":

        furmula=formulario(request.POST)

        if furmula.is_valid():

            info=furmula.cleaned_data

            send_mail(info['asunto'], info['mensaje'],
            info.get('email',''),['davidortegax213@gmail.com'],)

            return render(request,"pedidos/gracias.html")

    else:

        formula=formulario()
   
    return  render(request, "pedidos/fin.html",{"fz1":formula})            