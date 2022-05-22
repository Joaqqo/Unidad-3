from Carrera import Carrera

class Facultad:
    __codF= 0
    __nomF= ""
    __direcF=""
    __localidad=""
    __telefono=""
    __carrera=[]

    def __init__(self, cod, nom, dir, loc, tel):
        self.__codF= cod
        self.__nomF= nom
        self.__direcF= dir
        self.__localidad= loc
        self.__telefono= tel
        self.__carrera= []

    def agregarCarrera(self, car):
        carrr=Carrera(car[1], car[2], car[3], car[4], car[5])
        self.__carrera.append(carrr)


    def getCarrera(self):
        return self.__carrera
    def getNombreFacu(self):
        return self.__nomF
    def getLocalidad(self):
        return self.__localidad
