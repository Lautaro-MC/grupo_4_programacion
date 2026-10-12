from pedido import pedido


class cliente:

    def __init__(self, nombre, mesa):
        self.nombre = nombre
        self.mesa = mesa
        self.pedido = None

    def tomar_pedido(self, num_pedidio):
        self.pedido = pedido(num_pedidio)
        print(f"se creo el pedido {num_pedidio} para la mesa {self.mesa}")

    def calcular_pago(self):
        total = 0

        for producto in self.pedido.productos:
            total += producto.precio

        return total