import csv
from Facultad import Facultad

class ManejadorFacultad:
    __listaFacultad=[]

    def __init__(self):
        self.__listaFacultad=[]

    def agregadorLista(self, facu):
        self.__listaFacultad.append(facu)



    def mostrarcode(self, code):
        bandera=True
        if code > len(self.__listaFacultad) or code == 0:
            bandera=False
        else:
            print("\n --- {} --- \n".format(self.__listaFacultad[code-1].getNombreFacu()))
            for i in range(len(self.__listaFacultad[code-1].getCarrera())):
                print("Nombre: {}".format(self.__listaFacultad[code-1].getCarrera()[i].getNombre()))
                print("Duración: {}" .format(self.__listaFacultad[code-1].getCarrera()[i].getDuracion()))
                print("---------------------------------")
        return bandera

    def buscar(self,nom):
        i, j= 0, 0
        bandera=True
        while i < len(self.__listaFacultad) and bandera:
            j=0
            while j < len(self.__listaFacultad[i].getCarrera()) and bandera:
                if self.__listaFacultad[i].getCarrera()[j].getNombre().lower() == nom.lower():
                    bandera = False
                    print("Código: {}{} - Nombre de Facultad: {} - Localidad: {}" .format(i+1, j+1, self.__listaFacultad[i].getNombreFacu(), self.__listaFacultad[i].getLocalidad()))
                j+=1
            i+=1
        return bandera

 #Manejador Archivo de otra forma
    def manejadorArchivoDOS(self):
        archivo=open("Facultades.csv")
        reader=csv.reader(archivo, delimiter=";")
        anterior=-1
        aux=0
        for i in reader:
            aux=int(i[0])
            if aux !=anterior:
                facc=Facultad(int(i[0]),str(i[1]), str(i[2]), str(i[3]), str(i[4]))
                self.agregadorLista(facc)
                anterior=aux
            else:
                if aux==anterior:
                    self.__listaFacultad[aux-1].agregarCarrera(i)
                    anterior=aux


    def manejadorArchivo(self):
        with open("Facultades.csv") as archivo:
            reader=csv.reader(archivo, delimiter=";")
            filaFacu=next(reader)
            bandera= True
            while bandera:
                cod=int(filaFacu[0])
                nom=str(filaFacu[1])
                dir=str(filaFacu[2])
                loc=str(filaFacu[3])
                tel=str(filaFacu[4])
                facc=Facultad(cod,nom,dir,loc,tel)
                self.agregadorLista(facc)
                filaCarrera=next(reader)
                while bandera and filaFacu[0] == filaCarrera[0]:
                    try:
                        self.__listaFacultad[int(filaFacu[0])-1].agregarCarrera(filaCarrera)
                        filaCarrera=next(reader)
                    except StopIteration:
                        bandera= False
                filaFacu=filaCarrera









