from Personal import Personal
class Docente(Personal):
    __carrera= ""
    __cargo= ""
    __catedra= ""

    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, areainv="", tipoinv="", carrera="", cargo="", catedra=""):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad, areainv, tipoinv, carrera, cargo, catedra)
        self.__carrera= carrera
        self.__cargo= cargo
        self.__catedra= catedra

    def __str__(self):
        return f"DOCENTE: Apellido: {super().getApellido()} Nombre: {super().getNombre()}"

    def getCarrera(self):
        return self.__carrera
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra

    def porcentaje(self):
        percent=super().getAntiguedad()
        if self.__cargo.lower() == "simple":
            percent+=10
        elif self.__cargo.lower() =="semiexclusivo":
            percent+=20
        elif self.__cargo.lower() == "exclusivo":
            percent+=50
        return percent

    def changeCargo(self, nuevoCargo):
        self.__cargo= nuevoCargo
        print("¡Hecho!")

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldoB=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                areainv="",
                tipoinv="",
                carrera=self.__carrera,
                cargo=self.__cargo,
                catedra=self.__catedra
            )
        )
        return d
