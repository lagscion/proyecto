import json
import peticiones as peticiones_module
import agregar_usuarios
import listar_usuarios
import buscar_usuario
import actualizar_usuario  
import loggin
import eliminar_usuario
import gestion_herramientas
import devoluciones

with open("peticiones.json", "r") as arch_pet:
    peticiones_data = json.load(arch_pet)
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)

def print_menu_norm(id_usuario, vecinos, ):
    print(f"""\n *** BIENVENID@ {(vecinos[id_usuario]["nombre"])} ***
            
Que desea?
            
1. consultar el estado de las herramienta
            
2. solicitud de herramienta
            
3. devover herramienta
            
4.) salir

""")



def menu_norm(id_usuario, herramientas, vecinos, peticiones_data):
    print_menu_norm(id_usuario, vecinos)

    while True:
        try:
            opcion = int(input("\nopcion : "))
            if opcion == 1:
                estado = {herramientas[i]["nombre"]:herramientas[i]["estado"] for i in herramientas}
                print ("\n",estado)
                print_menu_norm(id_usuario, vecinos)
            elif opcion ==2:
                peticiones_module.peticion(id_usuario, herramientas)
                print_menu_norm (id_usuario, vecinos)
            elif opcion == 3:
                with open("vecinos.json", "r") as arch_vec:
                    vecinos_actualizados = json.load(arch_vec)
                devoluciones.devoluciones(id_usuario, vecinos_actualizados, herramientas)
                print_menu_norm (id_usuario, vecinos)
            elif opcion == 4 :
                loggin.loggin(vecinos, herramientas)
            else:
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                menu_norm(id_usuario, herramientas, vecinos, peticiones_data)
            

        except ValueError:
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_norm(id_usuario, vecinos)

############################################################################################################################################################################

def menu_admin(id_usuario, vecinos, herramientas, peticiones_data):
    
    print_menu_admin(id_usuario, vecinos)
    while True:
        try:
            opcion = int(input("\nopcion : "))
            if opcion == 1:
                agregar_usuarios.crear_usuario()
                print_menu_admin(id_usuario)
            elif opcion == 2:
                listar_usuarios.list_usuarios(vecinos)
                print_menu_admin(id_usuario)
            elif opcion == 3:
                buscar_usuario.buscar_usuario(vecinos)
                print_menu_admin(id_usuario)
            elif opcion == 4:
                actualizar_usuario.act_usu(vecinos)
                print_menu_admin(id_usuario)
            elif opcion == 5:
                eliminar_usuario.eliminar_usuario(vecinos, id_usuario)
                print_menu_admin(id_usuario)
            elif opcion == 6:
                gestion_herramientas.manejo_h (herramientas)
            elif opcion == 7:
                peticiones_module.aprovacion_prestamo(peticiones_data, vecinos)
            elif opcion == 8:
                loggin.loggin(vecinos, herramientas)
            else:
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                print_menu_admin(id_usuario)

        except ValueError:
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_admin(id_usuario)




def print_menu_admin(id_usuario, vecinos):
    with open ("vecinos.json", "r") as archivo:
        vecinos = json.load(archivo)
    print(f"""\n *** BIENVENID@ {(vecinos[id_usuario]["nombre"]).upper()} ***

Que desea?

1. Crear usuario

2. Listar usuarios

3. Buscar usuario por ID

4. Actualizar usuario

5. Eliminar o inactivar usuario

6. gestion de herramientas

7. solicitudes

8. salir

""")