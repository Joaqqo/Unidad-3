class Flores:
    __numero=0
    __nombre=""
    __color=""
    __descripcion=""

    def __init__(self, num, nom, col, des):
        self.__numero= num
        self.__nombre= nom
        self.__color= col
        self.__descripcion= des

    def __str__(self):
        return f"NUM: {self.__numero} - NOMBRE: {self.__nombre} - COLOR: {self.__color} - DESC: {self.__descripcion}"

    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getColor(self):
        return self.__color
    def getDescripcion(self):
        return self.__descripcion
