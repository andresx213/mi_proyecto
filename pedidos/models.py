from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True,null=True)
    telefono=models.CharField(max_length=10)
    def __str__(self):
        return self.nombre
class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=19)
    precio=models.IntegerField()
    def __str__(self):
        return 'el nombre es %s la seccion es %s y el precio es %s'%(self.nombre,self.seccion,self.precio)

class pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
       