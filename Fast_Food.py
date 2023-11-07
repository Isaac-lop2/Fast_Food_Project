from collections import deque

# Inicializar el menú con precios
menu_empleado = {}
menu_usuario = {}

# Inicializar una cola para rastrear los cambios de precios
cambios_precios = deque()

# Función para mostrar el menú (para empleado o usuario)
def mostrar_menu(menu):
    print("Menú y Precios:")
    for item, precio in menu.items():
        print(f"{item}: ${precio}")

# Función para actualizar precios (solo para empleados)
def actualizar_precios():
    mostrar_menu(menu_empleado)
    item = input("Ingresa el elemento del menú para actualizar el precio: ")
    if item in menu_empleado:
        nuevo_precio = float(input(f"Nuevo precio para {item}: $"))
        cambios_precios.append((item, menu_empleado[item], nuevo_precio))
        menu_empleado[item] = nuevo_precio
        print(f"Precio de {item} actualizado con éxito.")
    else:
        print("Producto no válido. Inténtalo de nuevo.")

# Función para crear el menú (solo para empleados)
def crear_menu():
    while True:
        nombre = input("Ingresa el nombre del elemento del menú (o 'fin' para terminar): ")
        if nombre == 'fin':
            break
        precio = float(input(f"Precio para {nombre}: $"))
        menu_empleado[nombre] = precio
        print(f"{nombre} ha sido añadido al menú.")

# Función para deshacer el último cambio de precio (solo para empleados)
def deshacer_cambio():
    if cambios_precios:
        item, precio_anterior, _ = cambios_precios.pop()
        menu_empleado[item] = precio_anterior
        print(f"Se deshizo el cambio de precio para {item}.")
    else:
        print("No hay cambios de precio para deshacer.")

while True:
    print("\nOpciones:")
    print("1. Mostrar Menú (Usuario)")
    print("2. Mostrar Menú (Empleado)")
    print("3. Actualizar Precios (Empleado)")
    print("4. Crear Menú (Empleado)")
    print("5. Deshacer Cambio de Precio (Empleado)")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_menu(menu_usuario)
    elif opcion == "2":
        mostrar_menu(menu_empleado)
    elif opcion == "3":
        actualizar_precios()
    elif opcion == "4":
        crear_menu()
    elif opcion == "5":
        deshacer_cambio()
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")