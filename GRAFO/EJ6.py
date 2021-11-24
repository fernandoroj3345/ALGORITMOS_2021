from tda_grafo import Grafo #grafo dirigido
'''Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen del ejercicio
20 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver las siguientes actividades:
A. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que
representa, no más de 20 palabras;
B. Deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano,
pareja, la etiquetas de dichas aristas son estos nombre de relación.
C. Dado el nombre de un dios mostrar los hijos de este;
D. Dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
E. Determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación
    entre ambos;
F. Dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como
    camino más corto el que tenga menor número de aristas;
F. Realizar un barrido en profundidad y amplitud de dicho grafo;
H. Realizar un barrido mostrando el nombre de cada dios y el de su madre;
I. Mostrar todos los ancestros de un determinado dios;
J. Mostrar todos los nietos de Cronos;
K. Mostrar todos los hijos de Tea;
L. Persista los datos del grafo en archivos, uno para los vértices y otro para las aristas.'''

DiosesGriegos= Grafo()
#abro el archivo de texto y  los datos del archivo y cargo los datos.
file = open('Dioses.txt', encoding="utf8")#UTF significa “ Formato de transformación Unicode ” y el '8' significa que se utilizan valores de 8 bits en la codificación
lineas = file.readlines()#readlines Devuelve una lista con todas las líneas del archivo.
lineas.pop(0)#borrar la primera linea de mi archivo dioses.txt que lo unico que tiene (esa linea) es que es cada campo.
#creamos los nodos del grafo
for linea in lineas:
    dios = linea.split(';')#con split voy cortando los textos que que esten separados con ";" y los asocio a
                                                                    #los datos que agrego al dicccionario. 
    dios_data = {}#diccionario vacio.
    nombre = dios[0]
    dios_data['descripcion'] = dios[5]#accedo a la columna 5
    dios_data['genero'] = dios[6]# "" "" "" "" "" "" "" "" "" "" ""
    DiosesGriegos.insertar_vertice(nombre, data = dios_data)

#cargo las lineas y genero las relaciones entre nodos
for linea in lineas:
    dios = linea.split(';')
    nombre = dios[0]
    padre = dios[1]
    madre = dios[2]
    hermanos = dios[3].split('/')#Devuelve solo un array en lugar de una linea de texto.(valor de ASCII 10, definido como nueva línea)
    hijos = dios[4].split('/')
    genero = dios[6]
    pareja = dios[7].split('\n')[0]
    if (madre != '-'):
        DiosesGriegos.insertar_arista(1, nombre, madre, data = 'hijo/a')#1 peso de todas las aristas.
    if (padre != '-'):
        DiosesGriegos.insertar_arista(1, nombre, padre, data = 'hijo/a')
    if (hijos[0] != '-'): # porque se creo una lista con un unico elemento que es '-' si no tiene hijos
        for hijo in hijos:#hijo es una sublista
            if (genero == 'F'):
                DiosesGriegos.insertar_arista(1, nombre, hijo,  data = 'madre')
            else:
                DiosesGriegos.insertar_arista(1, nombre, hijo,  data = 'padre')
    #Hermanos es una sublista
    if (hermanos[0] != '-'): # porque se creo una lista con un unico elemento que es '-' si no tiene hermanos
        for hermano in hermanos: 
            DiosesGriegos.insertar_arista(1, nombre, hermano, data = 'hermano/a')
    
    if (pareja != '-'):
        DiosesGriegos.insertar_arista(1, nombre, pareja, data = 'pareja')

print()

#C)
#Dado el nombre de un dios mostrar los hijos de este;

nombre_dios = input('Ingrese el nombre de un dios para ver a sus hijos: ').capitalize()#formateamos el string
hijos = DiosesGriegos.hijos_dios(nombre_dios)
if (hijos == None):
    print ('El dios ingresado no se encuentra cargado.')
elif (not hijos == []):#comparamos para ver si una
    print ('Los hijos de', nombre_dios, 'son:')
    for hijo in hijos:
        print ('\n - ', hijo)
else:
    print ('No hay informacion sobre los hijos de', nombre_dios)
print()

#Dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
#D)
nombre_dios = input('Ingrese el nombre de un dios para ver a su familia: ').capitalize()
padres, hijos, hermanos = DiosesGriegos.familia_dios(nombre_dios)

if (padres == None):
    print ('El dios ingresado no se encuentra cargado.')
else:
    print ('Miembros de la familia de', nombre_dios, ':')    
    if (not padres == []):#not devuelve true si alguno de los operadores es False
        print ('Padres:')
        for padre in padres:
            print (' -', padre)
    if (not hermanos == []):            
        print ('Hermanos:')
        for hermano in hermanos:
            print (' -', hermano)
    if (not hijos == []):            
        print ('Hijos:')
        for hijo in hijos:
            print (' -', hijo)    
print()


#E)
#Determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la relación
#entre ambos;
print('A continuacion, ingrese los nombres de dos Dioses Griegos para determinar si tienen una relacion directa.')
vertice_origen = input('Ingrese el nombre del primer dios: ').capitalize()#convierte el primer caracter de la cadena en una mayuscula.
vertice_destino = input('Ingrese el nombre del segundo dios: ').capitalize()
relaciones = DiosesGriegos.relacion_dioses(vertice_origen, vertice_destino)
if (not relaciones == []):
    print ('Relacion(es) entre', vertice_origen, 'y', vertice_destino, ':')
    for relacion in relaciones:
        print(' - ', vertice_origen, 'es', relacion, 'de', vertice_destino)
else:
    print('No existe relacion directa entre', vertice_origen, 'y', vertice_destino)
print()

#F)
#Dados dos DiosesGriegos determinar el camino más corto entre estos y mostrarlo. Considere como
#camino más corto el que tenga menor número de aristas;

print('A continuacion, ingrese los nombres de dos Dioses Griegos para determinar el camino mas corto entre ambos.')
dios1 = input('Ingrese el nombre del primer dios: ').capitalize()
dios2 = input('Ingrese el nombre del segundo dios: ').capitalize()
print()
ver_origen = DiosesGriegos.buscar_vertice(dios1)
ver_destino = DiosesGriegos.buscar_vertice(dios2)

pila_camino = DiosesGriegos.dijkstra(ver_origen, ver_destino)

destino = dios1
costo = None

print ('El camino mas corto es:')
while(not pila_camino.pila_vacia()):
    dato = pila_camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(' - ', dato[1][0])#[1]nombre del Dios [0]es el coste computacional
        destino = dato[1][1]

print('El costo total del camino es', costo)
print()

#G)
#Realizar un barrido en profundidad y amplitud de dicho grafo;
a = input('Presione enter para ver el barrido en profundidad.')
DiosesGriegos.barrido_profundidad(0)
print()
DiosesGriegos.marcar_no_visitado()
a = input('Presione enter para ver el barrido en amplitud.')
DiosesGriegos.barrido_amplitud(0)
DiosesGriegos.marcar_no_visitado()
print()

#H)
#Realizar un barrido mostrando el nombre de cada dios y el de su madre;
a = input('Presione enter para ver el barrido de los DiosesGriegos y sus madres.')
DiosesGriegos.barrido_profundidad_dioses_madres(0)
DiosesGriegos.marcar_no_visitado()
print()

#I)
#Mostrar todos los ancestros de un determinado dios;
ancestros = []
nombre_dios = input('Ingrese el nombre de un dios para ver a sus ancestros: ').capitalize()
DiosesGriegos.ancestros_dios(nombre_dios, ancestros)
if (not ancestros == []):
    print('Ancestros de', nombre_dios)
    for ancestro in ancestros:
        print(' - ', ancestro)
else:
    print ('No hay informacion sobre los ancestros de', nombre_dios)
print()

#J)
#Mostrar todos los nietos de Cronos;
print ('Nietos de Cronos:')
nietos = DiosesGriegos.nietos_dios('Kronos')
for nieto in nietos:
    print (' - ', nieto)
print()

#K)
#Mostrar todos los hijos de Tea;
print ('Los hijos de Tea son:')
hijos = DiosesGriegos.hijos_dios('Theia')
for hijo in hijos:
    print (' - ', hijo)
print()





