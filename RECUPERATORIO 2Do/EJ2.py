from TDA_Grafo import Grafo


'''Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
necesarios para resolver las tareas, listadas a continuación:

1) Cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
2) Realizar un barrido en profundidad y amplitud partiendo desde las tres notebook: 
Red Hat, Debian, Arch;
3) Encontrar el camino más corto para enviar a imprimir un documento desde la pc:
Debian y Red Hat, hasta el servidor “MongoDB”;
4) Encontrar el árbol de expansión mínima;
5) La impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
realice un barrido en profundidad para corroborar que efectivamente fue borrada;
6) Debe utilizar un grafo no dirigido'''

#Debemos indicar mediante la variable booleana dirigido, si el grafo 
#es dirigido tendrá valor verdadero y si es no dirigido falso
network=Grafo(dirigido=False)

#1)Cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
network.insertar_vertice('Manjaro', data = {'PC'})
network.insertar_vertice('Parrot', data = {'PC'})
network.insertar_vertice('Fedora', data = {'PC'})
network.insertar_vertice('Mint', data = {'PC'})
network.insertar_vertice('Ubuntu', data = {'PC'})
network.insertar_vertice('Arch', data = {'Notebook'})
network.insertar_vertice('Debian', data = {'Notebook'})
network.insertar_vertice('Red Hat', data = {'Notebook'})
network.insertar_vertice('Router 1', data = {'Router'})
network.insertar_vertice('Router 2', data = {'Router'})
network.insertar_vertice('Router 3', data = {'Router'})
network.insertar_vertice('Guarani', data = {'Servidor'})
network.insertar_vertice('MongoDB', data = {'Servidor'})
network.insertar_vertice('Switch 1', data = {'Switch'})
network.insertar_vertice('Switch 2', data = {'Switch'})   
network.insertar_vertice('Impresora', data = {'impresora'})

network.insertar_arista(40, 'Manjaro', 'Switch 2')
network.insertar_arista(12, 'Parrot',   'Switch 2')
network.insertar_arista(5,  'MongoDB',  'Switch 2')
network.insertar_arista(56, 'Arch',     'Switch 2')
network.insertar_arista(40, 'Manjaro',  'Switch 2')
network.insertar_arista(61, 'Router 3', 'Switch 2')
network.insertar_arista(43, 'Router 1', 'Router 3')
network.insertar_arista(50, 'Router 2', 'Router 3')
network.insertar_arista(37, 'Router 2', 'Router 1')
network.insertar_arista(9,  'Router 2', 'Guarani')
network.insertar_arista(25, 'Router 2', 'network Hat')
network.insertar_arista(29, 'Router 1', 'Switch 1')
network.insertar_arista(17, 'Switch 1', 'Debian')
network.insertar_arista(18, 'Switch 1', 'Ubuntu')
network.insertar_arista(22, 'Switch 1', 'Impresora')
network.insertar_arista(80, 'Switch 1', 'Mint')

#2)Realizar un barrido en profundidad y amplitud partiendo desde las tres notebook:
# Red Hat, Debian, Arch;
print ('BARRIDO EN AMPLITUD:')
pos = network.buscar_vertice('Red Hat') 
print('Barrido en profundidad de Red Hat Es:')
network.barrido_profundidad(pos)
network.marcar_no_visitado()
print('')
print('Barrido en Amplitud de Red Hat:')
network.barrido_amplitud(pos)
network.marcar_no_visitado()
print('')

pos = network.buscar_vertice('Debian') 
print('El Barrido En Profundidad De Debian Es:')
network.barrido_profundidad(pos)
network.marcar_no_visitado()
print('')
print('El Barrido En Amplitud De Debian Es:')
network.barrido_amplitud(pos)
network.marcar_no_visitado()
print('')

pos = network.buscar_vertice('Arch')
print('El Barrido En Profundidad De Es Arch:')
network.barrido_profundidad(pos)
network.marcar_no_visitado()
print('')
print('El Barrido En Amplitud De Arch Es:')
network.barrido_amplitud(pos)
network.marcar_no_visitado()
print('')

########################################################################################

#3) Encontrar el camino más corto para enviar a imprimir un documento desde la pc:
#Debian y Red Hat, hasta el servidor “MongoDB”;
print('PUNTO Nº3')
def camino_mas_corto(uno,dos):
    ver_origen = network.buscar_vertice(uno)
    ver_destino = network.buscar_vertice(dos)
    pila_camino = network.dijkstra(ver_origen, ver_destino)
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

print('El camino más corto de Debian a MongoDB Es:')
camino_mas_corto('Debian', 'MongoDB')
print('')
print('El camino más corto de Red Hat a MongoDB Es :')
camino_mas_corto('Red Hat', 'MongoDB')
print('')

'''
#4) Encontrar el árbol de expansión mínima;

exp_mini = network.prim()#Arbol de expansión minimo.
peso = 0
print('Árbol De Expansión Mínima Es:')
for elemento in exp_mini:
    print(elemento[1])
    peso += elemento[0]
print('El Costo Total Es', peso, 'km.')
print('')



#5) La impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
#realice un barrido en profundidad para corroborar que efectivamente fue borrada;

network.eliminar_vertice('Impresora')
print('Barrido en profundidad para corroborar que se elimino Impresora')
network.barrido_profundidad(0)

'''