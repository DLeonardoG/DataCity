import json
import funciones
from funciones_segundarias import *

def crear_city():
    datos = funciones.cargar_datos()
    ciudades={}
    clear_screen()
    ciudades["nombre"]=input("Ingrese el nombre de la ciudad: ").lower()
    ciudades["codigo postal"]=input("Ingrese el codigo postal: ").lower()
    ciudades["poblacion"]=input("Ingrese poblacion de la ciudad: ").lower()
    ciudades["pais"]=input("Ingrese el pais: ")
    
    datos["ciudades"].append(ciudades)
    print(ciudades["nombre"]," ha sido registrada con éxito!")
    funciones.guardar_datos(datos)
    return

def crear_ciudad():
    while True:
        crear_city()
        continuar = very()
        if continuar == "2": break
        else: clear_screen()



