class producto:
    def __init__(self, nombre, precio):
        while True:
            if precio <= 0:
                print("El precio no es valido")
            else:
                self.nombre = nombre
                self.precio = precio



class bebida(producto):
    def __init__(self, tamano_L, nombre, precio):
        while True:
            if precio <= 0:
                print("El precio no es valido")
            else:
                super().__init__(nombre, precio)
                self.tamano_L = tamano_L



class comida(producto):
    def __init__(self, guarnicion, nombre, precio, para_compartir = False):
        while True:   
            if precio <= 0:
                print("El precio no es valido")
            else:
                super().__init__(nombre, precio)
                self.guarnicion = guarnicion

