from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def carrito_total(items):
    total = 0
    for item in items:
        total += item.cantidad * item.producto.precio
    return total



