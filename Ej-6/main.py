from Decodificador import Decodificador

import os

def menu():
    salir = False
    opcion = 0
    while not salir:
        print('\n----------------------MENU DE OPCIONES---------------------')
        print('\n 1-Insertar aparato en una posición determinada')
        print('\n 2-Agregar aparato a la colección')
        print('\n 3-Mostrar que tipo de aparato se encuentra en una posición')
        print('\n 4-Mostrar cantidad de aparatos cuya marca sea Philips')
        print('\n 5-Marca de los lavarropas con carga Superior')
        print('\n 6-Mostrar datos de aparatos')
        print('\n 7-Almacenar los objetos en un archivo json')
        print('\n 8- Salir')
        opcion = int(input('\n Ingrese una OPCION: '))
        if(opcion == 1):
            aparato=lista.cargaAparato()
            if aparato == None:
                print("--- Intente de nuevo ---")
            else:
                posicion=int(input("Ingrese la posición que desea insertar el aparato:  "))
                lista.insertarAparato(aparato, posicion-1)
        if(opcion == 2):
            aparato=lista.cargaAparato()
            if aparato == None:
                print("--- Intente de nuevo ---")
            else:
                lista.agregarAparato(aparato)
                print("¡El aparato fue agregado correctamente! \n")
        if(opcion == 3):
            posicion=int(input("Ingrese la posición que desea ver:  "))
            lista.mostrarAparato(posicion-1)
        if(opcion == 4):
            lista.marcaPhilips()
        if(opcion == 5):
            print("Marca de lavarropas con tipo de carga 'Superior': ")
            lista.lavarropaSuperior()
        if(opcion == 6):
            lista.mostrarPrecios()
        if(opcion == 7):
            d=lista.toJSON()
            decode.guardarJSONArchivo(d, "aparatoselectronicos.json")
            print("¡Los datos se guardaron correctamente!. ")
        if(opcion == 8):
            print("\n FINALIZA EL PROGRAMA \n")
            salir = True
        os.system('cls')

if __name__ == '__main__':
    decode= Decodificador()
    diccionario= decode.leerJSONArchivo("aparatoselectronicos.json")
    lista= decode.decodificarDiccionario(diccionario)
    menu()


