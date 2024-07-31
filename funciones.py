import json

def leer_crear_json():
    try:
        with open("json\\datos.json","r") as lectura:
            datos = json.load(lectura)
            return datos
    except FileNotFoundError:
        return {}

def guardar_actualizar_json(datos):
    with open("json\\datos.json","w") as guardar:
        json.dump(datos,guardar, indent=4)
    print("\n...GUARDANDO...\n")