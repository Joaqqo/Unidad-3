from Aparato import Aparato
class Lavarropa(Aparato):
    __capacidad=0
    __velcentri=0 #Velocidad de centrifugado
    __cantpro=0 #Cantidad de programas
    __tipocarga=""

    def __init__(self, marca, modelo, color, pfab, preciob, capacidad, velcentri, cantpro, tipocarga):
        super().__init__(marca, modelo, color, pfab, preciob)
        self.__capacidad=capacidad
        self.__velcentri=velcentri
        self.__cantpro=cantpro
        self.__tipocarga=tipocarga

    def __str__(self):
        s="Lavarropa: MARCA: {} - PAIS:{} - PRECIO: ${}" .format(super().getMarca(), super().getPais(), super().importeVenta())
        return s

    def getTipoCarga(self):
        return self.__tipocarga

    def porcentaje(self):
        percent=0.0
        if self.__capacidad <= 5:
            percent=1.01
        elif self.__capacidad >5:
            percent=1.03
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
                velcentri=self.__velcentri,
                cantpro=self.__cantpro,
                tipocarga=self.__tipocarga
            )
        )
        return d
