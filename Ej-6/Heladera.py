from Aparato import Aparato

class Heladera(Aparato):
    __capacidad=0
    __freezer=None
    __ciclica=None

    def __init__(self, marca, modelo, color, pfab, preciob, capacidad, freezer, ciclica):
        super().__init__(marca, modelo, color, pfab, preciob)
        self.__capacidad=capacidad
        self.__freezer=freezer
        self.__ciclica=ciclica

    def __str__(self):
        s="Heladera: MARCA: {} - PAIS:{} - PRECIO: ${}" .format(super().getMarca(), super().getPais(), super().importeVenta())
        return s

    def porcentaje(self):
        percent=0.0
        if not self.__freezer and not self.__ciclica:
            percent=1.01
        elif self.__freezer and not self.__ciclica:
            percent=1.05
        elif self.__ciclica and self.__freezer or not self.__freezer:
            percent=1.10
        return percent

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=super().getMarca(),
                modelo=super().getModelo(),
                color=super().getColor(),
                pfab=super().getPais(),
                preciob=super().getPrecioB(),
                capacidad=self.__capacidad,
                freezer=self.__freezer,
                ciclica=self.__ciclica
            )
        )
        return d
