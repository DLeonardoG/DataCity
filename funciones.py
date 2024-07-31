import json

def cargar_datos():
    try:
        with open("datos.json","r") as lectura:
            datos = json.load(lectura)
            return datos
    except FileNotFoundError:
        return {
            "ciudades":[]
        }

def guardar_datos(datos):
    with open("datos.json","w", encoding="utf-8") as guardar:
        json.dump(datos,guardar, indent=4)
    print("\n...GUARDANDO...\n")