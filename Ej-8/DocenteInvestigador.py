from Docente import Docente
from Investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoriaInvestigacion= 0
    __importeExtra= 0

    def __init__(self, cuil=0, nombre="", apellido="", sueldoB=0.0, antiguedad=0, carrera="", cargo="", catedra="", areainv="", tipoinv="", categoria=0, importeextra=0):
        super().__init__(cuil, nombre, apellido, sueldoB, antiguedad, areainv, tipoinv, carrera, cargo, catedra)
        self.__categoriaInvestigacion= categoria
        self.__importeExtra= importeextra

    def __str__(self):
        return f"DOCENTE-INVESTIGADOR: Apellido: {super().getApellido()} Nombre: {super().getNombre()}"

    def getCategoriaInvestigacion(self):
        return self.__categoriaInvestigacion
    def getImporteExtra(self):
        return self.__importeExtra

    def changeExtra(self, nuevo):
        self.__importeExtra= nuevo
        print("El importe extra se cambió exitosamente. ")

    def porcentaje(self):
        percent=Docente.porcentaje(self)
        percentdos= (self.__importeExtra * 100) / Docente.getSueldoBasico(self)
        return percent + percentdos

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=super().getCuil(),
                apellido=super().getApellido(),
                nombre=super().getNombre(),
                sueldoB=super().getSueldoBasico(),
                antiguedad=super().getAntiguedad(),
                carrera=super().getCarrera(),
                cargo=super().getCargo(),
                catedra=super().getCatedra(),
                areainv = super().getArea(),
                tipoinv = super().getTipo(),
                categoria=self.__categoriaInvestigacion,
                importeextra=self.__importeExtra
            )
        )
        return d
