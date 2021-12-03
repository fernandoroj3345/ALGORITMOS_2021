
from TDA_Grafo import Grafo
'''
Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:

A) Cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho, baño 1,
baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

B) Cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco,
el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;

C) Obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para
conectar todos los ambientes;

D) Determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv;

E) Determinar si hay conexión directa e indirecta, entre la habitación 2 y la terraza.

'''
#A cargo la lista que es dinamica para acceder a los datos.

#A) cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
ambiente = Grafo (dirigido=False)

ambiente.insertar_vertice('cocina', data = {'comedor'})
ambiente.insertar_vertice('comedor', data = {'baño 1'})
ambiente.insertar_vertice('cochera', data = {'comedor'})
ambiente.insertar_vertice('quincho', data = {'habitación 2'})
ambiente.insertar_vertice('baño 1', data = {'patio'})
ambiente.insertar_vertice('baño 2', data ={None} )
ambiente.insertar_vertice('habitacion 1', data ={None} )
ambiente.insertar_vertice('habitacion 2', data = {None})
ambiente.insertar_vertice('sala de estar', data ={None})
ambiente.insertar_vertice('terraza', data ={None})
ambiente.insertar_vertice('patio', data = {None})

#B)Cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco,
#el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;

ambiente.insertar_arista(40, 'cocina','comedor')
ambiente.insertar_arista(12, 'cochera','baño 1' )
ambiente.insertar_arista(23, 'baño 2','baño 1')
ambiente.insertar_arista(12, 'habitaciob 1','comedor')
ambiente.insertar_arista(75, 'sala de estar','patio')
ambiente.insertar_arista(78, 'terraza','baño 1')
ambiente.insertar_arista(63, 'comedor','cocina')
ambiente.insertar_arista(41, 'patio','terraza')
ambiente.insertar_arista(12, 'habitacion 2','baño 2')
ambiente.insertar_arista(32, 'quincho','cocina')
ambiente.insertar_arista(12, 'quincho','comedor')
ambiente.insertar_arista(11, 'comedor','terraza')
ambiente.insertar_arista(47, 'terraza','patio')
ambiente.insertar_arista(56, 'habitacion 1','terraza')
ambiente.insertar_arista(12, 'terraza', 'sala de estar')
ambiente.insertar_arista(78, 'sala de estar','patio')
ambiente.insertar_arista(98, 'patio','cochera')
ambiente.insertar_arista(701, 'cochera','terraza')


#C)Obtener el árbol de expansión mínima y determine cuantos metros de cables se 
# necesitan para conectar todos los ambientes;

print('PUNTO C')
exp_mini = ambiente.prim()#Arbol de expansión minimo.
peso = 0
print('Árbol De Expansión Mínima Es:')
for elemento in exp_mini:
    print(elemento[1])
    peso += elemento[0]
print('El Costo Total Es', peso, 'Mtrs.')
print('')

##############################################################################################################

#D)Determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv;

print('PUNTO D')
def camino_mas_corto(uno,dos):
    ver_origen = ambiente.buscar_vertice(uno)
    ver_destino = ambiente.buscar_vertice(dos)
    pila_camino = ambiente.dijkstra(ver_origen, ver_destino)
    costo = None
    destino = dos
    while(not pila_camino.pila_vacia()):
        dato = pila_camino.desapilar()
        if(dato[1][0] == destino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            destino = dato[1][1]
    print('El costo total del camino es', costo)

print('El camino más corto de habitacion 1 a Sala De Estar Es:')
camino_mas_corto('habitacion 1', 'sala de estar')
print('')

##############################################################################################################

#E) Determinar si hay conexión directa e indirecta, entre la habitación 2 y la terraza.
print('Ingrese los nombres de Las Habitaciones Para Determinar Si Tienen Relacion De Adayacencia Directa o Indirecta.')
vertice_origen = input('Ingrese el nombre de La Primer Habitacion: ').capitalize()#convierte el primer caracter de la cadena en una mayuscula.
vertice_destino = input('Ingrese el nombre De La Segunda Habitacion: ').capitalize()
relaciones = ambiente.relacion_habitaciones(vertice_origen, vertice_destino)
if (not relaciones == []):
    print ('Relacion(es) entre', vertice_origen, 'y', vertice_destino, ':')
    for relacion in relaciones:
        print(' - ', vertice_origen, 'es', relacion, 'de', vertice_destino)
else:
    print('No existe relacion directa entre', vertice_origen, 'y', vertice_destino)
print()