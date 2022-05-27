from Contrato import Contrato
#from Equipo import Equipo
from datetime import date
import numpy as np

class ManejadorContratos:
    __cantidad=0
    __dimension=0
    __incremento=5

    def __init__(self, dimension, incremento=5):
        self.__ArregloContratos= np.empty(dimension, dtype=Contrato)
        self.__cantidad=0
        self.__dimension= self.__dimension

    def agregadorContrato(self, contr):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__ArregloContratos.resize(self.__dimension)
        self.__ArregloContratos[self.__cantidad]= contr
        self.__cantidad+= 1

    def cargaContrato(self, jug, equ): #Carga los contratos
        print("----CONTRATO DEL JUGADOR----")
        print("-- {} --" .format(jug))
        print("Inicio de contrato, ingrese los datos en números.")
        dia=int(input("Ingrese el día de inicio de contrato:  "))
        mes=int(input("Ingrese el mes de inicio de contrato:  "))
        anio=int(input("Ingrese el año de inicio de contrato:  "))
        fechainicio=date(anio,mes,dia)
        print("-----------------------------------------------")
        print("Finalización de contrato, ingrese los datos en números.")
        dia=int(input("Ingrese el día de finalización de contrato:  "))
        mes=int(input("Ingrese el mes de finalización de contrato:  "))
        anio=int(input("Ingrese el año de finalización de contrato:  "))
        fechafin=date(anio,mes,dia)
        print("-----------------------------------------------")
        print("Pago mensual del contrato.")
        pago=float(input("Ingrese el pago mensual del jugador:  "))
        contrr=Contrato(fechainicio,fechafin,pago,equ,jug)
        self.agregadorContrato(contrr)
        return contrr
    def mostrar(self):
        for contrato in self.__ArregloContratos:
            print(contrato)



    def cargaArchivo(self): #Carga el archivo con los datos, Nombre del jugador, DNI del jugador, Fecha de inicio de contrato, Fecha de finalización del contrato y el pago mensual
        i=0
        archivo= open("Datos","w")
        archivo.write("Nombre del equipo;DNI;Fecha Inicio;Fecha Finalizacion;Pago mensual")
        archivo.write("\n")
        while i < self.__cantidad:
            nom=str(self.__ArregloContratos[i].getJugador().getNombre())
            dni=str(self.__ArregloContratos[i].getJugador().getDNI())
            ini=str(self.__ArregloContratos[i].getFechaInicio())
            fin=str(self.__ArregloContratos[i].getFechaFin())
            pag=str(self.__ArregloContratos[i].getPagoMensual())
            archivo.write(nom + ";")
            archivo.write(dni + ";")
            archivo.write(ini + ";")
            archivo.write(fin + ";")
            archivo.write(pag + ";")
            archivo.write("\n")
            i+=1
        archivo.close()
