if __name__ == "__main__":

    class Producto:
        def __init__(self,nombre,precio,cantidad) -> None:
            self.nombre = nombre
            self.precio = precio
            self.cantidad = cantidad
        
class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_productos(self,producto):
        self.productos.append(producto)

    def mostrar_producto(self):
        for producto in self.productos:
            print("Nombre: ",producto.nombre)
            print("Precio: ",producto.precio)
            print("Cantidad: ",producto.cantidad)
            print("------------------------------")

catalogo = Catalogo()

P1 = Producto("cables",25,15)
P2 = Producto("destornilladores",10,25)
P3 = Producto("tornillos",15,150)
P4 = Producto("llantas",34,10)

catalogo.agregar_productos(P1)
catalogo.agregar_productos(P2)
catalogo.agregar_productos(P3)
catalogo.agregar_productos(P4)

catalogo.mostrar_producto()