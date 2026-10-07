from pedido import pedido


class cliente:

    def __init__(self, nombre, mesa):
        self.nombre = nombre
        self.mesa = mesa
        self.pedido = pedido()

    def tomar_pedido(self, producto):
        self.pedido.agregar_producto(producto)

    def calcular_pago(self):
        total = 0

        for producto in self.pedido.productos:
            total += producto.precio

        return total