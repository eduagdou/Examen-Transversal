from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito, CarritoItem
def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    return render(request, 'ver_carrito.html', {'items': items})

def checkout(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    total = sum(item.cantidad * item.producto.precio for item in items)
    return render(request, 'checkout.html', {'items': items, 'total': total})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = CarritoItem.objects.filter(carrito=carrito)
    return render(request, 'ver_carrito.html', {'items': items})

def incrementar_cantidad(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)
    item.cantidad += 1
    item.save()
    return redirect('ver_carrito')

def disminuir_cantidad(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)
    if item.cantidad > 1:
        item.cantidad -= 1
        item.save()
    else:
        item.delete()
    return redirect('ver_carrito')

def eliminar_item(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)
    item.delete()
    return redirect('ver_carrito')
