# Grupo: 2
# Estudiantes: Samuel Alvarez Montoya
# Unidad 2 - Taller Evaluativo: Implementación de Algoritmos en Python
# Temas: Funciones, parámetros, recursividad, estructuras de datos y manejo de errores

import random
from datetime import datetime

inventario = {}
CATEGORIAS = ("Computador", "Teléfono", "Periférico")


def validar_texto(valor):
    if valor.strip() == "":
        print("No puede dejar el dato vacío.")
        return None
    return valor.strip()


def validar_precio(valor):
    try:
        precio = float(valor)
        if precio > 0:
            return precio
        print("El precio debe ser mayor que cero.")
    except ValueError:
        print("Ingrese un número válido.")
    return None


def validar_cantidad(valor):
    try:
        cantidad = int(valor)
        if cantidad >= 0:
            return cantidad
        print("La cantidad no puede ser negativa.")
    except ValueError:
        print("Ingrese un número entero.")
    return None

def solicitar_dato(mensaje, validar):
    while True:
        dato = input(mensaje)
        resultado = validar(dato)
        if resultado != None:
            return resultado

def elegir_categoria():
    while True:
        print("1. Computador")
        print("2. Teléfono")
        print("3. Periférico")
        opcion = input("Categoría: ")
        if opcion == "1":
            return CATEGORIAS[0]
        elif opcion == "2":
            return CATEGORIAS[1]
        elif opcion == "3":
            return CATEGORIAS[2]
        else:
            print("Opción no válida.")

def generar_codigo(categoria, inicio=1):
    inicial = categoria[0].upper()
    usados = 0
    for codigo in inventario:
        if codigo[0] == inicial:
            usados = usados + 1
    if usados == 999:
        return ""

    codigo = ""
    while codigo == "" or codigo in inventario:
        numero = random.randint(inicio, 999)
        codigo = f"{inicial}{numero:03d}"
    return codigo

def mostrar_mensajes(*mensajes):
    for mensaje in mensajes:
        print(mensaje)


def agregar_producto():
    nombre = solicitar_dato("Nombre: ", validar_texto)
    categoria = elegir_categoria()
    precio = solicitar_dato("Precio: ", validar_precio)
    cantidad = solicitar_dato("Cantidad: ", validar_cantidad)
    codigo = generar_codigo(categoria=categoria)

    if codigo == "":
        print("No quedan códigos disponibles en esta categoría.")
        return

    fecha = str(datetime.now())
    inventario[codigo] = f"{nombre}~{categoria}~{precio}~{cantidad}~{fecha}"
    mostrar_mensajes("Producto agregado.", f"Código: {codigo}")

def mostrar_producto(codigo, datos):
    partes = datos.split("~")
    print("\n--------------------------------------------")
    print(f"Código: {codigo}")
    print(f"Nombre: {partes[0]}")
    print(f"Categoría: {partes[1]}")
    print(f"Precio: {partes[2]}")
    print(f"Cantidad: {partes[3]}")
    print(f"Fecha: {partes[4]}")


def ver_productos():
    if len(inventario) == 0:
        print("No hay productos registrados. Ingrewe al menos uno...")
        return
    for codigo in inventario:
        mostrar_producto(codigo, inventario[codigo])


def editar_producto():
    codigo = input("Código a editar: ").upper().strip()
    if codigo not in inventario:
        print("No existe ese producto.")
        return

    partes = inventario[codigo].split("~")
    nombre = partes[0]
    categoria = partes[1]
    precio = partes[2]
    cantidad = partes[3]
    fecha = partes[4]

    print("1. Nombre")
    print("2. Precio")
    print("3. Cantidad")
    print("4. Categoría")
    opcion = input("¿Qué desea editar?: ")

    if opcion == "1":
        nombre = solicitar_dato("Nuevo nombre: ", validar_texto)
    elif opcion == "2":
        precio = solicitar_dato("Nuevo precio: ", validar_precio)
    elif opcion == "3":
        cantidad = solicitar_dato("Nueva cantidad: ", validar_cantidad)
    elif opcion == "4":
        categoria = elegir_categoria()
    else:
        print("Opción no válida.")
        return

    inventario[codigo] = f"{nombre}~{categoria}~{precio}~{cantidad}~{fecha}"
    print("Producto editado.")


def eliminar_producto():
    codigo = input("Código a eliminar: ").upper().strip()
    if codigo in inventario:
        inventario.pop(codigo)
        print("Producto eliminado.")
    else:
        print("No existe ese producto.")

def buscar_producto(codigos, letra, posicion=0):
    if posicion == len(codigos):
        return 0

    codigo = codigos[posicion]
    partes = inventario[codigo].split("~")
    encontrados = 0

    if partes[0][0].lower() == letra.lower():
        mostrar_producto(codigo, inventario[codigo])
        encontrados = 1

    return encontrados + buscar_producto(codigos, letra, posicion + 1)

def buscar_por_inicial():
    letra = solicitar_dato("Ingrese una letra: ", validar_texto)
    if len(letra) != 1 or letra.isalpha() == False:
        print("Debe ingresar una sola letra.")
        return

    codigos = list(inventario)
    cantidad = buscar_producto(codigos, letra)
    print(f"Productos encontrados: {cantidad}")

def estadisticas():
    precios = []
    for codigo in inventario:
        partes = inventario[codigo].split("~")
        precios.append(float(partes[2]))

    if len(precios) == 0:
        print("No hay productos registrados.")
        return

    promedio = sum(precios) / len(precios)
    print(f"Promedio: {promedio:.2f}")
    print(f"Máximo: {max(precios):.2f}")
    print(f"Mínimo: {min(precios):.2f}")


def mostrar_menu():
    print("\nBienvenido...\n")
    print("1. Agregar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Ver productos")
    print("5. Buscar por inicial")
    print("6. Estadísticas")
    print("7. Salir\n")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        editar_producto()
    elif opcion == "3":
        eliminar_producto()
    elif opcion == "4":
        ver_productos()
    elif opcion == "5":
        buscar_por_inicial()
    elif opcion == "6":
        estadisticas()
    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    else:
        print("\nOpción no válida. Intente nuevamente.")
