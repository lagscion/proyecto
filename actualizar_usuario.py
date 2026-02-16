import json
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)

def act_usu(vecinos):
    with open ("vecinos.json", "r") as archivo:
        vecinos = json.load(archivo)
    
    
    id_usu = input ("ingrese el id de la persona que quiere actualizar: ")
    
    while id_usu not in vecinos:
        print("Ese ID no existe. No se puede acceder.")
        input("pulse cualquier tecla para continuar")
        id_usu = (input("\n ingrese el id de la persona que quiere actualizar: "))

    print("""\nque parametro quisiera cambiar? : 
1.) nombre
2.) id
3.) telefono
4.) direccion
5.) admin\n""") 
    opcion = int(input ("opcion: "))

    while opcion < 0 :
    
        print("\ningrese una opcion valida")
        input("\npresione cualquier tecla para continuar...")
        print("""\nque parametro quisiera cambiar? : 
1.) nombre
2.) id
3.) telefono
4.) direccion
5.) admin
6.) salir \n""") 
        opcion = int(input ("\nopcion: "))




    if opcion == 1:
        new_nombre = input ("ingrese el nuevo nombre: ")
        vecinos[id_usu]["nombre"] = new_nombre

        with open ("vecinos.json", "w") as archivo:
            json.dump(vecinos, archivo, indent=4)


    if opcion == 2:
        new_id = input ("ingrese el nuevo id: ")
        while new_id in vecinos["id"]:
            print("Ese ID ya existe. No se puede registrar.")
            input("pulse cualquier letra para continuar")
            id = int(input("\nIngrese el nuevo ID del usuario: "))
            id = str(id)  
        vecinos[id_usu]["id"] = new_id

        with open ("vecinos.json", "w") as archivo:
            json.dump(vecinos, archivo, indent=4)


    if opcion == 3:
        while True:
            try:
                new_telefono = int(input("\nIngrese el nuevo ID del usuario: "))
                break
            except ValueError:
                print("telefono inválido...")
        while new_telefono in vecinos["telefono"]:
                print("Ese telefono ya existe. No se puede registrar.")
                input("pulse cualquier letra para continuar")
                new_telefono = (input("\nIngrese el nuevo telefono del usuario: "))
        vecinos[id_usu]["telefono"] = new_telefono

        with open ("vecinos.json", "w") as archivo:
            json.dump(vecinos, archivo, indent=4)


    if opcion == 4:
        new_direccion = input ("ingrese la nueva direccion: ")
        while new_direccion in vecinos["direccion"]:
                print("Esa direccion ya esta registrada. No se puede registrar.")
                input("pulse cualquier letra para continuar")
                new_direccion = (input("\nIngrese la nueva direccion del usuario: "))
        vecinos[id_usu]["direccion"] = new_direccion

        with open ("vecinos.json", "w") as archivo:
            json.dump(vecinos, archivo, indent=4)


    if opcion == 5:
        new_admin = input ("obtendra permisos de admin? Y o N: ").upper()
        if new_admin == "Y":
            admin = True
            vecinos[id_usu]["admin"] = admin
            with open ("vecinos.json", "w") as archivo:
                json.dump(vecinos, archivo, indent=4)
        else: 
            admin = False
            vecinos[id_usu]["admin"] = admin
            with open ("vecinos.json", "w") as archivo:
                json.dump(vecinos, archivo, indent=4)

    with open ("vecinos.json", "r") as archivo:
        vecinos = json.load(archivo)


