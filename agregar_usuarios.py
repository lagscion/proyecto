import logs

def crear_usuario(vecinos):
    nombre = input("\ningrese el nombre del nuevo usuario: ").upper()
    while nombre in [vecinos[i]["nombre"].upper() for i in vecinos]:
        mensaje = "se intento crear un usuario existente"
        logs.registrar_evento(mensaje)
        print("Ese usuario ya existe. No se puede registrar.")
        input("pulse cualquier letra para continuar")
        nombre = input("\nIngrese el nuevo nombre del usuario: ").upper()

    while True:
        try:
            id = input("\nIngrese el nuevo ID del usuario: ")
            if id in vecinos:
                mensaje = "se intento ingresar un id existente en el menu de agregar usuario"
                logs.registrar_evento(mensaje)
                print("Ese ID ya existe. No se puede registrar.")
                input("pulse cualquier letra para continuar")
                continue
            break
        except ValueError:
            mensaje = "se intento ingresar un valor diferente a un numero"
            logs.registrar_evento(mensaje)
            print("ID inválido...")

    while True:
        try:
            telefono = input("\ningrese el numero de telefono del nuevo usuario: ")
            if any(vecinos[i]["telefono"] == telefono for i in vecinos):
                mensaje = "se intento agregar un telefono ya existente en la funcion agregar usuario"
                logs.registrar_evento(mensaje)
                print("Ese telefono ya tiene usuario. No se puede registrar.")
                input("pulse cualquier letra para continuar")
                continue
            break
        except ValueError:
            mensaje = "se intento ingresar un valor diferente a un numero en el menu de agregar usuario"
            logs.registrar_evento(mensaje)
            print("opcion incorrecta...")
            input ("presione cualquier tecla para continuar: ")

    direccion = input("\ningrese la direccion del nuevo usuario: ")
    while any(vecinos[i]["direccion"] == direccion for i in vecinos):
        mensaje = "se intento ingresar una direccion ya existente en el menu de agregar usuario"
        logs.registrar_evento(mensaje)
        print("Esa direccion ya esta asignada. No se puede registrar.")
        input("pulse cualquier letra para continuar")
        direccion = input("\nIngrese la nueva direccion del usuario: ")

    admin = input("\nel usuario tiene permisos de administracion? Y o N: ").upper()
    while admin not in ["Y", "N"]:
        mensaje = "se ingreso una opcion diferente a Y o N en el menu de agregar usuario"
        logs.registrar_evento(mensaje)
        print("opcion incorrecta...")
        admin = input("\nel usuario tiene permisos de administracion? Y o N: ").upper()

    admin = True if admin == "Y" else False

    vecinos[id] = {
        "nombre": nombre,
        "telefono": telefono,
        "direccion": direccion,
        "admin": admin,
        "prestamo": {}
    }

    print("\n*** USUARIO INGRESADO CORRECTAMENTE ***")

