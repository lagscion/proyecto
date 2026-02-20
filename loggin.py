import json
import menus
import logs

def menuID():
    print("\n*** HOLA ***\n")

def loggin(vecinos, herramientas):
    with open("peticiones.json", "r", encoding="utf-8") as archivo:
        peticiones_data = json.load(archivo)

    ids_val = [vecinos[i]["id"] for i in vecinos]

    menuID()
    id_usuario = input("Ingrese su id: ")

    while id_usuario not in ids_val:
        mensaje = "se intento acceder con un id inexistente en el menu de loggin"
        logs.registrar_evento(mensaje)
        print("Error: digite un id valido")
        menuID()
        id_usuario = input("")

    id_relacion = {vecinos[i]["id"]: vecinos[i]["admin"] for i in vecinos}
    permisos = id_relacion[id_usuario]

    if permisos:
        menus.menu_admin(id_usuario, vecinos, herramientas, peticiones_data)
    else:
        menus.menu_norm(id_usuario, vecinos, herramientas, peticiones_data)

    return id_usuario


