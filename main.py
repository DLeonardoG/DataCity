import json

def main():
    while True:
        print("Bienvenido a Datacity")
        print("1. registro de datos de ciudades")
        print("2. Editar registros")
        print("-----------------------------------------------")
        print("3. mostrar registros")
        print("4. mostrar registros por poblacion mayor")
        print("5. mostrar registros por poblacion menor")
        print("-----------------------------------------------")
        print("6. busquedad por nombre")
        print("7. busquedad por pais")
        print("8. busquedad por codigo postal")
        print("-----------------------------------------------")
        print("9. salir")
        try:
            opt=int(input("ingrese su opcion: "))
            if opt==1:
                
            elif opt==2:
            elif opt==3:
            elif opt==4:
            elif opt==5:
            elif opt==6:
            elif opt==7:
            elif opt==8:
            elif opt==9:
                break
            else:
                print("La opcion que ingresaste no esta disponible.")
        except Exception:
            print("Error introducciste un valor no valido")