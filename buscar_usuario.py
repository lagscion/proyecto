import json


def buscar_usuario(vecinos):

    with open ("vecinos.json", "r") as archivo:
        vecinos = json.load(archivo)

    id_busc = input("ingrese el id del usuario que planea buscar: ")

    while id_busc not in vecinos:
        print("id inexistente, porfavor ingrese un id valido: ")
        input("presione cualquier tecla para continuar: ")
        id_busc = input("ingrese el id del usuario que planea buscar: ")

    if id_busc in vecinos:
        usuario = vecinos[id_busc]
        print("\nUsuario encontrado:")
        print("\nNombre:", usuario["nombre"])
        print("\nID:", usuario["id"])
        print("\nTeléfono:", usuario["telefono"])
        print("\nDirección:", usuario["direccion"])
        print("\nAdmin:", usuario["admin"])
