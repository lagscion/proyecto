import json
import logs
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)



def eliminar_usuario(vecinos, id_usuario):
    id_usuar = input("\ningrese  el id del usuario a eliminar: ")

    while id_usuar not in vecinos:
        mensaje = "se intento acceder con un id inexistente en la funcion de eliminar usuario"
        logs.registrar_evento(mensaje)
        print("Ese ID no existe. No se puede acceder.")
        input("pulse cualquier tecla para continuar")
        id_usuar= (input("\n ingrese el id de la persona que quiere eliminar: "))

    while len(vecinos) <= 1:
        mensaje = "se intento eliminar a todos los usuarios"
        logs.registrar_evento(mensaje)
        print("no puede eliminar a todos los usuarios.")
        input("pulse cualquier tecla para continuar")
        id_usuar= (input("\n ingrese el id de la persona que quiere eliminar: "))

    print (f"""\nesta seguro de querer eliminar a este usuario?: 
        \nnombre: {vecinos[id_usuar]["nombre"]}
        \nid: {vecinos[id_usuar]["id"]}
        \ntelefono: {vecinos[id_usuar]["telefono"]}
        \ndireccio: {vecinos[id_usuar]["direccion"]}
        \npermisos de admin: {vecinos [id_usuar]["admin"]} """)
    
    while len(vecinos) <= 1:
        mensaje = "se intento eliminar a todos los usuarios"
        logs.registrar_evento(mensaje)
        print("no puede eliminar a todos los usuarios.")
        input("pulse cualquier tecla para continuar")
        id_usuar= (input("\n ingrese el id de la persona que quiere eliminar: "))


    opcion = input ("Y o N: ").upper()
    while id_usuar == id_usuario:
        mensaje = "se intento eliminar el usuario con el que se esta logueado"
        logs.registrar_evento(mensaje)
        print("no puede eliminar a todos los usuarios.")
        input("pulse cualquier tecla para continuar")
        id_usuar= (input("\n ingrese el id de la persona que quiere eliminar: "))

        print (f"""\nesta seguro de querer eliminar a este usuario?: 
            \nnombre: {vecinos[id_usuar]["nombre"]}
            \nid: {vecinos[id_usuar]["id"]}
            \ntelefono: {vecinos[id_usuar]["telefono"]}
            \ndireccio: {vecinos[id_usuar]["direccion"]}
            \npermisos de admin: {vecinos [id_usuar]["admin"]} """)
        opcion = input ("Y o N: ").upper()
    while opcion not in ["Y", "N"]:
        mensaje = "se ingreso una opcion diferente a Y o N en el menu de eliminar usuario"
        logs.registrar_evento(mensaje)
        print("opcion incorrecta...")
        opcion = input ("Y o N: ").upper()

    if opcion == "Y":
        del vecinos[id_usuar]
        with open("vecinos.json", "w") as archivo:
            json.dump(vecinos, archivo, indent=4)
    else:
        return
    with open ("vecinos.json", "r") as archivo:
        vecinos = json.load(archivo)