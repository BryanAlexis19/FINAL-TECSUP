from django.urls import path
from . import views

# URL patterns for the bikeshop app

app_name = 'bikeshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('verProducto/<int:producto_id>', views.verProducto, name="verProducto"),
    path('verProductoRapido/<int:producto_id>', views.verProductoRapido, name="verProductoRapido"),
    path('agregarItemAlCarrito/<int:producto_id>', views.agregarItemAlCarrito, name="agregarItemAlCarrito"),
    path('mostrarCarrito', views.mostrarCarrito, name="mostrarCarrito"),
    path('elimiarProductoCarrito/<int:producto_id>', views.eliminarProductoCarrito, name="eliminarProductoCarrito"),
    path('limpiarCarrito', views.limpiarCarrito, name="limpiarCarrito"),
    path('loginUsuario', views.loginUsuario, name="loginUsuario"),
    path('logoutUsuario', views.logoutUsuario, name="logoutUsuario"),
    path('registroCliente', views.registroCliente, name="registroCliente"),
    path('registrarPedido', views.registrarPedido, name="registrarPedido"),
    path('confirmarPedido', views.confirmarPedido, name="confirmarPedido"),
    path('gracias', views.gracias, name="gracias"),
    # MIS VIEWS PARA NUTRISAN
    #----------------------------------------------------PACIENTE----------------------------------------------------
    path('registrarPaciente', views.registrarPaciente, name="registrarPaciente"),
    path('actualizarPaciente', views.actualizarPaciente, name="actualizarPaciente"),
    path('buscarPaciente', views.buscarPaciente, name="buscarPaciente"),
    #----------------------------------------------------DIAGNOSTICO-------------------------------------------------
    path('registrarDiagnostico', views.registrarDiagnostico, name="registrarDiagnostico"),
    path('actualizarDiagnostico', views.actualizarDiagnostico, name="actualizarDiagnostico"),
    path('verDiagnosticos', views.verDiagnosticos, name="verDiagnosticos"),
    #----------------------------------------------------ALIMENTO---------------------------------------------------
    path('verAlimentos', views.verAlimentos, name="verAlimentos"),
    path('registrarAlimento', views.registrarAlimento, name="registrarAlimento"),
    path('actualizarAlimento', views.actualizarAlimento, name="actualizarAlimento"),

        
]

