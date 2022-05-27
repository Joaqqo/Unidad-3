from ManejadorEquipos import ManejadorEquipos
from ManejadorContratos import ManejadorContratos
from ManejadorJugadores import ManejadorJugadores

import os


def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Inscribir jugador ')
        print('\n 2-Crear contrato para un jugador')
        print('\n 3-Consultar jugadores contratados')
        print('\n 4-Jugadores con contrato que se vence en 6 meses')
        print('\n 5-Obtener importe de los contratos')
        print('\n 6-Crear archivo con los datos de los contratos')
        print('\n 7- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            manJ.cargaJugador()
        if(opcion == 2):
            dnijug=input("Ingrese el DNI del jugador que desea crear contrato:  ")
            jugador=manJ.buscaJugador(dnijug)
            if jugador == None:
                print("Error en la búsqueda del jugador, intente de nuevo")
            else:
                team=input("Ingrese el equipo en el cual {} jugará:  " .format(jugador.getNombre()))
                equip=manE.buscarEquipo(team)
                if equip == None:
                    print("Error en la búsqueda del equipo, intente de nuevo")
                else:
                    contrt = manC.cargaContrato(jugador, equip)
                    manE.cargarContratoaEquipo(contrt, equip)


        if(opcion == 3):
            dnijug=input("Ingrese el DNI del jugador que desea consultar:  ")
            prueba=manE.jugadoresContratados(dnijug)
            if prueba== False:
                print("No se encontró el jugador ingresado")
            else:
                print("---------------------------------")

        if(opcion == 4):
            team=input("Ingrese el equipo que desea ver los contratos:  ")
            manE.vencContratos(team)
        if(opcion == 5):
            nombre=input("Ingrese el nombre del equipo que desea buscar:  ")
            importetotal=manE.importeContratos(nombre)
            print("El importe total por mes del equipo ingresado es: ${}" .format(importetotal))
        if(opcion == 6):
            manC.cargaArchivo()
            print("El archivo se creó exitosamente.")
        if(opcion == 7):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')


if __name__ == '__main__':
    manE= ManejadorEquipos(5)
    manC= ManejadorContratos(5)
    manJ= ManejadorJugadores()
    manE.manejadorArchivo()
    menu()



