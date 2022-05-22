from ManejadorFacultad import ManejadorFacultad
import os


def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Facultad, nombre de carreras y duración')
        print('\n 2-Código de carrera, nombre y localidad de la Facultad a la cual pertenece esa carrera')
        print('\n 3- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            code=int(input("Ingrese el código de la facultad que desea ver sus carreras:  "))
            ban=manF.mostrarcode(code)
            if ban == False:
                print("No se encontró el código ingresado. Intente de nuevo")
        if(opcion == 2):
            nombr=(input("Ingrese el nombre:  "))
            ban=manF.buscar(nombr)
            if ban == True:
                print("No se encontró el nombre ingresado. Intente de nuevo.")
        if(opcion == 3):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')
if __name__ == '__main__':
    manF=ManejadorFacultad()
    manF.manejadorArchivo()
    menu()
