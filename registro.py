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

def leer_citys():
    datos = funciones.cargar_datos()
    clear_screen()
    print_("Ciudades")
    linea()
    for sn in range(len(datos["ciudades"])):
        print_(datos["ciudades"][sn]["nombre"].capitalize())
    linea()
    for i in range(len(datos["ciudades"])):
        linea()
        es()
        # line()
        print_("Nombre ciudad: ",datos["ciudades"][i]["nombre"].capitalize())
        # line()
        es()
        # line()
        print_("Codigo postal: ",datos["ciudades"][i]["codigo postal"].capitalize())
        # line()
        es()
        # line()
        print_("Poblacion : ",datos["ciudades"][i]["poblacion"])
        # line()
        es()
        # line()
        print_("Pais: ",datos["ciudades"][i]["pais"].capitalize())
        # line()
        es()
        linea()
    return

def leer_ciudades():
    while True:
        leer_citys()
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

