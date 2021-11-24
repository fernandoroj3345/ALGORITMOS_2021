from TDA_arbol import Arbol
from TDA_ArbolBinario import Arbol
from TDACola import Cola
from TDAGrafo import Grafo
from TDA_HEAPMIN import HeapMin
from TDALista import Lista
from TDAPILA import Pila 
from random import choice

'''Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
necesarios para resolver las tareas, listadas a continuación:
1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
2. Realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
Hat, Debian, Arch;
3. Encontrar el camino más corto para enviar a imprimir un documento desde la pc:
Debian y Red Hat, hasta el servidor “MongoDB”;
4. Encontrar el árbol de expansión mínima;
5. La impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
realice un barrido en profundidad para corroborar que efectivamente fue borrada;
6. Debe utilizar un grafo no dirigido'''

Red=Grafo(dirigido=False)


