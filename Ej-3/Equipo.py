
class Equipo:
    __nombre=""
    __ciudad=""
    __contrato=[]

    def __init__(self, nom, ciu):
        self.__nombre= nom
        self.__ciudad= ciu
        self.__contrato=[]



    def __str__(self):
        s= f"--{self.__nombre}--\n"
        for contrato in self.__contrato:
            s+= f"{contrato}\n"
        return s

    def agregaContrato(self, contrato):
        self.__contrato.append(contrato)

    def getNombre(self):
        return self.__nombre
    def getCiudad(self):
        return self.__ciudad
    def getContrato(self):
        return self.__contrato
