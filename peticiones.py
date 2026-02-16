
import json
with open ("peticiones.json", "r") as arch_pet:
    peticiones = json.load(arch_pet)
with open ("herramientas.json", "r") as archivo_herr:
    herramientas = json.load(archivo_herr)
with open ("vecinos.json", "r") as archivo_vec:
    vecinos = json.load(archivo_vec)



def menu (id_usuario, herramientas):
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


def maxim_id():
    if not peticiones:
        return "1"
    return str(max(map(int, peticiones.keys())) + 1)


def peticion (id_usuario, herramientas):
    while True :

        menu(id_usuario, herramientas)
        opcion = (input("ID de la herramienta a presar: "))

        while int(opcion) < 1 or len(herramientas) < int(opcion) :
            print("opcion equivocada, pofavor ingrese una opcion valida...")
            input("pulse cualquier tecla para continuar: ")
            opcion = input("ID de la herramienta a presar: ")
        while opcion not in herramientas:
            print("opcion equivocada, pofavor ingrese una opcion valida...")
            input("pulse cualquier tecla para continuar: ")
            opcion = input("ID de la herramienta a presar: ")

        cantidad = int(input("ingrese la cantidad de herramientas a  prestar: "))
        while cantidad > herramientas[opcion]["stock"] or cantidad < 1:
            print("cantidad invalida, porfavor ingrese una cantidad valida ...")
            input("pulse cualquier tecla para continuar: ")
            cantidad = int(input("ingrese la cantidad de herramientas a  prestar: "))

        herramienta = herramientas[opcion]["nombre"]

        while True:
            try:  
                fecha = int(input("ingrese el numero aprox dias en los que devolveria la herramienta: "))
                break
            except ValueError:
                print("ingrese un valor valido")
            

        peticiones[maxim_id()] = {
            "id del pedido" : str(maxim_id()),
            "quien" : id_usuario,
            "herramienta" : herramienta,
            "cantidad" : cantidad,
            "fecha" : fecha,
            "estado" : ""

        }

        with open("peticiones.json", "w") as archivo_pet:
            json.dump(peticiones, archivo_pet, indent=4)
        print("\nsu pedido se realizo con exito")

        with open ("herramientas.json", "r") as archivo_herr:
            herramientas = json.load(archivo_herr)

        break

#APROVACIONES=================================================================================================================================================
def aprovar(peticiones, vecinos, herramientas):
    with open ("peticiones.json", "r") as arch_pet:
        peticiones = json.load(arch_pet)
    with open ("herramientas.json", "r") as archivo_herr:
        herramientas = json.load(archivo_herr)
    with open ("vecinos.json", "r") as archivo_vec:
        vecinos = json.load(archivo_vec)

    id_apro = input ("ingrese el ID del pedido que quisiera  aprovar: ")
    while id_apro not in peticiones:
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
        print("Error: herramienta no encontrada")
        return

    if herramientas[id_herramienta]["stock"] < cantidad:
        print("No hay suficiente stock")
        return

    pedido["estado"] = "aprobado"

    herramientas[id_herramienta]["stock"] -= cantidad

    if "prestamo" not in vecinos[id_usuario]:
        vecinos[id_usuario]["prestamo"] = {}

    vecinos[id_usuario]["prestamo"][id_apro] = pedido

    del peticiones[id_apro]

    with open("peticiones.json", "w") as arch_pet:
        json.dump(peticiones, arch_pet, indent=4)

    with open("vecinos.json", "w") as arch_vec:
        json.dump(vecinos, arch_vec, indent=4)

    with open("herramientas.json", "w") as arch_her:
        json.dump(herramientas, arch_her, indent=4)

    print("Préstamo aprobado correctamente")

# DENEGAR PETICIONES================================================================================================================================

def denegar (peticiones):

    if len(peticiones) == 0:
        print ("no hay pedidos... ".upper())
        return

    id_ped = input ("ingrese el id de el pedido que quiere denegar: ")

    while id_ped not in peticiones:
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

def aprovacion_prestamo(peticiones, vecinos):

    with open("peticiones.json", "r") as arch_pet:
        peticiones = json.load(arch_pet)

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
        print("\nopcion invalida, por favor ingrese una opcion valida")
        input("\npulse cualquier tecla para continuar")
        opcion = int(input("\nopcion: "))

    if opcion == 1:
        aprovar(peticiones, vecinos, herramientas)
    elif opcion == 2:
        denegar(peticiones)
    elif opcion == 3:
        return