from Jugador import Jugador

class ManejadorJugadores:
    __listaJugadores=[]

    def __init__(self):
        self.__listaJugadores=[]

    def buscaJugador(self, dni): #Busca jugador
        i=0
        bandera=False
        jug=None
        while i < len(self.__listaJugadores) and not bandera:
            if self.__listaJugadores[i].getDNI() == dni:
                jug= self.__listaJugadores[i]
                bandera=True
            i+=1
        return jug

    def cargaJugador(self): #Para cargar el jugador a mano
        nom=input("Ingrese nombre del jugador:  ")
        dni=input("Ingrese DNI del jugador:  ")
        nat=input("Ingrese ciudad natal del jugador:  ")
        org=input("Ingrese país de origen del jugador:  ")
        nac=input("Ingrese fecha de nacimiento del jugador(AA-MM-DD):  ")
        jug=Jugador(nom,dni,nat,org,nac)
        self.__listaJugadores.append(jug)
        print("¡Jugador inscripto!")




