from ManejadorFlores import ManejadorFlores
from ManejadorRamo import ManejadorRamo
import os

def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Registrar ramo vendido ')
        print('\n 2-Cinco flores más vendidas ')
        print('\n 3-Flores vendidas por tamaño')
        print('\n 4- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            manR.agregaRamo(manF)
        if(opcion == 2):
            conts=manF.ListaparaMax() #Creo una lista de enteros en 0 que servirán como contadores
            conts=manR.cantFloresenRamos(conts)
            indicmay=manF.floresPedidas(conts) #Indice de los mayores
            manF.mostrarMayores(indicmay) #Muestra las más vendidas
        if(opcion == 3):
            tamanio=input("Ingrese el tamaño de ramo que desea ver:  ")
            manR.mostrarxramo(tamanio)
        if(opcion == 4):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')


if __name__ == '__main__':
    manF= ManejadorFlores(8)
    manR= ManejadorRamo()
    manF.manejadorArchivo()
    menu()
