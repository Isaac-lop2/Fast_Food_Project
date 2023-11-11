class Producto:
    def __init__(self, nombre, stock, precio):
        self.nombre = nombre
        self.stock = stock
        self.precio = precio

    def actualizar_stock(self, cantidad):
        self.stock -= cantidad


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.total = 0

    def agregar_item(self, producto, cantidad):
        self.items.append({'producto': producto, 'cantidad': cantidad})
        self.total += producto.precio * cantidad


class Restaurante:
    def __init__(self):
        self.inventario = {}
        self.cola_pedidos = []
        self.clientes = {}

    def agregar_producto(self, nombre, stock, precio):
        if nombre in self.inventario:
            self.inventario[nombre].stock += stock
        else:
            producto = Producto(nombre, stock, precio)
            self.inventario[nombre] = producto

    def tomar_pedido(self, cliente_nombre, pedido_items):
        if cliente_nombre not in self.clientes:
            self.clientes[cliente_nombre] = {'nombre': '','email': '', 'edad': '', 'dpi': '', 'nit': ''}

        cliente = self.clientes[cliente_nombre]

        pedido = Pedido(cliente)
        for item in pedido_items:
            nombre_producto, cantidad = item
            if nombre_producto in self.inventario and self.inventario[nombre_producto].stock >= cantidad:
                pedido.agregar_item(self.inventario[nombre_producto], cantidad)
                self.inventario[nombre_producto].actualizar_stock(cantidad)
            else:
                print(f"Producto '{nombre_producto}' no disponible en stock.")

        self.cola_pedidos.append(pedido)

    def mostrar_cola_pedidos(self):
        if not self.cola_pedidos:
            print("No hay pedidos en la cola.")
        else:
            print("Cola de Pedidos:")
            for i, pedido in enumerate(self.cola_pedidos):
                print(f"Pedido {i + 1} - Cliente: {pedido.cliente['nombre']}")
                for item in pedido.items:
                    print(f"  - Producto: {item['producto'].nombre}, Cantidad: {item['cantidad']}, Precio: Q{item['producto'].precio}")
                print(f"  - Total: Q{pedido.total}")
            print("======================")


    def generar_factura(self, cliente_nombre, pedido, metodo_pago):
        print("\n======= Factura =======")
        print(f"Cliente: {cliente_nombre}")
        print(f"Correo electrónico: {self.clientes[cliente_nombre]['email']}")
        print(f"Nit: {self.clientes[cliente_nombre]['nit']}")
        print(f"Tipo de pago: {metodo_pago.lower()}")
        print("\nDetalle de la orden:")

        for item in pedido.items:
            print(f"{item['producto'].nombre}: Q{item['producto'].precio} x {item['cantidad']} = Q{item['producto'].precio * item['cantidad']}")

        print(f"\nTotal a pagar: Q{pedido.total}")
        print("======================")

    def agregar_cliente(self, nombre, email, edad, dpi, nit):
        if nombre not in self.clientes:
            self.clientes[nombre] = {'nombre': nombre,'email': email, 'edad': edad, 'dpi': dpi, 'nit': nit}
        else:
            print("¡Error! Cliente ya registrado.")

    def mostrar_menu(self):
        print("\n======= Menú del Restaurante =======")
        for producto in self.inventario.values():
            print(f"{producto.nombre}: Q{producto.precio}")
        print("===================================")


def mostrar_menu_principal():
    print("\nMenú Principal:")
    print("1. Agregar producto al inventario")
    print("2. Tomar un pedido")
    print("3. Mostrar cola de pedidos")
    print("4. Generar factura")
    print("5. Agregar cliente")
    print("6. Mostrar Menú")
    print("7. Salir")


if __name__ == "__main__":
    restaurante = Restaurante()

    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            stock_producto = int(input("Ingrese la cantidad en stock: "))
            precio_producto = float(input("Ingrese el precio del producto: "))
            restaurante.agregar_producto(nombre_producto, stock_producto, precio_producto)
            print(f"{nombre_producto} agregado al inventario.")
        elif opcion == "2":
            cliente_nombre = input("Ingrese el nombre del cliente: ")
            if cliente_nombre not in restaurante.clientes:
                print("¡Error! Cliente no registrado. Por favor, registre al cliente primero.")
            else:
                pedido_items = []
                while True:
                    nombre_producto = input("Ingrese el nombre del producto (o 'f' para terminar): ")
                    if nombre_producto == 'f':
                        break
                    cantidad = int(input("Ingrese la cantidad: "))
                    pedido_items.append((nombre_producto, cantidad))
                restaurante.tomar_pedido(cliente_nombre, pedido_items)
        elif opcion == "3":
            restaurante.mostrar_cola_pedidos()
        
        elif opcion == "4":
            cliente_nombre = input("Ingrese el nombre del cliente: ")
            if cliente_nombre not in restaurante.clientes:
                print("¡Error! Cliente no registrado. Por favor, registre al cliente primero.")
            else:
                if restaurante.cola_pedidos:
                    pedido = restaurante.cola_pedidos[0]
                    restaurante.mostrar_cola_pedidos()
                    metodo_pago = input("¿Desea pagar en efectivo o con tarjeta? ")
                    if metodo_pago.lower() == "efectivo":
                        print("Gracias por su pago en efectivo.")
                    elif metodo_pago.lower() == "tarjeta":
                        input("Ingrese el nombre del titular de la tarjeta: ")
                        input("Ingrese el número de la tarjeta: ")
                        input("Ingrese el código CVV: ")
                        print("Gracias por su pago con tarjeta.")
                    else:
                        print("Método de pago no válido.")

                    print(f"\nGenerando factura para el cliente {cliente_nombre}")
                    restaurante.generar_factura(cliente_nombre, pedido, metodo_pago)
                    restaurante.cola_pedidos.pop(0)
                else:
                    print("No hay pedidos pendientes.")

        elif opcion == "5":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            email_cliente = input("Ingrese el correo electrónico: ")
            edad_cliente = input("Ingrese la edad: ")
            dpi_cliente = input("Ingrese el DPI: ")
            nit_cliente = input("Ingrese el NIT: ")

            restaurante.agregar_cliente(nombre_cliente, email_cliente, edad_cliente, dpi_cliente, nit_cliente)
            print(f"Cliente {nombre_cliente} registrado exitosamente.")
        elif opcion == "6":
            restaurante.mostrar_menu()
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

