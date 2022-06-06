from Nodo import Nodo
#from Personal import Personal
from Docente import Docente
from Apoyo import Apoyo
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from IElemento import IPersonal
from ITesorero import ITesorero
from IDirector import IDirector
from zope.interface import implementer


@implementer(IPersonal)
@implementer(IDirector)
@implementer(ITesorero)
class Lista:
    __comienzo=None
    __actual=None #Elemento actual
    __indice=0 #Lleva la cuenta de los pasos de iteracion
    __tope=0 #Total de elementos de la lista

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def agregarPersonal(self, personal): #Para insertarlo en la lista (Inciso 2)
        nodo=Nodo(personal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def insertarPersonal(self, personal, posicion): #Para insertar en una posición determinada (Inciso 1)
        anterior=None
        if posicion == 0:
            self.agregarPersonal(personal)
            print("El aparato se insertó correctamente. ")
        else:
            nuevoap=Nodo(personal)
            aux=self.__comienzo
            i=0
            while aux is not None and i < posicion:
                anterior= aux
                aux=aux.getSiguiente()
                i+=1
            if aux is None:
                print("Número de posición incorrecto. ")
            else:
                nuevoap.setSiguiente(aux)
                anterior.setSiguiente(nuevoap)
                self.__tope+=1
                print("El aparato se insertó correctamente. ")

    def mostrarPersonal(self, posicion): #Muestra que tipo de aparato está en la posición ingresada (Inciso 3)
        tipo= None
        if posicion >=0 and posicion < self.__tope:
            i= 0
            aux= self.__comienzo
            while i <= posicion:
                tipo= type(aux.getDato())
                aux= aux.getSiguiente()
                i+=1
            if tipo == Docente:
                print("En la posición {} ingresada hay un objeto tipo 'Docente'.".format(posicion+1))
            elif tipo == Apoyo:
                print("En la posición {} ingresada hay un objeto tipo 'Apoyo'.".format(posicion+1))
            elif tipo == Investigador:
                print("En la posición {} ingresada hay un objeto tipo 'Investigador'.".format(posicion+1))
            elif tipo == DocenteInvestigador:
                print("En la posición {} ingresada hay un objeto tipo 'Docente Investigador'.".format(posicion+1))
            else:
                print("En la posicón ingresada no hay un objeto de tipo 'Heladera', 'Lavarropa' o 'Televisor'.")
        else:
            print("La posición ingresada es incorrecta. ")



    def mostrarCarrera(self, carrera): #Inciso 4
        nombres=[]
        for i in self:
            if type(i) == DocenteInvestigador:
                if i.getCarrera().lower() == carrera.lower():
                    nomb=i.getNombre()
                    nombres.append(nomb)
        nombres.sort()
        print(nombres)

    def contadorAreas(self, area):
        contDI=0
        contI=0
        for i in self:
            if type(i) == DocenteInvestigador:
                if i.getArea().lower() == area.lower():
                    contDI+=1
            elif type(i) == Investigador:
                if i.getArea().lower() == area.lower():
                    contI+=1
        print("La cantidad de Docentes Investigadores para el área ingresada es: {}" .format(contDI))
        print("La cantidad de Investigadores para el área ingresada es: {}" .format(contI))
        print("Entonces el total sería de: {}" .format(contDI+contI))

    def muestraAlfabeticamente(self, lista, long): #Ordena alfabeticamente y muestra los datos del Personal. Inciso 6
        j = 0
        aux = self.__comienzo
        while aux is not None:
            personal = aux.getDato()
            compara = personal.getApellido()
            if compara == lista[j]:
                j += 1
                print("NOMBRE: {} - APELLIDO: {} - CUIL: {} - SUELDO: ${} - ANTIGÜEDAD: {} - TIPO: {}".format(personal.getNombre().center(10), personal.getApellido().center(10), personal.getCuil(),personal.getSueldo(), personal.getAntiguedad(), type(personal)))
                if j != long:
                    aux = aux.getSiguiente()
                    if aux is None:
                        aux = self.__comienzo
                else:
                    aux = None
            else:
                aux = aux.getSiguiente()
                if aux is None:
                    aux = self.__comienzo

    def listadoApellidos(self): #Listado de apellidos. Inciso 6
        apellidos=[]
        for i in self:
            apellido=i.getApellido()
            apellidos.append(apellido)
        apellidos.sort()
        self.muestraAlfabeticamente(apellidos,len(apellidos))

    def muestraCategoria(self, categoria):
        acum=0
        for i in self:
            if type(i) == DocenteInvestigador:
                if i.getCategoriaInvestigacion() == categoria:
                    print("APELLIDO: {} - NOMBRE: {} - EXTRA: {}".format(i.getApellido().center(10), i.getNombre().center(20), i.getImporteExtra()))
                    acum+=i.getImporteExtra()
        if acum == 0:
            print("No existen Docentes investigadores con la categoría ingresada.")
        else:
            print("La Secretaría de Investigación, debe solicitar al Ministerio un total de ${} de importe extra".format(acum))

    def toJSON(self):
        lista= []
        for v in self:
            lista.append(v.toJSON())
        d= dict(__class__=self.__class__.__name__, datos=lista)
        return d


    def cargaPersonal(self):
        personal=None
        print("--Información básica del personal--")
        apellido=input("Apellido:  ")
        nombre=input("Nombre:  ")
        cuil=int(input("Cuil:  "))
        sueldo=float(input("Sueldo básico:  "))
        antig=int(input("Ingrese la antigüedad en años:  "))

        print("--Elija el tipo de personal--")
        print("1-Docente")
        print("2-Investigador")
        print("3-Apoyo")
        print("4-Docente Investigador")
        opcion=int(input("Ingrese la opción:  "))
        if opcion == 1:
            print("--Datos del Docente--")
            carrera=input("Carrera:  ")
            cargo=input("Cargo:  ")
            catedra=input("Catedra:  ")
            personal=Docente(cuil,apellido,nombre,sueldo,antig,carrera,cargo,catedra)
        elif opcion == 2:
            print("--Datos del Investigador--")
            area=input("Area de investigación:  ")
            tipo=input("Tipo de investigación:  ")
            personal=Investigador(cuil,apellido,nombre,sueldo,antig,area,tipo)
        elif opcion == 3:
            print("Datos del Personal de Apoyo--")
            categoria=int(input("Categoría:  "))
            personal=Apoyo(cuil,apellido,nombre,sueldo,antig,categoria)
        elif opcion == 4:
            print("--Datos del Docente Investigdor--")
            print("Datos de Docente--")
            carrera=input("Carrera:  ")
            cargo=input("Cargo:  ")
            catedra=input("Catedra:  ")
            print("Datos de Investigador--")
            area=input("Area de investigación:  ")
            tipo=input("Tipo de investigación:  ")
            categ=int(input("Categoría:  "))
            extra=float(input("Importe extra:  "))
            personal=DocenteInvestigador(cuil,apellido,nombre,sueldo,antig,carrera,cargo,catedra,area,tipo,categ,extra)
        return personal
    #--------------------------------Ejercicio 8-----------------------------------------------------------

    def buscarPersonal(self, cuil): #Para buscar un personal, devuelve None si no lo encontró
        aux=self.__comienzo
        while aux.getDato().getCuil() != cuil and aux.getSiguiente() != None:
            aux=aux.getSiguiente()
        if aux.getDato().getCuil() != cuil:
            personal=None
        else:
            personal=aux.getDato()
        return personal



    def gastosSueldoPorEmpleado(self, cuil): #Para el tesorero
        personal=self.buscarPersonal(cuil)
        if personal == None:
            print("Error con el CUIL ingresado, intente de nuevo.")
        else:
            print("El personal tiene unos gastos de: ${}" .format(personal.getSueldo()))

    def modificarBasico(self, cuil, nuevoBasico): #Para director
        personal=self.buscarPersonal(cuil)
        if personal == None:
            print("Error con el CUIL ingresado, intente de nuevo.")
        else:
            personal.changeSueldoB(nuevoBasico)

    def modificarCargo(self, cuil, nuevoCargo): #Para director
        personal= self.buscarPersonal(cuil)
        if personal == None:
            print("Error con el CUIL ingresado, intente de nuevo.")
        else:
            if type(personal) == Docente:
                personal.changeCargo(nuevoCargo)
            else:
                print("El personal con el CUIL ingresado, no es Docente.")

    def modificarCategoria(self, cuil, nuevaCategoria): #Para director
        personal= self.buscarPersonal(cuil)
        if personal == None:
            print("Error con el CUIL ingresado, intente de nuevo.")
        else:
            if type(personal) == Apoyo:
                personal.changeCategoria(nuevaCategoria)
            else:
                print("El personal con el CUIL ingresado, no es personal de Apoyo.")

    def modificarImporteExtra(self, cuil, nuevoImporteExtra): #Para director
        personal=self.buscarPersonal(cuil)
        if personal == None:
            print("Error con el CUIL ingresado, intente de nuevo.")
        else:
            if type(personal) == DocenteInvestigador:
                personal.changeExtra(nuevoImporteExtra)
            else:
                print("El personal con el CUIL ingresado, no es Docente Investigador.")

    def Login(self):
        print("POR FAVOR INGRESE SUS DATOS")
        log=[]
        usuario=input("USUARIO:  ")
        log.append(usuario)
        contra=input("CONTRASEÑA:  ")
        log.append(contra)
        return log







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
