from django.contrib import admin
from .models import Marca, Categoria, Producto, Comentario, FormaPago, Cliente, Pedido, PedidoDetalle 

# Register your models here.

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(FormaPago)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(PedidoDetalle)