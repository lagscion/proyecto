import json
with open ("peticiones.json", "r") as arch_pet:
    peticiones = json.load(arch_pet)
with open ("herramientas.json", "r") as archivo_herr:
    herramientas = json.load(archivo_herr)
with open ("vecinos.json", "r") as archivo_vec:
    vecinos = json.load(archivo_vec)



def menu ():
    


    print (f"""  *** ¡¡CLARO!!  ***

que deseas pedir?

1.) martillo: {herramientas["1"]["stock"]}

2.) destornillador: {herramientas["2"]["stock"]}




""")

def maxim_id():
    if len(peticiones) == 0:
        max_id = 1
    else: 
        max_id = len(peticiones)+1
    return max_id

def peticion (id_usuario):
    menu()
    opcion = input("opcion: ")

    while opcion not in ("1","2"):
        print("opcion equivocada, pofavor ingrese una opcion valida...")
        opcion = input("pulse cualquier tecla para continuar: ")
        menu()

    if opcion == "1":
        cantidad = int (input("\ncuantos desea pedir: "))
        while cantidad > int(herramientas["1"]["stock"])or cantidad == 0  :
            print ("error seleccione una cantidad valida")
            input ("presione cualquier tecla para continuar")
            menu()
            cantidad = int (input("\ncuantos desea pedir: "))
        who = vecinos[id_usuario]["nombre"]
        fecha = input ("cuantos dias se demoraria en retornar la herramienta: ")
        maxim_id()
        peticiones ["martillo"] = {
            "id del pedido" : (maxim_id()),
            "quien" : (who),
            "herramienta" : "destornillador",
            "cantidad" : (cantidad),
            "fecha" : (fecha),
            "estado" : ""
        }
        with open("peticiones.json", "w") as archivo_pet:
            json.dump(peticiones, archivo_pet, indent=4)
        print("\nsu pedido se realizo con exito")

    if opcion == "2":
        cantidad = int (input("\ncuantos desea pedir: "))
        while cantidad > int(herramientas["2"]["stock"])or cantidad == 0  :
            print ("error seleccione una cantidad valida")
            input ("presione cualquier tecla para continuar")
            menu()
            cantidad = int (input("\ncuantos desea pedir: "))
        who = vecinos[id_usuario]["nombre"]
        fecha = input ("cuantos dias se demoraria en retornar la herramienta: ")
        maxim_id()
        peticiones ["destornillador"] = {
            "id del pedido" : (maxim_id()),
            "quien" : (who),
            "herramienta" : "destornillador",
            "cantidad" : (cantidad),
            "fecha" : (fecha),
            "estado" : ""
        }
        with open("peticiones.json", "w") as archivo_pet:
            json.dump(peticiones, archivo_pet, indent=4)
        print("\nsu pedido se realizo con exito")




