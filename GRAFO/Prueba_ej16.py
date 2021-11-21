from tda_grafo import Grafo
'''Implementar un grafo no dirigido para almacenar puntos turísticos de interés de un determinado
país teniendo en cuenta los siguientes requerimientos:
A. Debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;
B. Cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: Atenas
(Partenón), Zeus (Olimpia), Hera (Olimpia), Apolo (Delfos),Poseidón (Sunión), Artemisa
(Éfeso) y Teatro de Dionisio (Acrópolis)
C. Hallar el árbol de expansión mínimo (Recubridor Minimo) partiendo de cualquiera de estos lugares;
D. Hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta
el templo de Apolo, en Delfos.'''

templos = Grafo(dirigido=False)

datos_templos = [{'nombre': 'Atenas (Partenon)', 'coordenadas' : {'latitud': '37°58′17″N', 'longitud': '23°43′36″E'}},
                 {'nombre': 'Zeus (Olimpia)', 'coordenadas' : {'latitud': '37°38′16″N', 'longitud': '21°37′48″E'}},
                 {'nombre': 'Hera (Olimpia)', 'coordenadas' : {'latitud': '37°38′20″N', 'longitud': '21°37′47″E'}},
                 {'nombre': 'Apollo (Delfos)', 'coordenadas' : {'latitud': '38°28′56″N', 'longitud': '22°30′05″E'}},
                 {'nombre': 'Poseidón (Sunión)', 'coordenadas' : {'latitud': '37°39′01″N', 'longitud': '24°01′28″E'}},
                 {'nombre': 'Artemisa (Éfeso)', 'coordenadas' : {'latitud': '37°56′59″N', 'longitud': '27°21′50″E'}},
                 {'nombre': 'Dionisio (Acrópolis)', 'coordenadas' : {'latitud': '37°58′13″N', 'longitud': '23°43′40″E'}},
]

#Carga de datos (Nodos)
for templo in datos_templos:
    templos.insertar_vertice(templo['nombre'], data = templo['coordenadas'])

def cargar_aristas ():#Conexiones entre los nodos
    templos.insertar_arista(127, 'Atenea (Partenon)', 'Zeus (Olimpia)')
    templos.insertar_arista(987, 'Atenea (Partenon)', 'Hera (Olimpia)')
    templos.insertar_arista(820, 'Atenea (Partenon)', 'Apollo (Delfos)')
    templos.insertar_arista(712, 'Atenea (Partenon)', 'Poseidón (Sunión)')
    templos.insertar_arista(632, 'Atenea (Partenon)', 'Artemisa (Éfeso)')
    templos.insertar_arista(101, 'Atenea (Partenon)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(422, 'Zeus (Olimpia)', 'Hera (Olimpia)')
    templos.insertar_arista(242, 'Zeus (Olimpia)', 'Apollo (Delfos)')
    templos.insertar_arista(355, 'Zeus (Olimpia)', 'Poseidón (Sunión)')
    templos.insertar_arista(769, 'Zeus (Olimpia)', 'Artemisa (Éfeso)')
    templos.insertar_arista(12, 'Zeus (Olimpia)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(47, 'Hera (Olimpia)', 'Apollo (Delfos)')
    templos.insertar_arista(69, 'Hera (Olimpia)', 'Poseidón (Sunión)')
    templos.insertar_arista(10, 'Hera (Olimpia)', 'Artemisa (Éfeso)')
    templos.insertar_arista(314, 'Hera (Olimpia)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(636, 'Apollo (Delfos)', 'Poseidón (Sunión)')
    templos.insertar_arista(896, 'Apollo (Delfos)', 'Artemisa (Éfeso)')
    templos.insertar_arista(111, 'Apollo (Delfos)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(111, 'Poseidón (Sunión)', 'Artemisa (Éfeso)')
    templos.insertar_arista(333, 'Poseidón (Sunión)', 'Dionisio (Acrópolis)')
    templos.insertar_arista(444, 'Artemisa (Éfeso)', 'Dionisio (Acrópolis)')

cargar_aristas()

print('Ejercicio 16')
print()

#C)
#Hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;
#Expancion minima implica crear un bosque.
bosque = templos.prim()
peso = 0
print('Arbol de expansion minimo:')
for elemento in bosque:
    print(' ', elemento[1][0], '-', elemento[1][1])
    peso += elemento[0] #Cuenta y acumula el peso
print('El costo total es', peso, 'km.')
print()

#D)
#Hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta
#el templo de Apollo, en Delfos.

nodo1 = 'Atenea (Partenon)'
nodo2 = 'Apollo (Delfos)'
ver_origen = templos.buscar_vertice(nodo1)
ver_destino = templos.buscar_vertice(nodo2)

pila_camino = templos.dijkstra(ver_origen, ver_destino)

destino = nodo2
distancia = None

print ('El camino mas corto es:')
while(not pila_camino.pila_vacia()):
    dato = pila_camino.desapilar()
    if(dato[1][0] == destino):
        if(distancia is None):
            distancia = dato[0]
        print(' - ', dato[1][0])#muestro el recorrido.
        destino = dato[1][1]

print('La distancia total del camino es de', distancia, 'km.')