from Flores import Flores
import numpy as np
import csv

class ManejadorFlores:
    __cantidad= 0
    __dimension= 0
    __incremento= 5

    def __init__(self, dimension, incremento=5):
        self.__ArregloFlores= np.empty(dimension, dtype=Flores)
        self.__cantidad= 0
        self.__dimension= dimension

    def agregaFlores(self, flor):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__ArregloFlores.resize(self.__dimension)
        self.__ArregloFlores[self.__cantidad]= flor
        self.__cantidad+= 1

    def ListaparaMax(self): #Crea la lista de enteros con los contadores
        lista=[]
        i=0
        while i < self.__cantidad:
            lista.append(0)
            i+=1
        return lista

    def floresPedidas(self, conts): #Va a retornar una lista con los índices donde estan las flores más vendidas
        mayores=[]
        for i in range(5):
            indice=conts.index(max(conts))
            mayores.append(indice)
            conts[indice]= 0
        return mayores

    def mostrarMayores(self, mayores): #Muestra las flores más vendidas
        print("Las 5 flores más vendidas en órden son: ")
        for i in range(len(mayores)):
            print("NOMBRE: {} - NUM: {}" .format(self.__ArregloFlores[mayores[i]].getNombre(), self.__ArregloFlores[mayores[i]].getNumero()))



    def buscarFlor(self, numero): #Buscador de número de flores
        i=0
        valor=-1
        bandera=True
        while i < self.__cantidad and bandera == True:
            if self.__ArregloFlores[i].getNumero() == numero:
                valor=i
                bandera=False
            i+=1
        return valor

    def getFlor(self, numf): #Para obtener los datos de la flor
        i= self.buscarFlor(numf)
        while i == -1:
            print("Error en el número de flor ingresado, intente de nuevo")
            numf=int(input("Ingrese número de flor:  "))
            i=self.buscarFlor(numf)
        return self.__ArregloFlores[i].getNumero(), self.__ArregloFlores[i].getNombre(), self.__ArregloFlores[i].getColor(), self.__ArregloFlores[i].getDescripcion()



    def mostrar(self):
        for i in range(len(self.__ArregloFlores)):
            print("NUM: {} - FLOR: {}" .format(self.__ArregloFlores[i].getNumero(), self.__ArregloFlores[i].getNombre()))

    def manejadorArchivo(self):
        archivo= open("flores.csv")
        reader= csv.reader(archivo, delimiter=";")
        for i in reader:
            flor=Flores(int(i[0]), str(i[1]), str(i[2]), str(i[3]))
            self.agregaFlores(flor)
        archivo.close()
