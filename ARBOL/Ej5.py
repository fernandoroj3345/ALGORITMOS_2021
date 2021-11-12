from TDA_ArbolBinario import *
from TDA_Cola import *

'''Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
(MCU), desarrollar un algoritmo que contemple lo siguiente:
A. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
que indica si es un héroe o un villano, True y False respectivamente;
B. Listar los villanos ordenados alfabéticamente;
C. Mostrar todos los superhéroes que empiezan con C;
D. Determinar cuántos superhéroes hay el árbol;
E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
encontrarlo en el árbol y modificar su nombre;
F. Listar los superhéroes ordenados de manera descendente;
G. Generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
los villanos, luego resolver las siguiente tareas:

I. determinar cuántos nodos tiene cada árbol;
II. realizar un barrido ordenado alfabéticamente de cada árbol'''

datos = [
    {'nombre':'Iron Man', 'heroe': True},
    {'nombre':'Thanos', 'heroe': False},
    {'nombre':'Kang', 'heroe': False},
    {'nombre':'Captain Marvel', 'heroe': True},
    {'nombre':'Agatha Harkness', 'heroe': False},
    {'nombre':'Captain America', 'heroe': True},
    {'nombre':'Taneleer Tivan', 'heroe': False},
    {'nombre':'Black Widow', 'heroe': True},
    {'nombre':'Doctor Strnge', 'heroe': True},
    {'nombre':'Scarlet Witch', 'heroe': True},
    {'nombre':'Ravonna Renslayer', 'heroe': False},
]

arbol = Arbol()

for personaje in datos:
    arbol = arbol.insertar_nodo(personaje['nombre'], personaje) # por el arbol avl

# arbol.preorden()

#B)
print('Villanos ordenados alfabeticamente:')
arbol.inorden_villanos()
print()

#C)
print('Superheroes que empiezan con C')
arbol.inorden_heroes_LetraC()
print()

#D)
print('En el arbol hay', arbol.contar_nodos(True), 'heroes.')
print()

#E)
buscado = input('Comience a escribir el nombre del personaje que desea cambiar: ')
arbol.busqueda_proximidad(buscado)
buscado = input('Ingrese el nombre completo del personaje que desea cambiar de la lista anterior: ')
pos = arbol.busqueda(buscado)
if (pos):
    nuevo_nombre = input('Ingrese el nuevo nombre: ')
    nombre, superheroe = arbol.eliminar_nodo(buscado)
    superheroe['nombre'] = nuevo_nombre
    arbol = arbol.insertar_nodo(nuevo_nombre, superheroe)
print()
# arbol.inorden()

#F)
print('Superheroes ordenados de manera descendente:')
arbol.postorden_heroes()
print()

#G)

arbol_heroes = Arbol()
arbol_villanos = Arbol()

arbol_heroes = arbol.separar_arbol(arbol_heroes, True)
print('Arbol de superheroes:')
arbol_heroes.inorden()
print('El arbol de superheroes tiene', arbol_heroes.contar_nodos(True), 'nodos.')
print()

arbol_villanos = arbol.separar_arbol(arbol_villanos, False)
print('Arbol de villanos:')
arbol_villanos.inorden()
print('El arbol de villanos tiene', arbol_villanos.contar_nodos(False), 'nodos.')
print()


