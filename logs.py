import datetime

def registrar_evento(mensaje):
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log = f"[{fecha_hora}] {mensaje}\n"
    with open("registro_eventos.txt", "a") as archivo:
        archivo.write(log)