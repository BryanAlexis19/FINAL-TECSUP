from django.shortcuts import redirect, render
from .models import Marca, Categoria, Producto, Comentario, FormaPago, Cliente, Pedido, PedidoDetalle 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .carrito import Cart
# Create your views here.

def index(request):
    lstCategorias = Categoria.objects.all()
    lstProductos = Producto.objects.all()
    
    context = {
        'categorias' : lstCategorias,
        'productos' : lstProductos,
    }

    return render(request, 'index.html', context)

def verProducto(request, producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    #objComentario = Comentario.objects.get(pk=objProducto.pk)
    context = {
        'producto' : objProducto,
        #'comentario' : objComentario
    }
    return render(request, 'verProducto.html', context)

def verProductoRapido(request, producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    #objComentario = Comentario.objects.get(pk=objProducto.pk)
    context = {
        'productoRapido' : objProducto,
        #'comentario' : objComentario
    }
    return render(request, 'verProducto.html', context)

def agregarItemAlCarrito(request, producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    cantidad = int(request.POST['cantidad'])
    carrito = Cart(request)
    carrito.add(objProducto,cantidad)
    print(request.session.get("cart"))
    return render(request, 'carrito.html')

def mostrarCarrito(request):
    return render(request,'carrito.html')

def eliminarProductoCarrito(request, producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    carrito = Cart(request)
    carrito.remove(objProducto)
    return render(request, 'carrito.html')

def limpiarCarrito(request):
    carrito = Cart()
    carrito.clear()
    return redirect('/carrito')

def loginUsuario(request):
    context = {}

    if request.method =='POST':
        dataUsuario = request.POST['usuario']
        dataClave = request.POST['clave']

        print(dataUsuario)

        loginUsuario = authenticate(request, username=dataUsuario, password=dataClave)
        if (loginUsuario):
            login(request, loginUsuario)
            return redirect('/')
        else:
            context = {
                'error' : 'datos incorrectos'
            }
    return render(request, 'loginUsuario.html', context)

def logoutUsuario(request):
    logout(request)
    return render(request, 'index.html')

def registroCliente(request):
    
    if request.method == 'POST':
        #Register new customer
        usuario = request.POST['usuario']
        clave = request.POST['clave']

        nuevoUsuario = User.objects.create_user(username=usuario, password=clave)

        nuevoUsuario.first_name = request.POST['nombre']
        nuevoUsuario.lasat_name = request.POST['apellido']
        nuevoUsuario.email = request.POST['email']

        nuevoUsuario.save()

        nuevoCliente = Cliente(usuario=nuevoUsuario)
        nuevoCliente.telefono = request.POST['telefono']
        nuevoCliente.save()

        return render(request, 'loginUsuario.html')
    
    return render(request, 'registroCliente.html')

def registrarPedido(request):
    if request.user.id is not None:
        usuarioPedido = User.objects.get(pk=request.user.id)
        clientePedido = Cliente.objects.get(usuario=usuarioPedido)
        lstFormasPago = FormaPago.objects.all()
        
        context = {
            'nombres': request.user.first_name,
            'apellidos': request.user.last_name,
            'telefono': clientePedido.telefono,
            'email': request.user.email,
            'formasPago': lstFormasPago
        }
    else:
        return redirect('/loginUsuario')
    
    return render(request, 'registrarPedido.html', context)

def confirmarPedido(request):
    #Save the order in the database
    usuarioPedido = User.objects.get(pk=request.user.id)
    clientePedido = Cliente.objects.get(usuario=usuarioPedido)
    dataFormaPagoId = request.POST['chkFormaPago']
    dataDireccion = request.POST['direccion']

    dataFormaPago = FormaPago.objects.get(pk = dataFormaPagoId)

    nuevoPedido = Pedido()
    nuevoPedido.cliente = clientePedido
    nuevoPedido.direccion = dataDireccion
    nuevoPedido.formaPago = dataFormaPago
    nuevoPedido.totalPagar = float(request.session.get("totalCart"))
    nuevoPedido.montoPago = 0
    nuevoPedido.save()

    #Register order details
    carritoPedido = request.session.get("cart")
    for key, value in carritoPedido.items():
        nuevoDetalle = PedidoDetalle()
        nuevoDetalle.pedido = nuevoPedido
        nuevoDetalle.cantidad = int(value["cantidad"])
        nuevoDetalle.precio = float(value["precio"])

        detalleProducto = Producto.objects.get(pk=value["producto_id"])

        nuevoDetalle.producto = detalleProducto
        nuevoDetalle.save()

    carrito = Cart(request)
    carrito.clear()
    return render(request, 'gracias.html')

def gracias(request):
    return render(request, 'gracias.html')


