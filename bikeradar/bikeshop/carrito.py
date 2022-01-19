class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        totalCart = self.session.get("totalCart")
        if not cart:
            cart = self.session["cart"] = {}
            totalCart = self.session["totalCart"] = 0
        self.cart = cart
        self.totalCart = totalCart
        
    def add(self,producto,qty):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre" : producto.nombre,
                "categoria": producto.categoria.nombre,
                "marca": producto.marca.nombre,
                "cantidad" : qty,
                "precio": str(producto.precio),
                "imagen" : producto.imagen1.url,
                "total" : str(qty * producto.precio),
                "serie" : producto.serie,
                "peso" : str(producto.peso),
                "dimensiones" : producto.dimensiones,
                "color" : producto.color,
                "material" : producto.material,
                "fabricacion" : producto.fabricacion,
                }
        else:
            for key,value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = str(int(value["cantidad"]) + qty)
                    value["total"] = str(float(value["cantidad"]) * float(value["precio"]))
                    break
        self.save()
        
    def save(self):
        self.session["cart"] = self.cart
        total = 0

        for key,value in self.cart.items():           
            total = total + (float(value["cantidad"])) * float(value["precio"])
        self.session["totalCart"] = total
        self.session.modified = True

        
    def remove(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
            
    def clear(self):
        self.session["cart"] = {}
        self.session["totalCart"] = 0