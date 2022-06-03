from Aparato import Aparato
class Televisor(Aparato):
    __pantalla="" #Tipo de pantalla
    __pulgadas=0
    __definicion=""
    __internet=None

    def __init__(self, marca, modelo, color, pfab, preciob, pantalla, pulgadas, definicion, internet):
        super().__init__(marca, modelo, color, pfab, preciob)
        self.__pantalla=pantalla
        self.__pulgadas=pulgadas
        self.__definicion=definicion
        self.__internet=internet


    def __str__(self):
        s="Televisor: MARCA: {} - PAIS:{} - PRECIO: ${}" .format(super().getMarca(), super().getPais(), super().importeVenta())
        return s
    def getInternet(self):
        return self.__internet

    def porcentaje(self):
        percent=0.0
        if self.__definicion.lower() == "sd":
            percent=1.01
        elif self.__definicion.lower()== "hd":
            percent=1.02
        elif self.__definicion.lower()== "fullhd":
            percent=1.03
        if self.__internet:
            percent+=0.10
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
                pantalla=self.__pantalla,
                pulgadas=self.__pulgadas,
                definicion=self.__definicion,
                internet=self.__internet
            )
        )
        return d
