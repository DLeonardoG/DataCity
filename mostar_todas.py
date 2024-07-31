import funciones
from funciones_segundarias import *

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
leer_ciudades()