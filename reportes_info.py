import json
with open ("herramientas.json", "r") as archivo:
    herramientas = json.load(archivo)

def low_stock (herramientas):
    for a in herramientas:
        for i in herramientas[a]["id"] :
            while herramientas[i]["stock"] < 3:
                print (f""" *** HERRAMIENTAS CON BAJO STOCK ***
    NOMBRE= {herramientas[i]["nombre"]}
    STOCK= {herramientas[i]["stock"]}  
    """)
                break





#____________________________________________________________________________________________________________________________________________________________
def menu(herramientas):
    print ("""*** BIENVENIDO ***
QUE DESEA VER?:

1. Herramientas con stock bajo (por ejemplo, menos de 3 unidades).
           
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

menu (herramientas)