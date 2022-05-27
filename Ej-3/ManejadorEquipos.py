from Equipo import Equipo
import numpy as np
import csv
from datetime import date

class ManejadorEquipos:
    __cantidad=0
    __dimension=0
    __incremento=5

    def __init__(self, dimension, incremento=5):
        self.__ArregloEquipos= np.empty(dimension, dtype=Equipo)
        self.__cantidad= 0
        self.__dimension= dimension

    def agregadorEquipo(self, team):
        if self.__cantidad == self.__dimension:
            self.__dimension+= self.__incremento
            self.__ArregloEquipos.resize(self.__dimension)
        self.__ArregloEquipos[self.__cantidad]= team
        self.__cantidad+= 1

    def buscarEquipo(self, team): #Para buscar el equipo
        i=0
        bandera=False
        equip=False
        while i < self.__cantidad and not bandera:
            if self.__ArregloEquipos[i].getNombre().lower() == team.lower():
                equip=self.__ArregloEquipos[i]
                bandera=True
            i+=1
        return equip

    def jugadoresContratados(self, dni): #Consultar jugadores contratados
        i, j= 0, 0
        bandera=False
        while i < self.__cantidad and not bandera:
            j=0
            while j < len(self.__ArregloEquipos[i].getContrato()) and not bandera:
                if self.__ArregloEquipos[i].getContrato()[j].getJugador().getDNI() == dni:
                    print("Nombre del equipo y fecha de finalización del contrato del jugador con DNI {}:" .format(dni))
                    print(self.__ArregloEquipos[i].getNombre())
                    print(self.__ArregloEquipos[i].getContrato()[j].getFechaFin())
                    bandera=True
                j+=1
            i+=1
        return bandera

    def importeContratos(self, nom): #El importe total por mes de los equipos x contratos
        total=0
        equipo=self.buscarEquipo(nom)
        if equipo == False:
            print("Error con el equipo ingresado, intente de nuevo.")
        else:
            for i in range(len(equipo.getContrato())):
                total+=equipo.getContrato()[i].getPagoMensual()
        return total

    def vencContratos(self, nom): #Los vencimientos de los contratos en 6 meses
        equipo=self.buscarEquipo(nom) #Busca el nombre del equipo
        presente=date.today() #Toma el día de la fecha

        if equipo == False:
            print("Error con el equipo ingresado, intente de nuevo.")
        else:
            print("{} - {}" .format(equipo.getNombre(), equipo.getCiudad()))
            for i in range(len(equipo.getContrato())):
                fincont=equipo.getContrato()[i].getFechaFin() #Toma el valor de la fecha de finalización del contrato
                restames=fincont.month - presente.month #Restamos los meses
                animun=presente.year+1 #Sumamos uno al año actual
                if presente.year == fincont.year and restames <= 6:
                    print(equipo.getContrato()[i].getJugador())
                    print("-------------------------------------------------------")
                elif presente.year == animun and restames >= 6:
                    print(equipo.getContrato()[i].getJugador())
                    print("-------------------------------------------------------")
            

    def cargarContratoaEquipo(self, contrr, team): #Para cargar el contrato a un equipo
        team.agregaContrato(contrr)





    def manejadorArchivo(self):
        archivo=open("Equipos.csv")
        reader= csv.reader(archivo, delimiter=";")
        next(reader)
        for i in reader:
            team= Equipo(str(i[0]), str(i[1]))
            self.agregadorEquipo(team)
        archivo.close()
