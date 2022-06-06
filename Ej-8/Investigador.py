from Personal import Personal
class Investigador(Personal):
    __areaInvestigacion= ""
    __tipoInvestigacion= ""

    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, areainv="", tipoinv="", carrera="", cargo="", catedra=""):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad, areainv, tipoinv, carrera, cargo, catedra)
        self.__areaInvestigacion= areainv
        self.__tipoInvestigacion= tipoinv
    def getArea(self):
        return self.__areaInvestigacion
    def getTipo(self):
        return self.__tipoInvestigacion
    def __str__(self):
        return f"INVESTIGADOR: Apellido: {super().getApellido()} Nombre: {super().getNombre()}"

    def porcentaje(self):
        percent=super().getAntiguedad()
        return percent

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldoB=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                areainv=self.__areaInvestigacion,
                tipoinv=self.__tipoInvestigacion,
                carrera="",
                cargo="",
                catedra=""
            )
        )
        return d
