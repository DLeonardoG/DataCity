import json
from importaciones import *

def main():
    while True:
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
        try:
            opt=int(input("Ingrese su opcion: "))
            if opt==1:
            elif opt==2:
            elif opt==3:
            elif opt==4:
            elif opt==5:
            elif opt==6:
            elif opt==7:
                break
            else:
                print("La opcion que ingresaste no esta disponible.")
        except Exception:
            print("Error introducciste un valor no valido")