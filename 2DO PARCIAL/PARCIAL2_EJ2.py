from TDA_ArbolBinario import Arbol
from TDA_Cola import Cola
from TDA_GRAFO import Grafo
from TDA_HEAPMIN import HeapMin
from TDA_Lista import Lista
from TDA_PILA import Pila 

#Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
#necesarios para resolver las tareas, listadas a continuación:
#1). cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook,
#servidor, router, switch, impresora;
#2). realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
#Hat, Debian, Arch;
#3). encontrar el camino más corto para enviar a imprimir un documento desde la pc:
#Debian y Red Hat, hasta el servidor “MongoDB”;
#4). encontrar el árbol de expansión mínima;
#5). la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
#realice un barrido en profundidad para corroborar que efectivamente fue borrada;
#6). debe utilizar un grafo no dirigido.

G=Grafo

insertar_vertice(g, 'Ubuntu', 'PC')
insertar_vertice(g, 'Debian', 'Notebook')
insertar_vertice(g, 'Switch 1', 'Switch')
insertar_vertice(g, 'Impresora', 'Impresora')
insertar_vertice(g, 'Mint', 'PC')
insertar_vertice(g, 'Router 1', 'Router')
insertar_vertice(g, 'Router 2', 'Router')
insertar_vertice(g, 'Router 3', 'Router')
insertar_vertice(g, 'Red Hat', 'Notebook')
insertar_vertice(g, 'Guarani', 'Servidor')
insertar_vertice(g, 'Switch 2', 'Switch')
insertar_vertice(g, 'Manjaro', 'PC')
insertar_vertice(g, 'Parrot', 'PC')
insertar_vertice(g, 'Fedora', 'PC')
insertar_vertice(g, 'Arch', 'Notebook')
insertar_vertice(g, 'MongoDB', 'Servidor')
