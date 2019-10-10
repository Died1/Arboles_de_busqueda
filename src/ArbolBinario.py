''''........................................................
    Titulo: Implementacion de la Clase Nodo (Arbol Binario)
    Autor:  Eddy flores c.
    Fecha:  Abril del 2019
.........................................................'''
from src.Nodo import Nodo
from collections import deque


class ArbolBinarioDeBusqueda:

    def __init__(self):
        self.raiz = None

    '''===============================================================
    METODO INSERTAR
    ==============================================================='''

    def insertar(self, dato):
        if self.esArbolVacio():
            self.raiz = Nodo(dato)
        nodoActual = self.raiz
        nodoAnterior = Nodo.nodoVacio()
        # buscar la posicion del nuevoNodo
        while not Nodo.esNodoVacio(nodoActual):
            if dato == nodoActual.getDato():
                return False
            nodoAnterior = nodoActual
            if dato < nodoActual.getDato():
                nodoActual = nodoActual.getHijoIzquierdo()
            else:
                nodoActual = nodoActual.getHijoDerecho()
            # fin del ciclo
        # se inserte el nuevoNodo en su posicion
        nuevoNodo = Nodo(dato)
        if dato < nodoAnterior.getDato():
            nodoAnterior.setHijoIzquierdo(nuevoNodo)
        else:
            nodoAnterior.setHijoDerecho(nuevoNodo)
        # ------------------------------------------
        return True

    '''===============================================================
    FIN DEL METODO INSERTAR
    ==============================================================='''
    # Eliminar Iterativo

    def eliminarIterativo(self, datoAEliminar):
        nodoActual = self.raiz
        if self.esArbolVacio():
            return False
        while not nodoActual.esNodoVacio and datoAEliminar != nodoActual.getDato():
            if datoAEliminar < nodoActual.getDato():
                nodoActual = nodoActual.getHijoIzquierdo()
            else:
                nodoActual = nodoActual.getHijoDerecho()
        if datoAEliminar == nodoActual.getDato():
            # caso1:
            if nodoActual.esHoja():
                nodoActual = Nodo.nodoVacio()
            # caso2.
            if not nodoActual.esVacioHijoIzquierdo() and nodoActual.esVacioHijoDerecho:
                nodoActual = nodoActual.getHijoIzquierdo()
            if not nodoActual.esVacioHijoDerecho() and nodoActual.esVacioHijoIzquierdo:
                nodoActual = nodoActual.getHijoDerecho()
            # caso 3

        else:
            return False
    '''===============================================================
    METODO ELIMINAR
    ==============================================================='''

    def eliminar(self, dato):
        try:
            self.raiz = self.__eliminar(self.raiz, dato)
            return True
        except:
            return False

    def __eliminar(self, nodoActual, dato):
        if nodoActual == None:  # arbol vacio
            raise ValueError

        datoDelNodoActual = nodoActual.getDato()

        if dato > datoDelNodoActual:
            hijoDerecho = self.__eliminar(nodoActual.getHijoDerecho(), dato)
            nodoActual.setHijoDerecho(hijoDerecho)
        if dato < datoDelNodoActual:
            hijoIzquierdo = self.__eliminar(nodoActual.getHijoIzquierdo(), dato)
            nodoActual.setHijoIzquierdo(hijoIzquierdo)
        
        if dato == datoDelNodoActual:
            # caso1: nodo a eliminar es hoja
            if nodoActual.esHoja():
                return None

            # caso2: tiene un solo hijo
            if nodoActual.esVacioHijoIzquierdo() and not nodoActual.esVacioHijoDerecho():
                nuevoNodoActual = nodoActual.getHijoDerecho()
                nodoActual.setHijoDerecho(Nodo.nodoVacio())
                return nuevoNodoActual
            if not nodoActual.esVacioHijoIzquierdo() and nodoActual.esVacioHijoDerecho():
                nuevoNodoActual = nodoActual.getHijoIzquierdo()
                nodoActual.setHijoIzquierdo(Nodo.nodoVacio())
                return nuevoNodoActual

            #caso3: tiene ambos hijos
            sucesor = self.buscarDatoSucesor(nodoActual.getHijoDerecho())
            nuevoHijoDerecho = self.__eliminar(nodoActual.getHijoDerecho(), sucesor)
            nodoActual.setHijoDerecho(nuevoHijoDerecho)
            nodoActual.setDato(sucesor)

        return nodoActual

    def buscarDatoSucesor(self, nodoActual):
        nodoAnterior = nodoActual
        while not Nodo.esNodoVacio(nodoActual):
            nodoAnterior = nodoActual
            nodoActual = nodoActual.getHijoIzquierdo()
        return nodoAnterior.getDato()

    '''======================================================================
    FUNCIONES DE RECORRIDO DEL ARBOL
    ======================================================================'''

    def preOrden(self):
        recorrido = list()
        self.preOrdenR(self.raiz, recorrido)
        return recorrido

    def preOrdenR(self, nodoActual, recorrido):
        if Nodo.esNodoVacio(nodoActual):
            return
        recorrido.append(nodoActual.getDato())
        nodoHijoPorIzquierda = nodoActual.getHijoIzquierdo()
        self.preOrdenR(nodoHijoPorIzquierda, recorrido)
        nodoHijoPorDeracha = nodoActual.getHijoDerecho()
        self.preOrdenR(nodoHijoPorDeracha, recorrido)

    def inOrden(self):
        recorrido = list()
        self.inOrdenR(self.raiz, recorrido)
        return recorrido

    def inOrdenR(self, nodoActual, recorrido):
        if Nodo.esNodoVacio(nodoActual):
            return
        nodoHijoPorIzquierda = nodoActual.getHijoIzquierdo()
        self.inOrdenR(nodoHijoPorIzquierda, recorrido)
        recorrido.append(nodoActual.getDato())
        nodoHijoPorDeracha = nodoActual.getHijoDerecho()
        self.inOrdenR(nodoHijoPorDeracha, recorrido)

    def postOrden(self):
        recorrido = list()
        self.postOrdenR(self.raiz, recorrido)
        return recorrido

    def postOrdenR(self, nodoActual, recorrido):
        if Nodo.esNodoVacio(nodoActual):
            return
        nodoHijoPorIzquierda = nodoActual.getHijoIzquierdo()
        self.postOrdenR(nodoHijoPorIzquierda, recorrido)
        nodoHijoPorDeracha = nodoActual.getHijoDerecho()
        self.postOrdenR(nodoHijoPorDeracha, recorrido)
        recorrido.append(nodoActual.getDato())

    def recorridoPorNiveles(self):
        recorrido = list()
        if self.esArbolVacio():
            return recorrido
        nodoActual = Nodo.nodoVacio()
        colaDeNodos = deque()
        colaDeNodos.append(self.raiz)

        while colaDeNodos:
            nodoActual = colaDeNodos.popleft()
            recorrido.append(nodoActual.getDato())
            if not nodoActual.esVacioHijoIzquierdo():
                colaDeNodos.append(nodoActual.getHijoIzquierdo())
            if not nodoActual.esVacioHijoDerecho():
                colaDeNodos.append(nodoActual.getHijoDerecho())
        return recorrido

    '''======================================================================
    TAMAÑO
    ======================================================================'''

    def sizeRec(self):
        return self.__sizeRec(self.raiz)

    def __sizeRec(self, nodoActual):
        if Nodo.esNodoVacio(nodoActual):
            return 0
        cantidadPorIzquierda = self.__sizeRec(nodoActual.getHijoIzquierdo())
        cantidadPorDerecha = self.__sizeRec(nodoActual.getHijoDerecho())
        return cantidadPorIzquierda + cantidadPorDerecha + 1
    '''=======================================================================
    ALTURA
    ======================================================================='''

    def alturaRec(self):
        return self.__alturaRec(self.raiz)

    def __alturaRec(self, nodoActual):
        if Nodo.esNodoVacio(nodoActual):
            return 0
        alturaPorIzquierda = self.__alturaRec(nodoActual.getHijoIzquierdo())
        alturaPorDerecha = self.__alturaRec(nodoActual.getHijoDerecho())
        if alturaPorDerecha > alturaPorIzquierda:
            return alturaPorDerecha + 1
        return alturaPorIzquierda + 1

    '''=======================================================================
    CANTIDAD DE NODO
    ======================================================================='''

    def cantidadDeNodo(self):
        return self.__cantidadDeNodo(self.raiz)

    def __cantidadDeNodo(self, nodoActual):
        if Nodo.esNodoVacio(nodoActual):
            return 0
        cantidadPorIzquierda = self.__cantidadDeNodo(
            nodoActual.getHijoIzquierdo())
        cantidadPorDerecha = self.__cantidadDeNodo(nodoActual.getHijoDerecho())
        return cantidadPorIzquierda + cantidadPorDerecha + 1

    '''=======================================================================
    NIVEL DE UN NODO
    ======================================================================='''
    def nivelDeUnNodo(self, dato):
        recorrido = list()
        if self.esArbolVacio():
            return recorrido
        nodoActual = Nodo.nodoVacio()
        colaDeNodos = deque()
        colaDeNodos.append(self.raiz)

        while colaDeNodos:
            nodoActual = colaDeNodos.popleft()
            recorrido.append(nodoActual.getDato())
            if not nodoActual.esVacioHijoIzquierdo():
                colaDeNodos.append(nodoActual.getHijoIzquierdo())
            if not nodoActual.esVacioHijoDerecho():
                colaDeNodos.append(nodoActual.getHijoDerecho())
        return recorrido


    '''=======================================================================
    NODOS HOJAS (recorriendo por niveles)
    ======================================================================='''

    def nodosHojas(self):
        recorrido = list()
        if self.esArbolVacio():
            return recorrido
        nodoActual = Nodo.nodoVacio()
        colaDeNodos = deque()
        colaDeNodos.append(self.raiz)

        while colaDeNodos:
            nodoActual = colaDeNodos.popleft()
            if nodoActual.esHoja():
                recorrido.append(nodoActual.getDato())
            if not nodoActual.esVacioHijoIzquierdo():
                colaDeNodos.append(nodoActual.getHijoIzquierdo())
            if not nodoActual.esVacioHijoDerecho():
                colaDeNodos.append(nodoActual.getHijoDerecho())
        return recorrido

    '''=======================================================================
    NODOS PADRES (recorriendo por niveles)
    ======================================================================='''

    def nodosPadres(self):
        recorrido = list()
        if self.esArbolVacio():
            return recorrido
        nodoActual = Nodo.nodoVacio()
        colaDeNodos = deque()
        colaDeNodos.append(self.raiz)

        while colaDeNodos:
            nodoActual = colaDeNodos.popleft()
            if not nodoActual.esHoja():
                recorrido.append(nodoActual.getDato())
            if not nodoActual.esVacioHijoIzquierdo():
                colaDeNodos.append(nodoActual.getHijoIzquierdo())
            if not nodoActual.esVacioHijoDerecho():
                colaDeNodos.append(nodoActual.getHijoDerecho())
        return recorrido

    '''=======================================================================
    CLONAR UN ARBOL
    ======================================================================='''

    def clonarUnArbol(self, arbolActual):
        return arbolActual

    '''=======================================================================
    HERMANO DE UN NODO
    ======================================================================='''

    def hermanoDeUnNodo(self, dato):
        if self.esArbolVacio() or self.cantidadDeNodo() == 1 or self.raiz.getDato() == dato:
            raise ValueError
        nodoActual = self.raiz
        nodoPadre = Nodo.nodoVacio()
        while dato != nodoActual.getDato() and not Nodo.esNodoVacio(nodoActual):
            nodoPadre = nodoActual
            if dato < nodoActual.getDato():
                nodoActual = nodoActual.getHijoIzquierdo()
            else:
                nodoActual = nodoActual.getHijoDerecho()
        if dato == nodoActual.getDato():
            if nodoPadre.getHijoIzquierdo().getDato() == dato:
                return nodoPadre.getHijoDerecho()
            else:
                return nodoPadre.getHijoIzquierdo()
        else:
            raise ValueError

    '''=======================================================================
    BUSQUEDA BINARIA
    ======================================================================='''

    def buscar(self, dato):
        nodoAuxiliar = self.raiz
        while not Nodo.esNodoVacio(nodoAuxiliar):
            if dato == nodoAuxiliar.getDato():
                return nodoAuxiliar.getDato()
            if dato < nodoAuxiliar.getDato():
                nodoAuxiliar = nodoAuxiliar.getHijoIzquierdo()
            else:
                nodoAuxiliar = nodoAuxiliar.getHijoDerecho()
        return None
    ''' 
    Ascendente de un Nodo
    Refexion o espejo
    pooq de un arbol
    '''

    def vaciar(self):
        self.raiz = Nodo.nodoVacio()

    def esHoja(self, nodoActual):
        if nodoActual.getHijoIzquierdo() == None and nodoActual.getHijoDerecho() == None:
            return True
        else:
            return False

    def esArbolVacio(self):
        return Nodo.esNodoVacio(self.raiz)
