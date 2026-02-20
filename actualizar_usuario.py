import json
import logs

def act_usu(vecinos):
    
    
    id_usu = input ("ingrese el id de la persona que quiere actualizar: ")
    
    while id_usu not in vecinos:
        mensaje = "se intento acceder con un id inexistente en la funcion de actualizar usuario"
        logs.registrar_evento(mensaje)

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

    while opcion < 1 or opcion > 6:
        mensaje = "se intento poner una opcion equivocada"
        logs.registrar_evento(mensaje)
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
        new_id = input("Ingrese el nuevo ID para este usuario: ")

        
        while new_id in vecinos:
            print("Ese ID ya existe. Intente otro.")
            new_id = input("Ingrese el nuevo ID para este usuario: ")

        
        usuario = vecinos[id_usu]
        usuario["id"] = new_id

        
        vecinos[new_id] = vecinos.pop(id_usu)

        
        with open("vecinos.json", "w", encoding="utf-8") as archivo:
            json.dump(vecinos, archivo, indent=4, ensure_ascii=False)

        print(f"ID del usuario actualizado correctamente a {new_id}")


    if opcion == 3:
        while True:
            try:
                new_telefono = int(input("\nIngrese el nuevo ID del usuario: "))
                break
            except ValueError:
                mensaje = "se ingreso algo que no era un numero"
                logs.registrar_evento(mensaje)
                print("telefono inválido...")
        while any(vecinos[i]["telefono"] == new_telefono for i in vecinos):
                mensaje = "se intento ingresar un telefono ya existente"
                logs.registrar_evento(mensaje)
                print("Ese telefono ya existe. No se puede registrar.")
                input("pulse cualquier letra para continuar")
                new_telefono = (input("\nIngrese el nuevo telefono del usuario: "))
        vecinos[id_usu]["telefono"] = new_telefono

        with open ("vecinos.json", "w") as archivo:
            json.dump(vecinos, archivo, indent=4)


    if opcion == 4:
        new_direccion = input ("ingrese la nueva direccion: ")
        while any(vecinos[i]["direccion"] == new_direccion for i in vecinos):
                mensaje = "se intento ingresar una direcicion existente"
                logs.registrar_evento(mensaje)
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



