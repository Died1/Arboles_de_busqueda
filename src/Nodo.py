''''........................................................
    Titulo: Implementacion de la Clase Nodo (Arbol Binario)
    Autor:  Eddy flores c.
    Fecha:  Abril del 2019
.........................................................'''
class Nodo:

    def __init__(self, dato):
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.dato = dato

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getHijoIzquierdo(self):
        return self.hijoIzquierdo

    def setHijoIzquierdo(self, hijoIzquierdo):
        self.hijoIzquierdo = hijoIzquierdo

    def getHijoDerecho(self):
        return self.hijoDerecho

    def setHijoDerecho(self, hijoDerecho):
        self.hijoDerecho = hijoDerecho

    def esVacioHijoIzquierdo(self):
        return self.hijoIzquierdo == None

    def esVacioHijoDerecho(self):
        return self.hijoDerecho == None

    def esHoja(self):
        return self.esVacioHijoIzquierdo() and self.esVacioHijoDerecho()

    @staticmethod
    def nodoVacio():
        return None

    @staticmethod
    def esNodoVacio(nodo):
        return nodo == None
