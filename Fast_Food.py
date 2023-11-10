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

class ElementoMenu:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.siguiente = None

class MenuRestaurante:
    def __init__(self):
        self.inicio = None

    def agregar_elemento(self, nombre, precio):
        nuevo_elemento = ElementoMenu(nombre, precio)
        if self.inicio is None:
            self.inicio = nuevo_elemento
        else:
            actual = self.inicio
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_elemento

    def mostrar_menu(self):
        actual = self.inicio
        print("\n======= Menú del Restaurante =======")
        while actual:
            print(f"{actual.nombre}: Q{actual.precio}")
            actual = actual.siguiente
        print("===================================")

    def ordenar_menu(self):
        if self.inicio is None or self.inicio.siguiente is None:
            return

        cambiado = True
        while cambiado:
            actual = self.inicio
            cambiado = False

            while actual.siguiente:
                if actual.precio > actual.siguiente.precio:
                    actual.precio, actual.siguiente.precio = actual.siguiente.precio, actual.precio
                    actual.nombre, actual.siguiente.nombre = actual.siguiente.nombre, actual.nombre
                    cambiado = True
                actual = actual.siguiente

def ingresar_menu():
    menu = MenuRestaurante()
    
    print("¡Bienvenido a la creación del Menú del Restaurante!")

    while True:
        nombre = input("Ingrese el nombre del elemento del menú (Comida, Bebida, Postres) (o 'q' si ya termino de agregar cosas al menu) \nIngrese su opción: ")
        if nombre.lower() == 'q':
            break

        precio = float(input(f"Ingrese el precio de {nombre}: "))
        menu.agregar_elemento(nombre, precio)
    menu.ordenar_menu()
    return menu

def hacer_pedido(menu):
    while True:
        menu.mostrar_menu()

        print("\nRegistro de cliente")
        nombre_cliente = input("\nIngrese su nombre (o 'q' para salir): ")
        if nombre_cliente.lower() == 'q':
            break

        email_cliente = input("Ingrese su correo electrónico: ")
        edad_cliente = input("Ingrese su edad: ")
        dpi_cliente = input("Ingrese su DPI: ")
        nit_cliente = input("Ingrese su NIT: ")

        class Cliente:
            def __init__(self, nombre, email, edad, dpi, nit):
                self.nombre = nombre
                self.email = email
                self.edad = edad
                self.dpi = dpi
                self.nit = nit

        class Pedido:
            def __init__(self):
                self.elementos = []

            def agregar_elemento(self, elemento):
                self.elementos.append(elemento)

            def calcular_total(self):
                total = 0
                for elemento in self.elementos:
                    total += elemento.precio
                return total

        cliente = Cliente(nombre_cliente, email_cliente, edad_cliente, dpi_cliente, nit_cliente)

        pedido = Pedido()
        while True:
            eleccion = input("\n¿Qué desea ordenar segun el menu? (Ingrese 'q' si desea terminar de ordenar o 's' para salir): ")
            if eleccion.lower() == 'q':
                break
            elif eleccion.lower() == 's':
                break
            else:
                elemento = menu.inicio
                while elemento:
                    if eleccion.lower() == elemento.nombre.lower():
                        pedido.agregar_elemento(elemento)
                        break
                    elemento = elemento.siguiente

        total = pedido.calcular_total()
        print(f"\nTotal a pagar: Q{total}")

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
            
        generar_factura(cliente, pedido, metodo_pago)
        print(f"\nGracias, {cliente.nombre} por su pedido. Su orden ha sido registrada.")


def generar_factura(cliente, pedido, metodo_pago):
    print("\n======= Factura =======")
    print(f"Cliente: {cliente.nombre}")
    print(f"Correo electrónico: {cliente.email}")
    print(f"Nit: {cliente.nit}")
    print(f"Tipo de pago: {metodo_pago.lower()}")
    print("\nDetalle de la orden:")
    
    for elemento in pedido.elementos:
        print(f"{elemento.nombre}: Q{elemento.precio}")

    total = pedido.calcular_total()
    print(f"\nTotal a pagar: Q{total}")
    print("======================")
    

def main():
    print("¡Bienvenido al Menu!")

    menu = MenuRestaurante()

    while True:
        opcion = input("\n¿Qué desea hacer? \n1. Ingresar al menú \n2. Hacer un pedido \n('q' para salir) \nIngrese su opción: ")

        if opcion == 'q':
            break
        elif opcion == '1':
            menu = ingresar_menu()
        elif opcion == '2':
            if menu.inicio is None:
                print("¡Error! El menú está vacío. Por favor, ingrese elementos al menú primero.")
            else:
                print("¡Bienvenido a nuestro restaurante!")
                print("")

                hacer_pedido(menu)
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 'q'.")

if __name__ == "__main__":
    main()



