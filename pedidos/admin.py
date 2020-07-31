from django.contrib import admin
from pedidos.models import Cliente,Articulo,pedido
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion","telefono")
    search_fields=("nombre","direccion","telefono")
class ArticuloAdmin(admin.ModelAdmin):
    list_filter=("seccion","precio")  

class pedidoAdmin(admin.ModelAdmin):
    list_display=("numero","fecha") 
    list_filter=("fecha",)
    date_hierarchy="fecha"
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(pedido,pedidoAdmin)
