from Decodificador import Decodificador
from IElemento import IPersonal
import os




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
        print(' 9- Salir')
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
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')






if __name__ == "__main__":
    decode= Decodificador()
    diccionario= decode.leerJSONArchivo("personal.json")
    lista= decode.decodificarDiccionario(diccionario)
    menu((IPersonal(lista)))
