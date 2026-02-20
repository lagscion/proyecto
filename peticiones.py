
import json
import logs



def menu (id_usuario, herramientas,vecinos):
    print (f""" *** HOLA, CLARO {(vecinos[id_usuario]["nombre"])} ***
    herramientas: """)
    contador = 1
    for i in herramientas:
        print(f""" 
    herramienta id: {contador}
    nombre: {herramientas[i]["nombre"]}
    estado: {herramientas[i]["estado"]}
    categoria: {herramientas[i]["categoria"]}
    stock: {herramientas[i]["stock"]}
    valor: {herramientas[i]["valor"]}
    id: {herramientas[i]["id"]}""")
        contador += 1


def maxim_id(peticiones):
    if not peticiones:
        return "1"
    return str(max(map(int, peticiones.keys())) + 1)


def peticion(id_usuario, herramientas, vecinos, peticiones):
    while True :

        menu(id_usuario, herramientas, vecinos)
        opcion = (input("ID de la herramienta a presar: "))

        while int(opcion) < 1 or len(herramientas) < int(opcion) :
            mensaje = "se ingreso una opcion diferente a un numero o un numero fuera del rango de herramientas en el menu de solicitud de herramienta"
            logs.registrar_evento(mensaje)
            print("opcion equivocada, pofavor ingrese una opcion valida...")
            input("pulse cualquier tecla para continuar: ")
            opcion = input("ID de la herramienta a presar: ")
        while opcion not in herramientas:
            mensaje = "se ingreso una opcion diferente a un numero o un numero fuera del rango de herramientas en el menu de solicitud de herramienta"
            logs.registrar_evento(mensaje)
            print("opcion equivocada, pofavor ingrese una opcion valida...")
            input("pulse cualquier tecla para continuar: ")
            opcion = input("ID de la herramienta a presar: ")

        cantidad = int(input("ingrese la cantidad de herramientas a  prestar: "))
        while cantidad > herramientas[opcion]["stock"] or cantidad < 1:
            mensaje = "se ingreso una cantidad invalida  en el menu de solicitud de herramienta"
            logs.registrar_evento(mensaje)
            print("cantidad invalida, porfavor ingrese una cantidad valida ...")
            input("pulse cualquier tecla para continuar: ")
            cantidad = int(input("ingrese la cantidad de herramientas a  prestar: "))

        herramienta = herramientas[opcion]["nombre"]

        while True:
            try:  
                fecha = int(input("ingrese el numero aprox dias en los que devolveria la herramienta: "))
                while fecha < 1:
                    print ("ingrese una fecha valida...")
                    fecha = int(input("ingrese el numero aprox dias en los que devolveria la herramienta: "))
                break
            except ValueError:
                mensaje = "se ingreso un valor diferente a un numero en el menu de solicitud de herramienta"
                logs.registrar_evento(mensaje)
                print("ingrese un valor valido")
            

        nuevo_id = maxim_id(peticiones)

        peticiones[nuevo_id] = {
            "id del pedido" : nuevo_id,
            "quien" : id_usuario,
            "herramienta" : herramienta,
            "cantidad" : cantidad,
            "fecha" : fecha,
            "estado" : ""
        }

        with open("peticiones.json", "w") as archivo_pet:
            json.dump(peticiones, archivo_pet, indent=4)

        mensaje = f"se realizo una solicitud de herramienta {herramienta} por parte del usuario {vecinos[id_usuario]['nombre']} con id {id_usuario}"
        logs.registrar_evento(mensaje)

        break
#APROVACIONES=================================================================================================================================================
def aprovar(peticiones, vecinos, herramientas):


    id_apro = input ("ingrese el ID del pedido que quisiera  aprovar: ")
    while id_apro not in peticiones:
        mensaje = "se ingreso una opcion diferente a un numero o un numero fuera del rango de pedidos en el menu de aprovacion de peticiones"
        logs.registrar_evento(mensaje)
        print ("\nID invalido, profavor ingrese un ID valido")
        id_apro = input("Ingrese el ID del pedido que quiere aprobar: ")


    pedido = peticiones[id_apro]
    id_usuario = pedido["quien"]
    nombre_herramienta = pedido["herramienta"]
    cantidad = pedido["cantidad"]


    id_herramienta = None

    for h in herramientas:
        if herramientas[h]["nombre"] == nombre_herramienta:
            id_herramienta = h
            break

    if id_herramienta is None:
        mensaje = "se intento aprobar un pedido con una herramienta que no existe en el menu de aprovacion de peticiones"
        logs.registrar_evento(mensaje)
        print("Error: herramienta no encontrada")
        return

    if herramientas[id_herramienta]["stock"] < cantidad:
        mensaje = "se intento aprobar un pedido con una cantidad mayor al stock disponible en el menu de aprovacion de peticiones"
        logs.registrar_evento(mensaje)
        print("No hay suficiente stock")
        return

    pedido["estado"] = "aprobado"

    herramientas[id_herramienta]["stock"] -= cantidad

    if "prestamo" not in vecinos[id_usuario]:
        mensaje = "se intento aprobar un pedido para un usuario que no tiene prestamos registrados en el menu de aprovacion de peticiones"
        logs.registrar_evento(mensaje)
        vecinos[id_usuario]["prestamo"] = {}

    vecinos[id_usuario]["prestamo"][id_apro] = pedido

    del peticiones[id_apro]

    with open("peticiones.json", "w") as arch_pet:
        json.dump(peticiones, arch_pet, indent=4)

    with open("vecinos.json", "w") as arch_vecinos:
        json.dump(vecinos, arch_vecinos, indent=4)

    print("Préstamo aprobado correctamente")

# DENEGAR PETICIONES================================================================================================================================

def denegar (peticiones):

    if len(peticiones) == 0:
        print ("no hay pedidos... ".upper())
        return

    id_ped = input ("ingrese el id de el pedido que quiere denegar: ")

    while id_ped not in peticiones:
        mensaje = "se ingreso una opcion diferente a un numero o un numero fuera del rango de pedidos en el menu de denegacion de peticiones"
        logs.registrar_evento(mensaje)
        print("ID invalido...")
        id_ped = input ("ingrese el id de el pedido que quiere denegar: ")
    print (f"""\nesta seguro que quiere eliminar el pedido de: 
id del pedido: {peticiones[id_ped]["id del pedido"]}
id del usuario: {peticiones[id_ped]["quien"]}
herramienta: {peticiones[id_ped]["herramienta"]}
cantidad: {peticiones[id_ped]["cantidad"]}
fecha: {peticiones[id_ped]["fecha"]} dias
estado: {peticiones[id_ped]["estado"]}""")

    opcion = input("\nY o N: ").upper()
    
    while opcion not in ["Y", "N"]:
        mensaje = "se ingreso una opcion diferente a Y o N en el menu de denegacion de peticiones"
        logs.registrar_evento(mensaje)
        print ("\nopcion equivocada...")
        opcion = input("Y o N: ").upper()
    
    if opcion == "Y":
        peticiones[id_ped]["estado"] = "denegado"
        with open("peticiones.json", "w") as arch_pet:
            json.dump(peticiones, arch_pet, indent=4)
        print ("\npedido denegado exitosa mente")
    else:
        return


# DESARROLLADOR======================================================================================================================================

def aprovacion_prestamo(peticiones, vecinos, herramientas):


    if len(peticiones) == 0:
        print("\nNo hay préstamos pendientes.")
        return

    print("PRESTAMOS:")

    for i in peticiones:
        print(f"""
    id del prestamo: {peticiones[i]["id del pedido"]}
    id del usuario: {peticiones[i]["quien"]}
    herramienta: {peticiones[i]["herramienta"]}
    cantidad: {peticiones[i]["cantidad"]}
    fecha: {peticiones[i]["fecha"]}
    estado: {peticiones[i]["estado"]}
    ======================================================================""")
    
    print("""QUE DESEARIA HACER

1.) aprobar prestamo

2.) rechazar prestamo

3.) salir """)

    opcion = int(input("\nopcion: "))

    while opcion not in [1, 2, 3]:
        mensaje = "se ingreso una opcion diferente a un numero o un numero fuera del rango de opciones en el menu de aprovacion de prestamos"
        logs.registrar_evento(mensaje)
        print("\nopcion invalida, por favor ingrese una opcion valida")
        input("\npulse cualquier tecla para continuar")
        opcion = int(input("\nopcion: "))

    if opcion == 1:
        aprovar(peticiones, vecinos, herramientas)
    elif opcion == 2:
        denegar(peticiones)
    elif opcion == 3:
        return