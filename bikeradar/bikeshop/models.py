from django.db import models
from django.db.models.deletion import RESTRICT
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    portada = CloudinaryField('Portada', default="", blank=True, null=True)
    logo = CloudinaryField('Logo', default="", blank=True, null=True)
    telefono = models.CharField(max_length=50, default='')


    def __str__(self):
        return self.nombre

    ''' class Meta:
        verbose_name_plural = "Negocio" '''


#Categoria del producto: /Lubricantes-mtb-ruta-bmx-cascos-guantes-etc/
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = CloudinaryField('imagen', default="", blank=True, null=True)

    def __str__(self):
        return self.nombre

    ''' class Meta:
        verbose_name_plural = "Categoria" '''


class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    nombre = CharField(max_length=200)
    imagen1 = CloudinaryField('Imagen 1', default="") # 290 x 258
    imagen2 = CloudinaryField('Imagen 2 (optional)', default="", blank=True, null=True) # 550 x 490
    imagen22 = CloudinaryField('Imagen 22 (optional)', default="", blank=True, null=True)
    imagen3 = CloudinaryField('Imagen 3 (optional)', default="", blank=True, null=True) # 550 x 550
    imagen33 = CloudinaryField('Imagen 33 (optional)', default="", blank=True, null=True)
    videourl = models. URLField(max_length=200, default="", blank=True, null=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    serie = models.CharField(max_length=200, default="", blank=True, null=True)
    peso = models.DecimalField(max_digits=9, decimal_places=2, default=0, blank=True, null=True)
    dimensiones = models.CharField(max_length=200, default="", blank=True, null=True)
    color = models.CharField(max_length=200, default="", blank=True, null=True)
    material = models.CharField(max_length=200, default="", blank=True, null=True)
    fabricacion = models.CharField(max_length=200, default="", blank=True, null=True)

    def __str__(self):
        return self.marca.nombre + " " + self.nombre

    ''' class Meta:
        verbose_name_plural = "Plato" '''

class Cliente(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT)
    telefono = models.CharField(max_length=20)


    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Comentario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    estrellas = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.producto.nombre + " por " + self.cliente.usuario.first_name


class FormaPago(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.RESTRICT)
    direccion = models.CharField(max_length=200)
    fechaHora = models.DateTimeField(auto_now=True)
    formaPago = models.ForeignKey(FormaPago,on_delete=models.RESTRICT)
    totalPagar = models.DecimalField(max_digits=9,decimal_places=2)
    montoPago = models.DecimalField(max_digits=20,decimal_places=2)

    def __str__(self):
        return self.direccion 

class PedidoDetalle(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto,on_delete=models.RESTRICT)
    precio = models.DecimalField(max_digits=9,decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return self.producto.nombre
