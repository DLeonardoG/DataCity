import json
from importaciones import *

def main():
    while True:
        diseño_logo()
        print("Bienvenido a Datacity")
        print("----------------------------------------------------")
        print("----------------------------------------------------")
        print("1. Registro de datos de ciudades")
        print("2. Editar registros")
        print("-----------------------------------------------")
        print("3. Mostrar ciudades")
        print("4. Busquedad por nombre")
        print("5. Busquedad por pais")
        print("6. Busquedad por codigo postal")
        print("-----------------------------------------------")
        print("7. Salir")

        opcion = input(">> ")
        if opcion == "1": crear_ciudad()
        elif opcion == "2": actualizar_ciudad()
        elif opcion == "3": leer_ciudades()
        elif opcion == "4": leer_ciudad_nombre()
        elif opcion == "5": leer_ciudad_pais()
        elif opcion == "6": leer_ciudad_cod()
        elif opcion == "7": break
        else: print("Opcion no valida")

main()