if __name__ == "__main__":

    class Producto:
        def __init__(self, nombre, codigo):
            self.nombre = nombre
            self.codigo = codigo

    def __str__(self):
        return "Producto: {}, Código: {}".format(self.nombre,self.codigo)
    
    def obtener_origen(self):
        return self.codigo.split("-")[0]

    def obtener_numero_lote(self):
        return self.codigo.split("-")[1]

p = Producto("Nombre del producto", "PERU-0001-2023")
print(p) 
print("País de origen: ",p.obtener_origen())
print("Numero de lote: ",p.obtener_numero_lote())
