from producto import producto, bebida, comida
from pedido import pedido
from cliente import cliente

agua = bebida(0.5, "agua_Villavicencio", 1500)

lomito = comida("lomito_clasico", 25000, "papas fritas", False)

cliente1 = cliente("Isabel", 22)
print()
cliente1.tomar_pedido(1)
print()
cliente1.pedido.agregar_producto(agua)
print()
cliente1.pedido.agregar_producto(lomito)
print()
cliente1.pedido.mostrar_pedido()
print(f"total: {cliente1.calcular_pago()}")
print()
cliente1.pedido.sacar_producto(agua)
print()
cliente1.pedido.mostrar_pedido()
print(f"total: {cliente1.calcular_pago()}")

cliente1.pedido.sacar_producto("fideos")

