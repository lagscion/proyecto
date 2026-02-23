import loggin
import json


with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)

if __name__ == "__main__":
    while True:
        loggin.loggin(vecinos, herramientas)         
