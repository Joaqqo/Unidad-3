from Decodificador import Decodificador
from IElemento import IPersonal
from ITesorero import ITesorero
from IDirector import IDirector

import os

def menuGastos(list):
    salir = False
    opcion = 0
    while not salir:
        print('\n BIENVENIDO')
        print('\n----------------Opciones de Tesorero----------------')
        print('\n 1-Consultar sueldo del personal')
        print('\n 2-Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            cuil= int(input("Ingrese el CUIL del personal que desea consultar sueldo:  "))
            list.gastosSueldoPorEmpleado(cuil)
        if(opcion == 2):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True

def menuDirector(list):
    salir = False
    opcion = 0
    while not salir:
        print('\n BIENVENIDO')
        print('\n----------------Opciones de Director----------------')
        print('\n 1-Modificar el sueldo básico de un Personal')
        print('\n 2-Modificar cargo')
        print('\n 3-Modificar categoría')
        print('\n 4-Modificar importe extra')
        print('\n 5- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            cuil= int(input("Ingrese el CUIL del personal que desea modificar:  "))
            sueldob=float(input("Ingrese el nuevo sueldo básico del personal:  "))
            list.modificarBasico(cuil,sueldob)
        if(opcion == 2):
            cuil= int(input("Ingrese el CUIL del personal que desea modificar:  "))
            cargo=input("Ingrese el nuevo cargo del personal:  ")
            while cargo.lower() != "exclusivo" and cargo.lower() != "semiexclusivo" and cargo.lower() != "simple":
                print("Error con el cargo ingresado, intente de nuevo.")
                cargo=input("Ingrese el nuevo cargo del personal:  ")
            list.modificarCargo(cuil, cargo)
        if(opcion == 3):
            cuil= int(input("Ingrese el CUIL del personal que desea modificar:  "))
            categoria=int(input("Ingrese la nueva categoría del Personal:  "))
            while categoria < 1 or categoria > 22:
                print("Error con la categoría ingresada, intente de nuevo.")
                categoria=int(input("Ingrese la nueva categoría del Personal:  "))
            list.modificarCategoria(cuil,categoria)
        if(opcion == 4):
            cuil= int(input("Ingrese el CUIL del personal que desea modificar:  "))
            extra=float(input("Ingrese el nuevo importe extra del personal:  "))
            list.modificarImporteExtra(cuil,extra)
        if(opcion == 5):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True



def menu(lista):
    salir = False
    opcion = 0
    while not salir:
        print('----------------------MENU DE OPCIONES---------------------')
        print(' 1-Insertar personal a la colección')
        print(' 2-Agregar personal a la colección')
        print(' 3-Tipo de personal en la posición ingresada')
        print(' 4-Listado de nombres con carrera ingresada de Docentes Investigadores')
        print(' 5-Cantidad de investigadores en el área ingresada')
        print(' 6-Listado de apellidos ordenado y su sueldo')
        print(' 7-Muestra los datos pedidos dada una categoría')
        print(' 8-Creación de archivo personal.json')
        print('--------------OPCIONES PARA TESORERO Y DIRECTOR-------------')
        print(' 9-Gastos de la empresa(Tesorero)')
        print(' 10-Menú de opciones (Director)')
        print(' 11- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            personal=lista.cargaPersonal()
            if personal == None:
                print("-Error, intente de nuevo-")
            else:
                posicion=int(input("Ingrese la posición donde desea insertar el personal:  "))
                lista.insertarPersonal(personal, posicion)
        if(opcion == 2):
            personal=lista.cargaPersonal()
            if personal == None:
                print("-Error, intente de nuevo-")
            else:
                lista.agregarPersonal(personal)
        if(opcion == 3):
            posicion=int(input("Ingrese la posición que desea ver:  "))
            lista.mostrarPersonal(posicion-1)
        if(opcion == 4):
            carrera=input("Ingrese la carrera que desea ver:  ")
            lista.mostrarCarrera(carrera)
        if(opcion == 5):
            area=input("Ingres el area que desea ver:  ")
            lista.contadorAreas(area)
        if(opcion == 6):
            lista.listadoApellidos()
        if(opcion == 7):
            categoria=int(input("Ingrese la categoría que desea revisar el importe total (Del 1 al 5):  "))
            while categoria < 1 or categoria > 5:
                print("Error, intente de nuevo.")
                categoria=int(input("Ingrese la categoría que desea revisar el importe total (Del 1 al 5):  "))
            lista.muestraCategoria(categoria)
        if(opcion == 8):
            d=lista.toJSON()
            decode.guardarJSONArchivo(d, "personal.json")
            print("¡El archivo se creó exitosamente!")
        if(opcion == 9):
            cuenta=lista.Login()
            if cuenta[0] == "uTesorero" and cuenta[1] == "ag@74ck":
                print("Bienvenido, Tesorero...")
                print("Ingresando...")
                menuGastos(ITesorero(lista))
            else:
                print("Error en Usuario/Contraseña, intente de nuevo.")
        if(opcion == 10):
            cuenta=lista.Login()
            if cuenta[0] == "uDirector" and cuenta[1] == "ufC77#!1":
                print("Bienvenido, Director...")
                print("Ingresando...")
                menuDirector(IDirector(lista))
            else:
                print("Error en Usuario/Contraseña, intente de nuevo.")
        if(opcion == 11):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')
        if(opcion == 12):
            cuil=int(input("Ingrese cuil:  "))
            persona=lista.buscarPersonal(cuil)
            print(persona)







if __name__ == "__main__":
    decode= Decodificador()
    diccionario= decode.leerJSONArchivo("personal.json")
    lista= decode.decodificarDiccionario(diccionario)
    menu((IPersonal(lista)))
