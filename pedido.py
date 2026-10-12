from producto import producto, bebida, comida


class pedido:
    def __init__(self, num_pedido):
        self.num_pedido = num_pedido
        self.productos = []


    def agregar_producto(self, producto):
        disponible = input(f"el producto {producto.nombre} esta disponible? s/n: ")
        if disponible == "s":
            self.productos.append(producto)
            print("el producto se ha agregado")
        else: 
            print("el producto no esta disponible")


    def sacar_producto(self, producto):
        if producto not in self.productos:
            print(f"el producto {producto} no estaba en el pedido")
        else:
            self.productos.remove(producto)
            print(f"el producto {producto.nombre} se ha eliminado del pedido")


    def mostrar_pedido(self):
        print("========================")
        print("        PEDIDO")
        print("========================")

        if not self.productos:
            print("El pedido está vacío")
        else:
            for producto in self.productos:
                print(f"- {producto.nombre}")

        print("========================")

