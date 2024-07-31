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


def actualizar_city():
    datos = funciones.cargar_datos()
    clear_screen()
    nombre =input("Ingrese el nombre de la ciudad: ").lower()    
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["nombre"] == nombre:
            while True:
                op = input("Ingrese una opcion:\n    0. Salir \n    1. Nombre\n    2. codigo postal\n    3. Poblacion\n    4. Pais\n\n>>  ")
                if op == "1": 
                    name =  datos["ciudades"][i]["nombre"]
                    datos["ciudades"][i]["nombre"]=input("Ingrese el nuevo nombre de la ciudad: ").lower()
                    es()
                    print_(f"La ciudad ",name," ha sido cambiada a ", datos["ciudades"][i]["nombre"]," con éxito!")
                    funciones.guardar_datos(datos)
                    return
                elif op == "2": 
                    name =  datos["ciudades"][i]["codigo postal"]
                    datos["ciudades"][i]["codigo postal"]=input("Ingrese el nuevo codigo postal de la ciudad: ").lower()
                    es()
                    print_(f"La ciudad ",name," ha sido cambiada a ", datos["ciudades"][i]["codigo postal"]," con éxito!")
                    funciones.guardar_datos(datos)
                    return
                elif op == "3": 
                    name =  datos["ciudades"][i]["poblacion"]
                    datos["ciudades"][i]["poblacion"]=input("Ingrese la nueva poblacion de la ciudad: ")
                    es()
                    print_(f"La poblacion ",name," ha sido cambiada a ", datos["ciudades"][i]["poblacion"]," con éxito!")
                    funciones.guardar_datos(datos)
                    return
                elif op == "4": 
                    name =  datos["ciudades"][i]["pais"]
                    datos["ciudades"][i]["pais"]=input("Ingrese el nuevo pais de la ciudad: ")
                    es()
                    print_(f"El pais ",name," ha sido cambiada a ", datos["ciudades"][i]["pais"]," con éxito!")
                    funciones.guardar_datos(datos)
                    return
                elif op == "0": 
                    funciones.guardar_datos(datos)
                    return
                else: print_("Opcion no valida")
    print(f"La ciudad",nombre,"no existe...")     
    funciones.guardar_datos(datos)
    return

def actualizar_ciudad():
    while True:
        actualizar_city()
        continuar = very()
        if continuar == "2": break
        else: clear_screen()
