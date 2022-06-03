from zope.interface import Interface


class IPersonal(Interface):
    def insertarPersonal(elementoAinsertar, posicion):  #Elemento a insertar y posición
        pass

    def agregarPersonal(elementoAagregar): #Elemento a agregar
        pass

    def mostrarPersonal(posicion): #Posición
        pass
