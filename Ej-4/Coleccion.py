from Calefactor import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactorGasNatural import CalefactorGasNatural
import numpy as np
import csv

class Coleccion:
    __ArregloCalefactores= None

    def __init__(self):
        self.__ArregloCalefactores= None

    def setValores(self):
        est=int(input("Ingrese la cantidad que se estima consumir de Kilowatts/h: "))
        CalefactorElectrico.estimacion=est
        est=int(input("Ingrese la cantidad que se estima consumir de Calorias/metro cúbico: "))
        CalefactorGasNatural.estimacion=est

    def menorCostoGas(self):
        menor=99999
        indice=None #Va a devolver en donde está el menor dato
        for i in range(len(self.__ArregloCalefactores)):
            if type(self.__ArregloCalefactores[i]) == CalefactorGasNatural: #Type devuelve el tipo
                #total=self.__ArregloCalefactores[i].getCalorias() * CalefactorGasNatural.getEstimacion()
                if menor > self.__ArregloCalefactores[i].getCalorias() * CalefactorGasNatural.getEstimacion():
                    indice=self.__ArregloCalefactores[i]
                    menor=self.__ArregloCalefactores[i].getCalorias()*CalefactorGasNatural.getEstimacion()
        return indice

    def menorCostoElectrico(self):
        menor=99999
        indice=None #Va a devolver en donde está el menor dato
        for i in range(len(self.__ArregloCalefactores)):
            if type(self.__ArregloCalefactores[i]) == CalefactorElectrico: #Type devuelve el tipo
                if menor > self.__ArregloCalefactores[i].getKWattH() * CalefactorElectrico.getEstimacion():
                    indice=self.__ArregloCalefactores[i]
                    menor=self.__ArregloCalefactores[i].getKWattH()*CalefactorElectrico.getEstimacion()
        return indice

    def menorTodo(self):
        indiG= self.menorCostoGas()
        indiE= self.menorCostoElectrico()
        if indiG.getCalorias()*CalefactorGasNatural.getEstimacion() < indiE.getWattH()*CalefactorElectrico.getEstimacion():
            print("El calefactor a gas {} {} {} es el que menos consume con {} calorias costo por metros cúbicos." .format(indiG.getMarca(), indiG.getModelo(), indiG.getMatricula(), indiG.getCalorias()))
        else:
            print("El calefactor eléctrico {} {} es el que menos consume con {} costo de kilowatts por hora." .format(indiE.getMarca(), indiE.getModelo(), indiE.getKWattH()))



    def mostrar(self):
        for calefactor in self.__ArregloCalefactores:
            print(calefactor)
        


    def manejadorArchivos(self):
        j= 0 #El índice del arreglo
        cantCal=int(input("Ingrese la cantidad de calefactores: "))
        self.__ArregloCalefactores= np.empty(cantCal, dtype=Calefactor)
        #--------------------------------------------------------------------------------
        archivo=open("calefactor-electrico.csv")
        reader= csv.reader(archivo, delimiter=";")
        for i in reader:
            pmax=int(i[2])
            print("Del calefactor eléctrico {} {}:" .format(i[0], i[1]))
            kwxh=float(input("Costo del kilowatt/h:  "))
            while kwxh*1000 > pmax:
                print("Costo de kilowatt erróneo, ingrese de nuevo.")
                kwxh=float(input("Costo del kilowatt/h:  "))
            electrico=CalefactorElectrico(str(i[0]),str(i[1]),pmax,kwxh)
            self.__ArregloCalefactores[j]= electrico
            j+= 1
        archivo.close()
        print("-----------------------------------------------------------------------")
        #--------------------------------------------------------------------------------
        archivo=open("calefactor-a-gas.csv")
        reader= csv.reader(archivo, delimiter=";")
        for i in reader:
            print("Del calefactor a gas {} {}" .format(i[0], i[1]))
            kcal=int(input("Ingrese el costo de las kilocalorias por metro cúbico:  "))
            gasnat=CalefactorGasNatural(str(i[0]), str(i[1]), str(i[2]), kcal)
            self.__ArregloCalefactores[j]= gasnat
            j+= 1
        archivo.close()
        #--------------------------------------------------------------------------------
