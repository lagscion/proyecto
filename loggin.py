import json
import menus
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)



def menuID():
    print ("""*** HOLA ***

""")

def  loggin():

    ids_val = [vecinos[i]["id"] for i in vecinos]

    menuID()
    id_usuario = input ("Ingrese su id :")

    while id_usuario not  in ids_val:
        print ("error")
        print("digite un id valido")
        menuID()
        id_usuario = input("")
    
    id_relacion = {vecinos  [i]["id"] : vecinos[i]["admin"]for i in vecinos}
    permisos = (id_relacion[id_usuario])
    if permisos :
        menus.menu_admin(id_usuario)
    else:
        menus.menu_norm(id_usuario)

    return id_usuario


