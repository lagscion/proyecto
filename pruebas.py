import json

with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)

# herramienta = []
# for claves in herramientas:
#     herramienta.append(claves)

estado = {i: herramientas[i]["estado"] for i in herramientas}

print (estado)
