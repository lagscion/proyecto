
def menu_norm ():

    print("""\n *** BIENVENIDO ***
          
Que desea?
          
1. consultar el estado de las herramienta
          
2. solicitud de herramienta

 """)
    while True:
        try:
            opcion = int(input("opcion : "))
            if opcion == 1:
                print("si")
            elif opcion ==2:
                print("talvez")
            else:
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                print_menu_norm()

        except ValueError:
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_norm()



def menu_admin():
    print(""" *** BIENVENIDO ***
Que desea?

1.Crear usuario

2. Listar usuarios

3. Buscar usuario por ID

4. Actualizar usuario

5. Eliminar o inactivar usuario
opcion : """)

def print_menu_norm():
        print(""" *** BIENVENIDO ***
Que desea?
1. consultar el estado de las herramienta
2. solicitud de herramienta

""")