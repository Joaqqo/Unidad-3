
class Jugador:
    __nombre=""
    __DNI=""
    __ciudadN="" #Ciudad natal
    __paisOrg="" #País de origen
    __nacimiento="" #Fecha de nacimiento


    def __init__(self, nom, dni, cin, pas,nac):
        self.__nombre= nom
        self.__DNI= dni
        self.__ciudadN= cin
        self.__paisOrg= pas
        self.__nacimiento= nac

    def __str__(self):
        return f"Nombre: {self.__nombre} - DNI: {self.__DNI} - Nacimiento: {self.__nacimiento} - {self.__ciudadN}, {self.__paisOrg}"

    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__DNI
    def getCiudad(self):
        return self.__ciudadN
    def getPais(self):
        return self.__paisOrg
    def getNacimiento(self):
        return self.__nacimiento


