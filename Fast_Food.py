class Pedido:
    def __init__(self, cliente, items):
        self.cliente = cliente
        self.items = items

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.precio
        return total

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Q.{self.precio:.2f}"

def tomar_pedido():
    cliente = input("Nombre del cliente: ")
    items = []

    while True:
        nombre = input("Nombre del producto (o 'f' para finalizar el pedido): ")
        if nombre.lower() == 'f':
            break
        precio = float(input("Precio del producto: "))
        producto = Producto(nombre, precio)
        items.append(producto)

    return Pedido(cliente, items)

def mostrar_pedido(pedido):
    print(f"Cliente: {pedido.cliente}")
    print("Productos en el pedido:")
    for item in pedido.items:
        print(f"  - {item}")

if __name__ == "__main__":
    pedidos = []

    while True:
        opcion = input("¿Desea tomar un nuevo pedido? (s/n): ")
        if opcion.lower() != 's':
            break
        pedido = tomar_pedido()
        pedidos.append(pedido)

    print("Resumen de pedidos:")
    for i, pedido in enumerate(pedidos,1):
        print(f"Pedido {i}:")
        mostrar_pedido(pedido)
        print(f"Total: Q.{pedido.calcular_total():.2f}")
        print()
        
