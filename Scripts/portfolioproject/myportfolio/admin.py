from django.contrib import admin
from .models import Producto,Carrito,CarritoItem
# Register your models here.
admin.site.register(Producto)
admin.site.register(CarritoItem)
admin.site.register(Carrito)
