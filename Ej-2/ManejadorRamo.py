from Ramo import Ramo

class ManejadorRamo:
    __listaRamo=[]

    def __init__(self):
        self.__listaRamo= []

    def verifTamanio(self):
        listtm=["Chico", "Mediano", "Grande"]
        print("1=CHICO - 2=MEDIANO - 3=GRANDE")
        tam=int(input("Ingrese el tamaño del ramo en número: "))
        while tam < 1 or tam > 3:
            print("Error en el tamaño, ingrese de nuevo")
            tam=int(input("Ingrese el tamaño del ramo en número: "))
        tam= listtm[tam-1]
        return tam

    def cantFloresenRamos(self, contadores): #Cuenta la cantidad de tipos flores que hay en cada ramo
        for ramo in self.__listaRamo:
            for flor in ramo.getFlores():
                contadores[flor.getNumero()-1]+=1
        return contadores

    def mostrarxramo(self, tama): #Para el inciso 3, mostrar solo los de tamaño ingresado
        for ramo in self.__listaRamo:
            if ramo.getTamanio().lower() == tama.lower():
                print(ramo)




    def agregaRamo(self, manF):
        tamanio=self.verifTamanio()
        ramo=Ramo(tamanio)
        cantf=int(input("Ingrese la cantidad de flores que va a tener su ramo:  "))
        i=0
        print("Número de las flores y su nombre:")
        manF.mostrar()
        while i<cantf:
            numf=int(input("Ingrese el número de la flor que desea agregar al ramo: "))
            flor= manF.getFlor(numf)
            ramo.agregaFlores(flor[0], flor[1], flor[2], flor[3])
            i+=1
        self.__listaRamo.append(ramo)

