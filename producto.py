class producto:
    def __init__(self, nombre, precio):
            while precio <= 0:
                print("El precio no es valido")
                precio = float(input("ingrese un precio valido"))
            self.nombre = nombre
            self.precio = precio



class bebida(producto):
    def __init__(self, tamano_L, nombre, precio):
            super().__init__(nombre, precio)
            self.tamano_L = tamano_L



class comida(producto):
    def __init__(self, nombre, precio, guarnicion, para_compartir): 
            super().__init__(nombre, precio)
            self.guarnicion = guarnicion
            self.para_compartir = para_compartir
