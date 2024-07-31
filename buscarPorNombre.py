from funciones_segundarias import *
import funciones

def leer_city():
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
            return datos
    print_(f"La ciudad ",nombre," no existe...")
    funciones.guardar_datos(datos)
    return

def leer_ciudad():
    while True:
        leer_city()
        continuar = very()
        if continuar == "2": break
        else: clear_screen()

leer_ciudad()