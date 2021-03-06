from Lista import Lista
from Docente import Docente
from Apoyo import Apoyo
from Investigador import Investigador
from DocenteInvestigador import DocenteInvestigador
from Personal import Personal
from pathlib import Path
import json


class Decodificador:

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()


    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario


    def decodificarDiccionario(self, d):
        if "__class__" not in d:
            return d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "Lista":
                elementos = d["datos"]
                lista = class_()
                for i in range(len(elementos)):
                    dElemento = elementos[i]
                    class_name = dElemento.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dElemento["__atributos__"]
                    unPersonal = class_(**atributos)
                    lista.agregarPersonal(unPersonal)
                return lista