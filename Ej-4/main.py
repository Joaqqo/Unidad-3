from Coleccion import Coleccion
import os
def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Carga de datos')
        print('\n 2-Estimación de consumición de uso por hora/metro cúbico')
        print('\n 3-Marca y modelo de calefactor gas natural de menor consumo')
        print('\n 4-Marca y modelo de calefactor gas eléctrico de menor consumo')
        print('\n 5-Calefactor de menor consumo')
        print('\n 6-Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            manC.manejadorArchivos()
        if(opcion == 2):
            manC.setValores()
        if(opcion == 3):
            gas=manC.menorCostoGas()
            print("El calefactor de gas natural con menor consumo es: ")
            print(gas)
        if(opcion == 4):
            electrico=manC.menorCostoElectrico()
            print("El calefactor eléctrico con menor consumo es: ")
            print(electrico)
        if(opcion == 5):
            manC.menorTodo()
        if(opcion == 6):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        if(opcion == 7):
            manC.mostrar()
        os.system('cls')

if __name__ == '__main__':
    manC=Coleccion()
    menu()
