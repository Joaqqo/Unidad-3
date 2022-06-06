import abc

class Personal:
    __cuil= 0
    __apellido= ""
    __nombre= ""
    __sueldoB= 0
    __antiguedad= 0


    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, areinv="", tipoinv="", carrera="", cargo="", catedra=""):
        self.__cuil= cuil
        self.__apellido= apellido
        self.__nombre= nombre
        self.__sueldoB= sueldoB
        self.__antiguedad= antiguedad

    @abc.abstractmethod
    def porcentaje(self):
        pass
    def getSueldo(self):
        return self.__sueldoB + (self.porcentaje()*self.__sueldoB) / 100

    def getCuil(self):
        return self.__cuil
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getSueldoBasico(self):
        return self.__sueldoB
    def getAntiguedad(self):
        return self.__antiguedad

    def changeSueldoB(self, nuevo):
        self.__sueldoB= nuevo
        print("El sueldo básico se cambió exitosamente. ")


