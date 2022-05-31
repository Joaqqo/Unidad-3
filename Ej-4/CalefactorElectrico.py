from Calefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __maxPotencia=0
    __kilowattxhora=0.0
    estimacion=0


    def __init__(self, mar, mod, max, kxh):
        super().__init__(mar,mod)
        self.__maxPotencia= max
        self.__kilowattxhora=kxh

    def __str__(self):
        return f"{super().getMarca()} - {super().getModelo()}"


    @classmethod
    def getEstimacion(cls):
        return cls.estimacion
    def getKWattH(self):
        return self.__kilowattxhora
    def getWattH(self):
        watt= self.__kilowattxhora*1000
        return watt




