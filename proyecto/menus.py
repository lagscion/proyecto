
import peticiones as peticiones_module
import agregar_usuarios
import listar_usuarios
import buscar_usuario
import actualizar_usuario  
import eliminar_usuario
import gestion_herramientas
import devoluciones
import reportes_info
import logs

def print_menu_norm(id_usuario, vecinos, ):
    print(f"""\n *** BIENVENID@ {(vecinos[id_usuario]["nombre"])} ***
            
Que desea?
            
1. consultar el estado de las herramienta
            
2. solicitud de herramienta
            
3. devover herramienta
            
4.) salir

""")



def menu_norm(id_usuario, vecinos, herramientas, peticiones_data):

    while True:
        try:
            print_menu_norm(id_usuario, vecinos)
            
            opcion = int(input("\nopcion : "))
            if opcion == 1:
                estado = {herramientas[i]["nombre"]:herramientas[i]["estado"] for i in herramientas}
                print ("\n",estado)
                print_menu_norm(id_usuario, vecinos)
            elif opcion ==2:
                peticiones_module.peticion(id_usuario, herramientas, vecinos, peticiones_data)
                print_menu_norm (id_usuario, vecinos)
            elif opcion == 3:
                devoluciones.devoluciones(id_usuario, vecinos, herramientas)
                print_menu_norm (id_usuario, vecinos)
            elif opcion == 4 :
                break
            else:
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                print_menu_norm(id_usuario, vecinos)

        except ValueError:
            mensaje = "se ingreso una opcion diferente a un numero en el menu de usuario normal"
            logs.registrar_evento(mensaje)
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_norm(id_usuario, vecinos)

############################################################################################################################################################################

def menu_admin(id_usuario, vecinos, herramientas, peticiones_data):
    while True:
        try:
            print_menu_admin(id_usuario, vecinos)
            opcion = int(input("\nopcion : "))
            if opcion == 1:
                agregar_usuarios.crear_usuario(vecinos)
            elif opcion == 2:
                listar_usuarios.list_usuarios(vecinos)
            elif opcion == 3:
                buscar_usuario.buscar_usuario(vecinos)
            elif opcion == 4:
                actualizar_usuario.act_usu(vecinos)
            elif opcion == 5:
                eliminar_usuario.eliminar_usuario(vecinos, id_usuario)
            elif opcion == 6:
                gestion_herramientas.manejo_h (herramientas)
            elif opcion == 7:
                peticiones_module.aprovacion_prestamo(peticiones_data, vecinos, herramientas)
            elif opcion == 8:
                reportes_info.menu(herramientas, vecinos)
            elif opcion == 9:
                break
            else:
                mensaje = "se intento ingresar una opcion invalida en el menu de administrador"
                logs.registrar_evento(mensaje)
                print("\ningrese una opcion valida")
                input("\npresione cualquier tecla para continuar...")
                print_menu_admin(id_usuario)

        except ValueError:
            mensaje = "se ingreso una opcion diferente a un numero en el menu de administrador"
            logs.registrar_evento(mensaje)
            print("ingrese una opcion valida")
            input("presione cualquier tecla para continuar...")
            print_menu_admin(id_usuario)




def print_menu_admin(id_usuario, vecinos):

    print(f"""\n *** BIENVENID@ {(vecinos[id_usuario]["nombre"]).upper()} ***

Que desea?

1. Crear usuario

2. Listar usuarios

3. Buscar usuario por ID

4. Actualizar usuario

5. Eliminar o inactivar usuario

6. gestion de herramientas

7. solicitudes

8. reportes o informacion

9. salir
""")