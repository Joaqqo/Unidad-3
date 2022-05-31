from zope.interface import Interface



class IpruebaInterfaz(Interface):
    def insertarElemento(elemento, posicion): #Elemento a insertar y posición
        pass

    def agregarElemento(elemento): #Elemento a agregar
        pass

    def mostrarElemento(posicion): #Posición
        pass
