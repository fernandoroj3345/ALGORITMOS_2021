from TDA_arbol import Arbol
from TDA_Cola import Cola
from TDA_GRAFO import Grafo
from TDA_HEAPMIN import HeapMin
from TDA_Lista import Lista
from TDA_PILA import Pila 
from random import choice
#El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
#resolver los siguientes requerimientos:

#1)Almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
#conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter por ejemplo 7A),
# existen varios dinosaurios con el mismo nombre pero sus códigos son
#distintos, los códigos no pueden ser repetidos (tenga cuidado);

#2)Se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
#código;

#3)Realizar un barrido en orden del árbol ordenado por nombre;

#4)Mostrar toda la información del dinosaurio 792;

#5)Mostrar toda la información de todos los T-Rex que hay en la isla;

#6)Modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
#cargado, su nombre correcto es Stygimoloch;

#7)Mostrar la ubicación de todos los Raptores que hay en la isla;

#8)Contar cuantos Diplodocus hay en el parque;

#9)Debe cargar al menos 15 elementos.

#creo un diccionario y cargo los Dinosaurios

#Nº1
Dinodatos=[{'nombre':'Parasaurolofus','codigo':'792','ubicacion':'7a'},
    {'nombre':'Saltasaurus','codigo':'78','ubicacion':'9i'},
    {'nombre':'Chirostenote','codigo':'67','ubicacion':'2s'},
    {'nombre':'Acronthosaurus','codigo':'89','ubicacion':'d3'},
    {'nombre':'Velociraptor','codigo':'10','ubicacion':'0a'},
    {'nombre':'Dilophosaurus','codigo':'67','ubicacion':'9t'},
    {'nombre':'Coelophysis','codigo':'01','ubicacion':'8g'},
    {'nombre':'Ceratosaurus','codigo':'02','ubicacion':'5g'},
    {'nombre':'Monolophosaurus','codigo':'11','ubicacion':'4g'},
    {'nombre':'Spinosaurus','codigo':'12','ubicacion':'3f'},
    {'nombre':'Astralopitecus','codigo':'13','ubicacion':'3g'},
    {'nombre':'Compsognathus','codigo':'15','ubicacion':'6i'},
    {'nombre':'Tyrannosaurus rex','codigo':'09','ubicacion':'2b'},
    {'nombre':'Braquiosaurio','codigo':'03','ubicacion':'3x'},
    {'nombre':'Protoceratops.','codigo':'00','ubicacion':'5h'},
    {'nombre':'Stygimoloch','codigo':'23','ubicacion':'7x'}
]

#2
ArbolNombresDinos = Arbol()
ArbolCodigosDino = Arbol()
for Dino in Dinodatos:ArbolCodigosDino:#Para cada Dinosaurio en el diccionario inserto los nodos. 
    Arbol = Arbol.insertar_nodo(ArbolNombresDinos['nombre'], ArbolNombresDinos) # por el arbol avl

    Arbol = Arbol.insertar_nodo(ArbolCodigosDino['nombre'], ArbolCodigosDino) # por el arbol avl

#3)Realizar un barrido en orden del árbol ordenado por nombre;
ArbolNombresDinos.inorden()

#4)Mostrar toda la información del dinosaurio 792;
buscado=ArbolCodigosDino.busqueda(792)
print(buscado['nombre'],buscado['ubicacion']),buscado['codigo']

#5)Mostrar toda la información de todos los T-Rex que hay en la isla;
ArbolNombresDinos.inorden_dinosaurios()

#6)Modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
#cargado, su nombre correcto es Stygimoloch;

#7)Mostrar la ubicación de todos los Raptores que hay en la isla;
ArbolNombresDinos.inorden_dinosaurios.()













 

