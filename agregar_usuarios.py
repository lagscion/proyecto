import json
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)


def  crear_usuario():
    nombre = input ("\ningrese el nombre del nuevo usuario: ").upper()
    while nombre in vecinos["nombre"]:
        print("Ese usuario ya existe. No se puede registrar.")
        input("pulse cualquier letra para continuar")
        nombre = (input("\nIngrese el nuevo nombre del usuario: "))



    while True:
        try:
            id = int(input("\nIngrese el nuevo ID del usuario: "))
            id = str(id)  
            break
        except ValueError:
            print("ID inválido...")


    while id in vecinos:
        print("Ese ID ya existe. No se puede registrar.")
        input("pulse cualquier letra para continuar")
        id = int(input("\nIngrese el nuevo ID del usuario: "))
        id = str(id)  


    while True:
        try:
            telefono = int(input("\ningrese el numero de telefono del nuevo usuario: "))
            while telefono in vecinos["telefono"]:
                print("Ese telefono ya tiene usuario. No se puede registrar.")
                input("pulse cualquier letra para continuar")
                telefono = int(input("\nIngrese el nuevo telefono del usuario: "))
            break
        except ValueError:
            print("opcion incorrecta...")
            input ("presione cualquier tecla para continuar: ")

    direccion = input("\ningrese la direccion del nuevo usuario: ")
    while direccion in vecinos["direccion"]:
        print("Esa direccion ya esta asignada. No se puede registrar.")
        input("pulse cualquier letra para continuar")
        direccion = (input("\nIngrese la nueva direccion del usuario: "))


    admin = input("\nel usuario tiene permisos de administracion? Y o N: ").upper()
    while admin not in ["Y", "N"]:
        print("opcion incorrecta...")
        admin = input("\nel usuario tiene permisos de administracion? Y o N: ").upper()

    if admin == "Y":
        admin = True
    else: 
        admin = False

    vecinos[id] = {
        "nombre": nombre,
        "id": id,
        "telefono": telefono,
        "direccion": direccion,
        "admin": admin
    }

    with open("vecinos.json", "w") as archivo:
        json.dump(vecinos, archivo, indent=4)

    print ("\n*** usuario ingresado correctamente ***".upper())

