import json
import peticiones
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)

def print_menu_norm(id_usuario):
    print(f"""\n *** BIENVENID@ {(vecinos[id_usuario]["nombre"]).upper()} ***
            
Que desea?
            
1. consultar el estado de las herramienta
            
2. solicitud de herramienta
            
3. salir

""")



def menu_norm (id_usuario):
    print_menu_norm(id_usuario)

    while True:
        try:
            opcion = int(input("\nopcion : "))
            if opcion == 1:
                estado = {herramientas[i]["nombre"]:herramientas[i]["estado"] for i in herramientas}
                print ("\n",estado)
                print_menu_norm(id_usuario)
            elif opcion ==2:
                peticiones.peticion(id_usuario)
                print_menu_norm (id_usuario)
            elif opcion ==3:
                break
            else:
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                menu_norm(id_usuario)
            

        except ValueError:
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_norm(id_usuario)

############################################################################################################################################################################

def menu_admin(id_usuario):
    print_menu_admin(id_usuario)
    while True:
        try:
            opcion = int(input("\nopcion : "))
            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            else:
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                print_menu_admin(id_usuario)

        except ValueError:
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_admin(id_usuario)




def print_menu_admin(id_usuario):
    print(f"""\n *** BIENVENID@ {(vecinos[id_usuario]["nombre"]).upper()} ***

Que desea?

1. Crear usuario

2. Listar usuarios

3. Buscar usuario por ID

4. Actualizar usuario

5. Eliminar o inactivar usuario

""")