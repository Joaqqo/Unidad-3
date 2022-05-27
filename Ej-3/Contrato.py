from datetime import date

class Contrato:
    __fechainicio= date
    __fechafin= date
    __pagomensual=0.0
    __equipo=None
    __jugador=None

    def __init__(self, ini, fin, pag, equ, jug):
        self.__fechainicio= ini
        self.__fechafin= fin
        self.__pagomensual= pag
        self.__equipo= equ
        self.__jugador= jug

    def __str__(self):
        return f"Jugador: {self.__jugador} - De {self.__fechainicio} Hasta {self.__fechafin} con ${self.__pagomensual} mensuales"

    def getPagoMensual(self):
        return self.__pagomensual
    def getFechaInicio(self):
        return self.__fechainicio
    def getFechaFin(self):
        return self.__fechafin
    def getJugador(self):
        return self.__jugador

