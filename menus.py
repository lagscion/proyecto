import json
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)

def print_menu_norm():
    print("""\n *** BIENVENIDO ***
            
Que desea?
            
1. consultar el estado de las herramienta
            
2. solicitud de herramienta

""")



def menu_norm ():
    print_menu_norm()

    while True:
        try:
            opcion = int(input("\nopcion : "))
            if opcion == 1:
                estado = {i: herramientas[i]["estado"] for i in herramientas}
                print ("\n",estado)
                print_menu_norm()
            elif opcion ==2:
                print("talvez")
            else:
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                menu_norm()

        except ValueError:
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_norm()

############################################################################################################################################################################

def menu_admin():
    print_menu_admin()
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
                menu_norm()

        except ValueError:
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            menu_norm()




def print_menu_admin():
    print("""\n *** BIENVENIDO ***
Que desea?

1.Crear usuario

2. Listar usuarios

3. Buscar usuario por ID

4. Actualizar usuario

5. Eliminar o inactivar usuario

opcion : """)