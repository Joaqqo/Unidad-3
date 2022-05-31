class Calefactor:
    __marca=""
    __modelo=""

    def __init__(self, mar, mod):
        self.__marca= mar
        self.__modelo= mod

    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
