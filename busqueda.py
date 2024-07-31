from funciones_segundarias import *
import funciones

def leer_city_nombre():
    datos= funciones.cargar_datos()
    clear_screen()
    nombre =input("Ingrese el nombre de la ciudad: ").lower()
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["nombre"] == nombre:
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
    print_(f"La ciudad ",nombre," no existe...")
    return

def leer_ciudad_nombre():
    while True:
        leer_city_nombre()
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

# ----------------------------

def leer_city_pais():
    datos= funciones.cargar_datos()
    clear_screen()
    nombre =input("Ingrese el nombre del pais: ").lower()
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["pais"] == nombre:
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
    print_(f"La ciudad ",nombre," no existe...")
    return

def leer_ciudad_pais():
    while True:
        leer_city_pais()
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

# ---------------------------------------------

def leer_city_cod():
    datos= funciones.cargar_datos()
    clear_screen()
    nombre =input("Ingrese el codigo postal de la ciudad: ").lower()
    for i in range(len(datos["ciudades"])):
        if datos["ciudades"][i]["codigo postal"] == nombre:
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
    print_(f"La ciudad ",nombre," no existe...")
    return

def leer_ciudad_cod():
    while True:
        leer_city_cod()
        continuar = very()
        if continuar == "2": break
        else: clear_screen()



