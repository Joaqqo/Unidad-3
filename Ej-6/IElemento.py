from zope.interface import Interface

class IAparato(Interface):
    def insertarAparato(elementoAinsertar, posicion):
        pass
    def agregarAparato(elementoAagregar):
        pass
    def mostrarAparato(posicion):
        pass
