import json
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)

def menu ():
    print (f"""  *** ¡¡CLARO!!  ***

que deseas pedir?

1.) martillo:{herramientas["martillo"]["stock"]}

2.) destornillador: {herramientas["destornillador"]["stock"]}




""")

menu()
opcion = input("opcion: ")

while opcion not in ("1","2"):
    print("opcion equivocada, pofavor ingrese una opcion valida...")
    opcion = input("pulse cualquier tecla para continuar: ")
    menu()
print ("good boy")