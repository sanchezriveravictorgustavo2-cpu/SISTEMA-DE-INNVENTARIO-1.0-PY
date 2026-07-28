inventario = []
#esta funcion crea productos
def agregar_producto():
    nombre = input("\nIngresa el nombre del producto: ").lower().strip()
    #excepciones donde el usuario ingrese letras o simbolos a el precio o cantidad de los productos
    try:
        precio = float(input("Ingresa el preecio del producto: "))
        cantidad = int(input("Ingresa la cantidad inicial de este producto: "))
    except ValueError:
        print("¡Error! El precio y la cantidad deben ser números. Registro cancelado.")
        return
    producto = {
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad,
    }
    inventario.append(producto)
    print("producto agregado correctamente")



#aqui creamos la funcion de ver todos los productos
def ver_productos():
    if len(inventario) >0: #aqui si las lista tiene mas de 1 producto los imprime y gracias al for los va imprimiendo
        print("============Productos==========")
        for producto in inventario:
            print("------------------------------------------------------------------------------------------------------")
            print(f"\n nombre: {producto['nombre']} / precio: ${producto['precio']} / cantidad: {producto['cantidad']}  ")
            print("------------------------------------------------------------------------------------------------------")
    else:
        print("\n no hay productos aún")
#esta funcion es para buscar un producto y saber sus caracteristicas



def buscar_productos():
    buscar = input("Ingresa un producto para buscarlo: ").lower().strip()

    encontrado = False
#el for lo que hace es rrecorer toda la lista y despues el if compara si en producto dentro de nombre hay uno igual y si lo hay imprime sus caracteristicas y despues se cierra
    for producto in inventario:
        if producto['nombre'] == buscar:
            print(f"\n nombre: {producto['nombre']} / precio: ${producto['precio']} / cantidad: {producto['cantidad']}")
            encontrado = True
            break
    if encontrado == False: #como no es un ciclo while solo rrecore todos los productos una sola vez cuando termina no lo encuentra entonces imprime eso
        print("Este producto no existe")



def eliminar_productos():
    buscar = input("Ingresa un producto para buscarlo: ").lower().strip()

    encontrado = False
    for producto in inventario:
        if producto['nombre'] == buscar:
            print(f"\n nombre: {producto['nombre']} / precio: ${producto['precio']} / cantidad: {producto['cantidad']}")
            encontrado = True
            eliminar = input("seguro que quieres eliminar? si/no ").lower().strip()
            if eliminar == "si":
                inventario.remove(producto)
                print("producto eliminado correctamente")
                break
            else:
                print("!Producto NO eliminado!")
                break

    if not encontrado: 
        print("Este producto no existe")



def eliminar_cantidad():
    buscar = input("Ingresa un producto para buscarlo: ").lower().strip()
    encontrado = False
    for producto in inventario:
        if producto['nombre'] == buscar:
            print(f"\n nombre: {producto['nombre']} / cantidad: {producto['cantidad']}")
            encontrado = True
            try:
                restar = int(input("Ingresa el valor a restar solo numeros"))

                if producto['cantidad'] >= restar and restar >=1:
                    producto['cantidad'] -= restar
                    print("producto restado perfectamente, la cantidad actual es:", producto['cantidad'])

                else:
                    print("no se puede restar ya que es mayor a la cantidad actual, SOLO INGRESA NUMEROS NO SIMBOLOS")

            except ValueError:
                print("Solo se puede ingresar numeros")
                return

            break
    if encontrado == False: 
        print("Este producto no existe")





#este es el menu principal 
while True:
    print("\n%...sistema de inventario en consola...%")
    print("opciones:")
    print("1.agregar producto\n" 
          "2.Ver productos\n"
          "3.buscar producto \n" 
          "4.eliminar producto\n"
          "5.Eliminar cantidad"
          "6.añadir cantidad\n" 
          "7.cambiar precio\n" 
          "8.salir")
    opcion = input("Elige una opción (1-): ").strip()
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        ver_productos()
    elif opcion == "3":
        buscar_productos()
    elif opcion == "4":
        eliminar_productos()
    elif opcion == "5":
        eliminar_cantidad()
    
