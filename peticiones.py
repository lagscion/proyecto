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
        vecinos_list = [vecinos[i]["nombre"] for i in vecinos]
        while who not in vecinos_list:
            print("no hay algun usuario con este nombre")
            input("presione cualquier tecla para continuar")
            who = input("\na nombre de quien es la peticion: ")

        peticiones ["martillo"] = {
            "id del usuario" : (vecinos[id_usuario]["nombre"]),
            "cantidad" : (cantidad),
            "quien" : (who)
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
        vecinos_list = [vecinos[i]["nombre"] for i in vecinos]
        while who not in vecinos_list:
            print("no hay algun usuario con este nombre")
            input("presione cualquier tecla para continuar")
            who = input("\na nombre de quien es la peticion: ").lower()

        peticiones ["destornillador"] = {
            "cantidad" : (cantidad),
            "quien" : (who)
        }
        with open("peticiones.json", "w") as archivo_pet:
            json.dump(peticiones, archivo_pet, indent=4)
        print("\nsu pedido se realizo con exito")




