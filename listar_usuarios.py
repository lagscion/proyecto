import json
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)


def list_usuarios(vecinos):
    with open("vecinos.json", "r") as archivo:
        vecinos = json.load(archivo)
    contador = 0 
    for i in vecinos :
        print (("\nnombre: "),vecinos[i]["nombre"],"\n")
        print (("id: "),vecinos[i]["id"],"\n")
        print (("telefono: "),vecinos[i]["telefono"],"\n")
        print (("direccion: "),vecinos[i]["direccion"],"\n")
        print (("admin: "),vecinos[i]["admin"],"\n")
        print ("================================================")
        contador += 1 



