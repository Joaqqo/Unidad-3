from Flores import Flores

class Ramo:
    __tamanio=""
    __flores=[]

    def __init__(self, tam):
        self.__tamanio= tam
        self.__flores= []

    def __str__(self):
        s= f"--{self.__tamanio}-- \n"
        for flor in self.__flores:
            s+= f"{flor}\n"
        return s

    def agregaFlores(self, num, nom, col, desc):
        obj=Flores(num, nom, col, desc)
        self.__flores.append(obj)

    def getTamanio(self):
        return self.__tamanio
    def getFlores(self):
        return self.__flores
