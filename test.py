import json
with open ("dadas_baja.json", "r") as archivo:
    dadas_baja = json.load(archivo)
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)

def  dar_baja (herramientas, dadas_baja):
    while True:
        lista_ids = []
    # print del menu
        print (f"""=== Regisatrar Baja de Herramienta ===
    \nID          nombre         estado    
    ----------------------------------""") 

    #ciclo para sacar los ids
        for id_her, datos in herramientas.items():
            lista_ids.append(herramientas[id_her]["id"])
            print(f"""\n{herramientas[id_her]["id"]}          {herramientas[id_her]["nombre"]}       {herramientas[id_her]["estado"]}""")


    #se pregunta por el id de la herrmienta
        id = input ("\nIngrese el ID de la herramienta que quiere dar de baja: ")
        while id not in lista_ids:
            print ("id equivocado porfavor ingrese uno nuevo....")
            id = input("\nID: ")
        fecha = input ("\ningrese la fecha de dado de baja con el formato (YYYY-MM-DD): ")
        motivo = input("\ningrese el motivo de la dada de baja: ")
        if herramientas[id]["estado"] == "dado de baja":
            print ("\nla herramienta ya fue dada de baja posterior mente")
            break
        else:
            dadas_baja[id] = {
                "id_herramienta" :  herramientas[id]["id"],
                "nombre" : herramientas[id]["nombre"],
                "estado" : "dada de baja",
                "fecha_baja" : fecha,
                "motivo" : motivo
            }
            with open("dadas_baja.json", "w") as archivo:
                json.dump ( dadas_baja, archivo, indent = 4)
            print ("herramienta dada de baja exitosa mente")
        confirmacion = input ("desea dar de baja a otra herramienta? S o N ").upper()
        while confirmacion not in ["Y", "N"]:
            print("opcion equivocada")
            confirmacion = input ("desea dar de baja a otra herramienta? S o N ").upper()
        if confirmacion == "Y":
            pass
        else:
            break















dar_baja(herramientas, dadas_baja)