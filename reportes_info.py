import json
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)
with open ("vecinos.json", "r") as archivo:
    vecinos = json.load(archivo)

def low_stock (herramientas):
    for a in herramientas:
        for i in herramientas[a]["id"] :
            while herramientas[i]["stock"] < 3:
                print (f""" *** HERRAMIENTAS CON BAJO STOCK ***
    NOMBRE= {herramientas[i]["nombre"]}
    STOCK= {herramientas[i]["stock"]}  
    """)
                break

#PRESTAMOS ACTIVOS_____________________________________________________________________________________________________________________________________________

def prestamos_activos(vecinos):

    print("\n*** PRÉSTAMOS ACTIVOS ***\n")

    hay_activos = False

    for id_vecino, datos_vecino in vecinos.items():

        prestamos = datos_vecino["prestamo"]

        for id_prestamo, prestamo in prestamos.items():

            if prestamo["estado"] == "activo":
                hay_activos = True
                print(f"Usuario: {datos_vecino['nombre']}")
                print(f"ID Usuario: {id_vecino}")
                print(f"Herramienta: {prestamo['herramienta']}")
                print(f"Cantidad: {prestamo['cantidad']}")
                print(f"Fecha: {prestamo['fecha']}")
                print("-" * 30)

    if not hay_activos:
        print("No hay préstamos activos.")

# HITORIA___________________________________________________________________________________________________________________________________________


def historial(vecinos):

    print("\n*** HISTORIAL ***")

    id_usuario = input("\nIngrese el ID del usuario a revisar: ")

    while id_usuario not in vecinos:
        print("ID erróneo, ingrese un ID válido.")
        id_usuario = input("\nIngrese el ID del usuario a revisar: ")

    prestamos = vecinos[id_usuario]["prestamo"]

    if not prestamos:
        print("\nEste usuario no tiene préstamos registrados.")
        return

    print(f"\nHistorial de {vecinos[id_usuario]['nombre']}\n")

    for id_prestamo, datos in prestamos.items():
        print(f"ID Pedido: {id_prestamo}")
        print(f"Herramienta: {datos['herramienta']}")
        print(f"Cantidad: {datos['cantidad']}")
        print(f"Fecha: {datos['fecha']}")
        print(f"Estado: {datos['estado']}")
        print("-" * 30)

# HERRAMIENTAS MAS SOLICITADAS___________________________________________________________________________________________________________________________
def mas_pedidas(vecinos):
    print("\n*** HERRAMIENTAS MÁS SOLICITADAS ***\n")

    herramientas = [] 


    for datos_vecino in vecinos.values():

        for prestamo in datos_vecino["prestamo"].values():
            herramienta = prestamo["herramienta"]
            cantidad = prestamo["cantidad"]


            for _ in range(cantidad):
                herramientas.append(herramienta)

    if not herramientas:
        print("No hay préstamos registrados.")
        return


    max_solicitudes = 0
    for h in set(herramientas): 
        veces = herramientas.count(h)
        if veces > max_solicitudes:
            max_solicitudes = veces


    for h in set(herramientas):
        if herramientas.count(h) == max_solicitudes:
            print(f"{h} -> {max_solicitudes} solicitudes")

#VECINO CON MAS HERRAMIENTAS SOLICITADAS

def usuario_mas_solicitudes(vecinos, ):
    max_prestamos = 0
    usuario_top = None

    for id_usuario, datos_vecino in vecinos.items():
        cantidad = len(datos_vecino["prestamo"])
        if cantidad > max_prestamos:
            max_prestamos = cantidad
            usuario_top = datos_vecino["nombre"]

    if usuario_top:
        print("\n*** USUARIO CON MÁS SOLICITUDES ***\n")
        print(f"Usuario: {usuario_top}")
        print(f"Cantidad de préstamos: {max_prestamos}")
    else:
        print("No hay usuarios con préstamos registrados.")
#____________________________________________________________________________________________________________________________________________________________
def menu(herramientas, vecinos):
    while True:
        print ("""\n*** BIENVENIDO ***
    QUE DESEA VER?:
    
    1. Herramientas con stock bajo (menos de 3 unidades).
            
    2. Préstamos activos y vencidos.
            
    3. Historial de préstamos de un usuario.
            
    4. Herramientas más solicitadas por la comunidad.
                
    5. Usuarios que más herramientas han solicitado.

    6. SALIR
    """)

        while True:
            try: 
                opcion = int(input ("opcion: "))
                while  opcion not in [1,2,3,4,5,6]:
                    print ("opcion equivocada...")
                    opcion = int(input ("opcion: "))
                break
            except ValueError:
                print(" opcion equivocada...")

        if opcion == 1:
            low_stock(herramientas)
        elif opcion ==2:
            prestamos_activos(vecinos)
        elif opcion == 3:
            historial (vecinos)
        elif opcion == 4:
            mas_pedidas(vecinos)
        elif opcion ==5: 
            usuario_mas_solicitudes(vecinos, )
        else:
            break



