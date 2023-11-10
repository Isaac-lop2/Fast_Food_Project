class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock -= cantidad

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def agregar_item(self, producto, cantidad):
        self.items.append({'producto': producto, 'cantidad': cantidad})

class Restaurante:
    def __init__(self):
        self.inventario = {}
        self.cola_pedidos = []

    def agregar_producto(self, nombre, stock):
        if nombre in self.inventario:
            self.inventario[nombre].stock += stock
        else:
            producto = Producto(nombre, stock)
            self.inventario[nombre] = producto

    def tomar_pedido(self, cliente, pedido_items):
        pedido = Pedido(cliente)
        for item in pedido_items:
            nombre_producto, cantidad = item
            if nombre_producto in self.inventario and self.inventario[nombre_producto].stock >= cantidad:
                pedido.agregar_item(nombre_producto, cantidad)
                self.inventario[nombre_producto].actualizar_stock(cantidad)
            else:
                print(f"Producto '{nombre_producto}' no disponible en stock.")

        self.cola_pedidos.append(pedido)

    def mostrar_cola_pedidos(self):
        print("Cola de Pedidos:")
        for i, pedido in enumerate(self.cola_pedidos):
            print(f"Pedido {i + 1} - Cliente: {pedido.cliente}")
            for item in pedido.items:
                print(f"  - Producto: {item['producto']}, Cantidad: {item['cantidad']}")

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar producto al inventario")
    print("2. Tomar un pedido")
    print("3. Mostrar cola de pedidos")
    print("4. Salir")

if __name__ == "__main__":
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            stock_producto = int(input("Ingrese la cantidad en stock: "))
            restaurante.agregar_producto(nombre_producto, stock_producto)
            print(f"{nombre_producto} agregado al inventario.")
        elif opcion == "2":
            cliente = input("Ingrese el nombre del cliente: ")
            pedido_items = []
            while True:
                nombre_producto = input("Ingrese el nombre del producto (o 'f' para terminar): ")
                if nombre_producto == 'f':
                    break
                cantidad = int(input("Ingrese la cantidad: "))
                pedido_items.append((nombre_producto, cantidad))
            restaurante.tomar_pedido(cliente, pedido_items)
        elif opcion == "3":
            restaurante.mostrar_cola_pedidos()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
