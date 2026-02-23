import json
import logs
def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def devoluciones(id_usuario, vecinos, herramientas):

    print(f"""*** BIENVENIDO {(vecinos[id_usuario]["nombre"]).upper()}***

TUS PRESTAMOS:
""")

    prestamos_usuario = vecinos[id_usuario]["prestamo"]

    if not prestamos_usuario:
        mensaje = "se intento realizar una devolucion sin tener prestamos registrados"
        logs.registrar_evento(mensaje)
        print("No tienes prestamos registrados.")
        return

    for id_pedido in prestamos_usuario:
        pedido = prestamos_usuario[id_pedido]

        if pedido["estado"] == "aprobado":
            print(f"""
ID del pedido: {pedido["id del pedido"]}
Herramienta: {pedido["herramienta"]}
Cantidad: {pedido["cantidad"]}
Dias : {pedido["fecha"]} dias
Estado: {pedido["estado"]}
""")

    prestamo = input("Ingrese el ID del prestamo que quisiera completar: ")
    devolucion = input("¿Deseas entregar la herramienta ya? Y o N: ").upper()

    while devolucion not in ["Y", "N"]:
        mensaje = "se ingreso una opcion diferente a Y o N en el menu de devoluciones"
        logs.registrar_evento(mensaje)
        print("Opción inválida.")
        devolucion = input("¿Deseas entregar la herramienta ya? Y o N: ").upper()

    if devolucion == "Y":

        if prestamo in prestamos_usuario:

            pedido = prestamos_usuario[prestamo]

            if pedido["estado"] == "aprobado":

                for id_herramienta in herramientas:
                    if herramientas[id_herramienta]["nombre"] == pedido["herramienta"]:
                        herramientas[id_herramienta]["stock"] += pedido["cantidad"]
                        break

                pedido["estado"] = "entregado"

                guardar_json("vecinos.json", vecinos)
                guardar_json("herramientas.json", herramientas)

                print("Devolución realizada correctamente.")

            else:
                mensaje = "se intento realizar una devolucion de un prestamo que no estaba aprobado o ya habia sido devuelto"
                logs.registrar_evento(mensaje)
                print("El préstamo no está aprobado o ya fue devuelto.")

        else:
                mensaje = "se intento realizar una devolucion con un id de prestamo inexistente"
                logs.registrar_evento(mensaje)
                print("ID de préstamo no encontrado.")