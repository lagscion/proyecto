import json
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)

nombre = input ("ingrese el nombre del nuevo usuario: ")


while True:
    try:
        id = int(input("Ingrese el nuevo ID del usuario: "))
        id = str(id)  
        break
    except ValueError:
        print("ID inválido...")


if id in vecinos:
    print("Ese ID ya existe. No se puede registrar.")
    exit()


while True:
    try:
        telefono = int(input("ingrese el numero de telefono del nuevo usuario: "))
        break
    except ValueError:
        print("opcion incorrecta...")
        input ("presione cualquier tecla para continuar: ")

direccion = input("ingrese la direccion del nuevo usuario: ")

admin = input("el usuario tiene permisos de administracion? Y o N: ").upper()
while admin not in ["Y", "N"]:
    print("opcion incorrecta...")
    admin = input("el usuario tiene permisos de administracion? Y o N: ").upper()

if admin == "Y":
    admin = True
else: 
    admin = False

vecinos[id] = {
    "nombre": nombre,
    "id": id,
    "telefono": telefono,
    "direccion": direccion,
    "admin": admin
}

if id in vecinos:
    print("Ese ID ya existe.")
