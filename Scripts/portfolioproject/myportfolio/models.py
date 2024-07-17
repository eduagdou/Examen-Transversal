from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')

def __str__(self):
    return f'{self.titulo}->{self.precio}'
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='CarritoItem')

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.cantidad} x {self.producto.titulo}'
    




