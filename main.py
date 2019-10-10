''''........................................................
    Titulo: Implementacion de la Clase Nodo (Arbol Binario)
    Autor:  Eddy flores c.
    Fecha:  Abril del 2019
.........................................................'''
from src.ArbolBinario import *

A = ArbolBinarioDeBusqueda()


print ('insertar 30')
A.insertar(30)
print (A.preOrden())

print ('insertar 20')
A.insertar(20)
print (A.preOrden())

print ('insertar 20')
A.insertar(20)
print (A.preOrden())


print ('insertar 10')
A.insertar(10)
print (A.preOrden())


print ('eliminar 25')
A.eliminar(25)
print (A.preOrden())

print ('insertar 80')
A.insertar(80)
print (A.preOrden())

print ('eliminar 10')
A.eliminar(10)
print (A.preOrden())






