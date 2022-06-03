import abc
#from abc import ABC

class Aparato:
    __marca=""
    __modelo=""
    __color=""
    __pfab="" #País de fabricación
    __preciob=0.0 #Precio base

    def __init__(self, mar, mod,col, pfa, prb):
        self.__marca=mar
        self.__modelo=mod
        self.__color=col
        self.__pfab=pfa
        self.__preciob=prb

    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getColor(self):
        return self.__color
    def getPais(self):
        return self.__pfab
    def getPrecioB(self):
        return self.__preciob


    @abc.abstractmethod
    def porcentaje(self):
        pass

    def importeVenta(self):
        return self.__preciob* self.porcentaje()





