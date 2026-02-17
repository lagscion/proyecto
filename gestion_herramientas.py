import json
import logs
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)

def menu_herramientas(herramientas):
    print ("""\nQUE PLANEA HACER CON LAS HERRAMIENTAS?: 

1. crear una nueva 

2. listarlas

3. buscar una herramienta

4. actualizar herramienta existente

5. eliminar herramienta

6. salir""")

# CREACION DE HERRAMIENTAS===================================================================================================================

def crear_herramientas(herramientas):
    nombre_h = input ("\nIngrese el nombre de la herramienta: ")
    nombres = [herramientas[i]["nombre"] for i in herramientas]
    while nombre_h in nombres:
        mensaje = "se intento crear una herramienta existente"
        logs.registrar_evento(mensaje)
        print("Ese nombre ya existe. No se puede registrar.")
        input("pulse cualquier letra para continuar")
        nombre_h = (input("\nIngrese el nombre de la herramienta:  "))
    estado_h = input ("\nEn que estado se encuentra la herramienta: ")
    categoria_h = input ("\nA que categoria pertenece: ")
    while True:
        try:
            stock_h = int(input ("\nCuantas herramientas hay: "))
            break
        except ValueError:    
            mensaje = "se intento ingresar un valor diferente a un numero en el menu de agregar herramienta"
            logs.registrar_evento(mensaje)
            print("\nValor inválido...")
    while True:
        try:
            valor_h = int(input ("\nQue valor estimado tiene esa herramienta: "))
            break
        except ValueError:
            mensaje = "se intento ingresar un valor diferente a un numero en el menu de agregar herramienta"
            logs.registrar_evento(mensaje)
            print("\nValor inválido...")

    while True:
        try:
            id_h = int(input("\nIngrese el id de la herramienta:  "))
            id_h = str(id_h)  
            while id_h in herramientas:
                mensaje = "se intento ingresar un id existente en el menu de agregar herramienta"
                logs.registrar_evento(mensaje)
                print("Ese ID ya existe. No se puede registrar.")
                input("pulse cualquier letra para continuar")
                id_h = str(int(input("\nIngrese el id de la herramienta:  ")))
            break
        except ValueError:
            mensaje = "se intento ingresar un valor diferente a un numero en el menu de agregar herramienta"
            logs.registrar_evento(mensaje)
            print("\nValor inválido...")



    herramientas[id_h] = {
        "nombre" : nombre_h,
        "estado" : estado_h,
        "categoria" : categoria_h,
        "stock" : stock_h,
        "valor" : valor_h,
        "id" : id_h
    }
    with open("herramientas.json", "w") as archivo:
        json.dump ( herramientas, archivo, indent = 4)

#LISTADO DE HERRAMIENTAS====================================================================================================================================

def listar_herramientas(herramientas):
        print ("herramientas: ")
        contador = 1
        for i in herramientas:
            print(f""" 
    herramienta No: {contador}
nombre: {herramientas[i]["nombre"]}
estado: {herramientas[i]["estado"]}
categoria: {herramientas[i]["categoria"]}
stock: {herramientas[i]["stock"]}
valor: {herramientas[i]["valor"]}
id: {herramientas[i]["id"]}""")
            contador += 1

# BUSCAR HERRAMIENTA ================================================================================================================================================

def buscar (herramientas):
    print("ingrese el id de su herramienta")
    id_bus  = input("ID: ")
    while id_bus not in herramientas:
        mensaje = "se intento buscar un id inexistente en el menu de buscar herramienta"
        logs.registrar_evento(mensaje)
        print ("id inexistente...")
        input ("presione cualqier tecla para continuar...")
        print("ingrese el id de su herramienta")
        id_bus  = input("ID: ")
    print(f"""\nHeramienta: {herramientas[id_bus]["nombre"]}

estado: {herramientas[id_bus]["estado"]}

categoria: {herramientas[id_bus]["categoria"]}

stock: {herramientas[id_bus]["stock"]}

valor: {herramientas[id_bus]["valor"]}

id: {herramientas[id_bus]["id"]}
""")





# ACTUALIZACION DE HERRAMIENTAS====================================================================================================

def actualizar_her(herramientas):
    with open ("herramientas.json", "r") as archivo:
        herramientas = json.load(archivo)
    
    
    id_her = input ("ingrese el id de la herramienta que quiere actualizar: ")
    
    while id_her not in herramientas:
        mensaje = "se intento acceder con un id inexistente en el menu de actualizar herramienta"  
        logs.registrar_evento(mensaje)
        print("Ese ID no existe. No se puede acceder.")
        input("pulse cualquier tecla para continuar")
        id_her = (input("\n ingrese el id de la herramienta que quiere actualizar: "))

    print("""\nque parametro quisiera cambiar? : 
1. nombre
2. estado
3. categoria
4. stock
5. valor
6. id\n""") 
    opcion = int(input ("opcion: "))

    while opcion < 1 or opcion > 6:
        mensaje = "se intento poner una opcion equivocada en el menu de actualizar herramienta"
        logs.registrar_evento(mensaje)
        print("\ningrese una opcion valida")
        input("\npresione cualquier tecla para continuar...")
        print("""\nque parametro quisiera cambiar? : 
1. nombre
2. estado
3. categoria
4. stock
5. valor
6. id\n""") 
        opcion = int(input ("\nopcion: "))

    if opcion == 1:
        nombre_her = input ("ingrese el nuevo nombre: ")
        herramientas[id_her]["nombre"] = nombre_her

        with open ("herramientas.json", "w") as archivo:
            json.dump(herramientas, archivo, indent = 4)


    if opcion == 2:
        estado_her = input ("ingrese el estado  de la herramienta: ")
        herramientas[id_her]["estado"] = estado_her

        with open ("herramientas.json", "w") as archivo:
            json.dump(herramientas, archivo, indent = 4)

    if opcion == 3:
        categoria_her = input ("ingrese la nueva categoria: ")
        herramientas[id_her]["categoria"] = categoria_her

        with open ("herramientas.json", "w") as archivo:
            json.dump(herramientas, archivo, indent = 4)


    if opcion == 4:
        stock_her = input ("ingrese la cantidad de herramientas: ")
        herramientas[id_her]["stock"] = stock_her

        with open ("herramientas.json", "w") as archivo:
            json.dump(herramientas, archivo, indent = 4)


    if opcion == 5:
        valor_her = input ("ingrese el valor de la herramienta: ")
        herramientas[id_her]["valor"] = valor_her

        with open ("herramientas.json", "w") as archivo:
            json.dump(herramientas, archivo, indent = 4)


    if opcion == 6:
        while True:
            nuevo_id = input("\nIngrese el nuevo ID de la herramienta: ")
            if nuevo_id in herramientas:
                mensaje = "se intento ingresar un id existente en el menu de actualizar herramienta"
                logs.registrar_evento(mensaje)
                print("Ese ID ya existe. No se puede registrar.")
                input("pulse cualquier letra para continuar")
            else:
                break

        herramientas[nuevo_id] = herramientas.pop(id_her)
        herramientas[nuevo_id]["id"] = nuevo_id

        with open("herramientas.json", "w") as archivo:
            json.dump(herramientas, archivo, indent=4)

# ELIMINAR HERRAMIENTAS================================================================================================================================

def eliminar (herramientas): 
    id_her = input("\ningrese  el id de la herramienta a eliminar: ")

    while id_her not in herramientas:
        mensaje = "se intento acceder con un id inexistente en la funcion de eliminar herramienta"
        logs.registrar_evento(mensaje)
        print("Ese ID no existe. No se puede acceder.")
        input("pulse cualquier tecla para continuar")
        id_her= (input("\n ingrese el id de la herramienta que quiere eliminar: "))

    while len(herramientas) <= 1:
        mensaje = "se intento eliminar a todas las herramientas"
        logs.registrar_evento(mensaje)
        print("no puede eliminar a todas las herramientas.")
        input("pulse cualquier tecla para continuar")
        id_her= (input("\n ingrese el id de la herramienta que quiere eliminar: "))

    print (f"""\nesta seguro de querer eliminar esta herramienta ?: 
        \nnombre: {herramientas[id_her]["nombre"]}
        \nestado: {herramientas[id_her]["estado"]}
        \ncategoria: {herramientas[id_her]["categoria"]}
        \ndireccio: {herramientas[id_her]["stock"]}
        \nvalor: {herramientas [id_her]["valor"]}
        \nid: {herramientas[id_her]["id"]}""")
    
    while len(herramientas) <= 1:
        mensaje = "se intento eliminar a todas las herramientas"
        logs.registrar_evento(mensaje)
        print("no puede eliminar a todas las herramientas.")
        input("pulse cualquier tecla para continuar")
        id_her = (input("\n ingrese el id de la herramienta que quiere eliminar: "))


    opcion = input ("Y o N: ").upper()

    if opcion == "Y":
        del herramientas[id_her]
        with open("herramientas.json", "w") as archivo:
            json.dump(herramientas, archivo, indent=4)
    else:
        pass
    with open ("herramientas.json", "r") as archivo:
        herramientas = json.load(archivo)


##################################################################################################################################

def manejo_h (herramientas):
    while True:

        with open ("herramientas.json", "r") as archivo:
            herramientas = json.load(archivo)
        
        menu_herramientas(herramientas)
        opcion = int(input("opcion: "))

        while opcion < 1 or opcion > 6:
            mensaje = "se intento poner una opcion equivocada en el menu de gestion de herramientas"
            logs.registrar_evento(mensaje)
            print("opcion invalida.")
            input("pulse cualquier tecla para continuar")
            menu_herramientas(herramientas)
            opcion = int(input("opcion: "))

        if opcion == 1:
            crear_herramientas(herramientas)
        elif opcion == 2:
            listar_herramientas(herramientas)
        elif opcion == 3:
            buscar(herramientas)
        elif opcion == 4:
            actualizar_her(herramientas)
        elif opcion == 5:
            eliminar (herramientas)
        else:
            break







