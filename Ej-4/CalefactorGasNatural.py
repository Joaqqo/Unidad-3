from Calefactor import Calefactor
class CalefactorGasNatural(Calefactor):
    __matricula=""
    __calorias=0
    estimacion=0

    def __init__(self, mar, mod, mat, cal):
        super().__init__(mar,mod)
        self.__matricula= mat
        self.__calorias= cal

    def __str__(self):
        return f"{super().getMarca()} - {super().getModelo()} "


    @classmethod
    def getEstimacion(cls):
        return cls.estimacion
    def getCalorias(self):
        return self.__calorias
    def getMatricula(self):
        return self.__matricula
