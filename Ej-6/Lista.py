from Nodo import Nodo
from Televisor import Televisor
from Heladera import Heladera
from Lavarropa import Lavarropa
from IElemento import IAparato
from zope.interface import implementer

@implementer(IAparato)
class Lista:
    __comienzo=None
    __actual=None #Elemento actual
    __indice=0 #Lleva la cuenta de los pasos de iteracion
    __tope=0 #Total de elementos de la lista

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def cargaAparato(self): #Carga aparato a mano
        aparato=None
        valor=None
        cic=None
        marca=input("Ingrese la marca del aparato:  ")
        modelo=input("Ingrese el modelo del aparato: ")
        color=input("Ingrese el color del aparato:  ")
        pais=input("Ingrese el país de fabricación del aparato:  ")
        precio=float(input("Ingrese el precio base del aparato:  "))
        tipo=input("Ingrese si el aparato es Televisor, Heladera o Lavarropa:  ")
        if tipo.lower() == "televisor":
            pantalla=input("Ingrese el tipo de pantalla:  ")
            pulgada=int(input("Ingrese las pulgadas del televisor:  "))
            defnicion=input("Ingrese tipo de definición (SD,HD, FULLHD):  ")
            internet=input("¿Tiene internet? (si/no): ")
            if internet.lower() == "si":
                valor=True
            elif internet.lower() == "no":
                valor=False
            aparato= Televisor(marca,modelo,color,pais,precio,pantalla,pulgada,defnicion,valor)

        elif tipo.lower() == "heladera":
            capacidad=int(input("Ingrese la capacidad de la heladera en litros:  "))
            freezer=input("¿Tiene freezer? (si/no): ")
            if freezer.lower() == "si":
                valor=True
            elif freezer.lower() == "no":
                valor=False
            ciclica=input("¿Es cíclica? (si/no): ")
            if ciclica.lower() == "si":
                cic=True
            elif ciclica.lower() == "no":
                cic=False
            aparato=Heladera(marca,modelo,color,pais,precio,capacidad,valor,cic)

        elif tipo.lower() == "lavarropa":
            capacidad=int(input("Ingrese la capacidad en del lavarropa KG:  "))
            velcentri=int(input("Ingrese la velocidad de centrifugado:  "))
            programas=int(input("Ingrese la cantidad de programas del lavarropa:  "))
            tipocarga=input("Ingrese el tipo de carga del lavarropa (Frontal/Superior):  ")
            aparato=Lavarropa(marca,modelo,color,pais,precio,capacidad,velcentri,programas,tipocarga)

        else:
            print("¡Error! \n")
        return aparato

    def insertarAparato(self, aparat, posicion): #Para insertar en una posición determinada (Inciso 1)
        anterior=None
        if posicion == 0:
            self.agregarAparato(aparat)
            print("El aparato se insertó correctamente. ")
        else:
            nuevoap=Nodo(aparat)
            aux=self.__comienzo
            i=0
            while aux is not None and i < posicion:
                anterior= aux
                aux=aux.getSiguiente()
                i+=1
            if aux is None:
                print("Número de posición incorrecto.")
            else:
                nuevoap.setSiguiente(aux)
                anterior.setSiguiente(nuevoap)
                self.__tope+=1
                print("El aparato se insertó correctamente. ")

    def agregarAparato(self, aparato): #Para insertarlo en la lista (Inciso 2)
        nodo=Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def mostrarAparato(self, posicion): #Muestra que tipo de aparato está en la posición ingresada (Inciso 3)
        tipo= None
        if posicion >=0 and posicion < self.__tope:
            i= 0
            aux= self.__comienzo
            while i <= posicion:
                tipo= type(aux.getDato())
                aux= aux.getSiguiente()
                i+=1
            if tipo == Televisor:
                print("En la posición {} ingresada hay un objeto tipo 'Televisor'.".format(posicion+1))
            elif tipo == Lavarropa:
                print("En la posición {} ingresada hay un objeto tipo 'Lavarropa'.".format(posicion+1))
            elif tipo == Heladera:
                print("En la posición {} ingresada hay un objeto tipo 'Heladera'.".format(posicion+1))
            else:
                print("En la posicón ingresada no hay un objeto de tipo 'Heladera', 'Lavarropa' o 'Televisor'.")
        else:
            print("La posición ingresada es incorrecta. ")


    def marcaPhilips(self): #Cuenta la cantidad de aparatos de marca Philips (Inciso 4)
        acum=0
        for i in self:
            if i.getMarca().lower() == "philips":
                acum+=1
        print("La cantidad de aparatos de marca Philips es: {}" .format(acum))

    def lavarropaSuperior(self): #Muestra la marca de los lavarropas con tipo de carga "Superior" (Inciso 5)
        for i in self:
            if type(i) == Lavarropa:
                if i.getTipoCarga().lower() == "superior":
                    print(i.getMarca())

    def mostrarPrecios(self): #Muestra los datos con los importes de venta (Inciso 6)
        for i in self:
            print(i)

    def toJSON(self):
        lista= []
        for v in self:
            lista.append(v.toJSON())
        d= dict(__class__=self.__class__.__name__, datos=lista)
        return d

    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
