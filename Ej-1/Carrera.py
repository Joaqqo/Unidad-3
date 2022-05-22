class Carrera:
    __codC=0
    __nomC="" #nomC el nombre de la carrera
    __nomF="" #nomF sería el nombre del profesional
    __duracion=""
    __titulo=""


    def __init__(self, cod, nom, nomf, dur, tit):
        self.__codC= cod
        self.__nomC= nom
        self.__nomF= nomf
        self.__duracion= dur
        self.__titulo= tit



    def getNombre(self):
        return self.__nomC
    def getNombrePro(self):
        return self.__nomF
    def getDuracion(self):
        return self.__duracion
