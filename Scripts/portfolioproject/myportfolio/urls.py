from django.urls import path
from . import views
from .views import agregar_al_carrito, ver_carrito,checkout,incrementar_cantidad,disminuir_cantidad,eliminar_item

urlpatterns =[
    path('', views.index , name='index'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', ver_carrito, name='ver_carrito'),
    path('checkout/', checkout, name='checkout'),
    path('incrementar_cantidad/<int:item_id>/', incrementar_cantidad, name='incrementar_cantidad'),
    path('disminuir_cantidad/<int:item_id>/', disminuir_cantidad, name='disminuir_cantidad'),
    path('eliminar_item/<int:item_id>/', eliminar_item, name='eliminar_item'),
    path('checkout/', checkout, name='checkout'),
]   