
import menus
import peticiones
import logs



def menuID():
    print ("""\n*** HOLA ***

""")

def  loggin(vecinos, herramientas, ):

    ids_val = [vecinos[i]["id"] for i in vecinos]

    menuID()
    id_usuario = input ("Ingrese su id :")

    while id_usuario not  in ids_val:
        mensaje = "se intento acceder con un id inexistente en el menu de loggin"
        logs.registrar_evento(mensaje)
        print ("error")
        print("digite un id valido")
        menuID()
        id_usuario = input("")
    
    
    id_relacion = {vecinos  [i]["id"] : vecinos[i]["admin"]for i in vecinos}
    permisos = (id_relacion[id_usuario])

    if permisos :
        menus.menu_admin(id_usuario, herramientas, peticiones, vecinos)
    else:
        menus.menu_norm(id_usuario, vecinos, herramientas, peticiones)

    return id_usuario



