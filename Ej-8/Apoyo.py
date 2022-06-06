from Personal import Personal
class Apoyo(Personal):
    __categoria = 0

    def __init__(self, cuil, apellido, nombre, sueldoB, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad)
        self.__categoria = categoria

    def __str__(self):
        return f"APOYO: Apellido: {super().getApellido()} Nombre: {super().getNombre()}"

    def porcentaje(self):
        percent=super().getAntiguedad()
        if self.__categoria >= 1 and self.__categoria <= 10:
            percent+=10
        elif self.__categoria >= 11 and self.__categoria <= 20:
            percent+=20
        elif self.__categoria >= 21 and self.__categoria <= 22:
            percent+=30
        return percent

    def changeCategoria(self, nuevaCategoria):
        self.__categoria= nuevaCategoria
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
                categoria=self.__categoria
            )
        )
        return d
