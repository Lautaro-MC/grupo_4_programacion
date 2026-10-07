from producto import producto


class pedido:
    def __init__(self, productos, producto):
        productos = []


    def agregar_producto(self, producto, productos):
        disponible = input("el producto esta disponible? s/n: ")
        if disponible == "s":
            productos.append(producto)
            print("el producto se ha agregado")
        else: 
            print("el producto no esta disponible")


    def sacar_producto(self, producto, productos):
        if producto not in productos:
            print("el producto no estaba en el pedido")
        else:
            productos.remove(producto)

