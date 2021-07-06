#1
#Dado un vector con personaje de las películas de la saga de Star Wars resolver las siguientes actividades:
#A
#Realizar un barrido recursivo del vector.
#B
#Realizar una función recursiva que permita determinar si ‘Yoda’ está en el vector y en que posición.

#Punto A
from TDA_COLA import *
from TDA_PILA import *

#A
def barrido_personajes(personajes):
    if(len(personajes)>0):
        print(personajes[0])
        barrido_personajes(personajes[1:])
#B
def buscar_yoda(vec, izq, der, x):
    if der < izq:
        return -1
    if vec[izq] == x:
        return izq
    if vec[der] == x:
        return der
    return buscar_yoda(vec, izq+1, der-1, x)
 

personajes = ['han solo','yoda','c3po','darth vader','chewbacca']
barrido_personajes(personajes)
n = len(personajes)
x = 'yoda'
pos = buscar_yoda(personajes, 0, n-1, x)
if pos != -1:
    print (x,'esta prensente en el indice ',pos)
else:
    print (x,'no esta presente')

###############################################################################################################

#2.
#Dada una cola con las notificaciones de las aplicaciones de red social de un Smartphone,de las cual se cuenta
# con la hora de la notificación, la aplicación que la emitió y el mensaje, resolver las siguientes actividades:
#C
#Escribir una función que elimine de la cola todas las notificaciones de Facebook;
#D.
#Escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, 
#sin perder datos en la cola;
#E.
#Utilizar una pila para almacenar temporalmente las notificaciones de Instagram y mostrar el contenido de dicha
#pila.

class notificaciones (object):

    def __init__(self, hora, aplicacion_emisora, mensaje):
        self.hora = hora
        self.aplicacion = aplicacion
        self.mensaje = mensaje

    def __str__(self):
        return str(self.hora)[:2] + ':' + str(self.hora)[2:]+ ' - ' + self.aplicacion + ' - ' + self.mensaje

datos_app = [('14:45','Telegram','notificacion'),('1:15','Snapchat','notificacion Python'),('00:00','Instagram','notificacion'),
         ('Twitter','notificacion'), ('11:15','Instagram','notificacion'), ('16:20','Facebook','notificacion'),
         ('9:28','Twitter','Python notificacion'), ('19:12','Facebook','notificacion'), ('15:39','Instagram','notificacion')]

notificaciones = Cola()
cola_aux = Cola()
pila_instagram = Pila()


for (hora, aplicacion, mensaje) in datos_app:
    notificacion = notificaciones(hora, aplicacion, mensaje)
    notificaciones.encolar(notificacion)

print()
print('Lista de notificaciones:')
barrido_cola(notificaciones)
print()

def eliminar_notificacion (cola, aplicacion):
    """Elimino la totalidad de notificaciones de la aplicacion dada de la cola."""
    cola_aux = Cola()
    while not cola.cola_vacia():
        x = cola.desencolar()
        if x.aplicacion != aplicacion:
            cola_aux.encolar(x)
    while not cola_aux.cola_vacia():
        cola.encolar(cola_aux.desencolar())

def mostrar_notificacion (cola, aplicacion, palabra):
    """Muestra las notificaciones de la aplicacion dada que contengan 'palabra' en el mensaje."""
    cola_aux = Cola()
    while not cola.cola_vacia():
        x = cola.desencolar(x)
        cola_aux.encolar(x)
        if (x.aplicacion == aplicacion and palabra in x.mensaje):
            print(x)
    while not cola_aux.cola_vacia():
        cola.encolar(cola_aux.desencolar())

#C.
eliminar_notificacion(notificaciones, 'Facebook')
print('Lista de notificaciones luego de eliminar las de Facebook:')
barrido_cola(notificaciones)
print()

#D. 
print ("Notificaciones de Twitter que contienen la palabra 'Python'")
mostrar_notificacion(notificaciones, 'Twitter', 'Python')
print()

#E.
while not notificaciones.cola_vacia():
    x = notificaciones.desencolar()
    cola_aux.encolar(x)
    if (x.aplicacion == 'Instagram'):
        pila_instagram.apilar(x)

while not cola_aux.cola_vacia():
    notificaciones.encolar(cola_aux.desencolar())

print('Notificaciones de Instagram:')
barrido_pila(pila_instagram)
print()

#################################################################################################################

3.
#Dada una lista con nombres de personajes de la saga de Avengers, resolver las
#siguientes tareas:
#A.
#Determinar si ‘Thor’ está en la lista, de ser así indicar en qué posición de la misma;
#B.
#Modificar el nombre de ‘Scalet Witch’ a ‘Scarlet Witch’;
#C.
#Dada una lista auxiliar con los siguientes personajes (‘Black Widow’, ‘Hulk’,
#‘Rocket Racoonn’, ‘Loki’), agregarlos a la lista principal en el caso de no estar cargados.
#D.
#Realizar un barrido ascendente y descendente de la lista.
#E.
#Mostrar la información del personaje en la posición 7.
#F.
#Mostrar todos los personajes que comienzan con C o S.
#G.
#Ahora los datos cambiaron y debe incluir (año de aparición y un campo booleano que indica si es héroe True 
#villano False), luego realizar un barrido ordenado por nombre y otro por año de aparición.
#Deberá cargar toda la información de nuevo.

personajes1 = [
    {'nombre':'Loki','año_aparicion': 2017, 'heroe' : False},
    {'nombre':'Black Widow','año_aparicion': 2021, 'heroe' : True},
    {'nombre':'Goku','año_aparicion': 1989, 'heroe' : True},
    {'nombre':' Black Panther','año_aparicion': 2010, 'heroe' : True},
    {'nombre':'Pepper Potts','año_aparicion': 2009, 'heroe' : False},
    {'nombre':'Scalet Witch','año_aparicion': 2014, 'heroe' : True}
]

personajes2 = [
    {'nombre':'Black Widow','año_aparicion': 2010, 'heroe' : True},
    {'nombre':'Hulk','año_aparicion': 2008, 'heroe' : True},
    {'nombre':'Rocket Raccoon','año_aparicion': 2014, 'heroe' : True},
    {'nombre':'Loki','año_aparicion': 2011, 'heroe' : False}

]

def mostrar_datos (lista, pos):
    print ('Nombre:', lista.obtener_elemento(pos)['nombre'], '| Año de aparición:', lista.obtener_elemento(pos)['año_aparicion'])
    if lista.obtener_elemento(pos)['heroe']:
        print ('Estado: Heroe')
    else:
        print ('Estado: Villano')

lista_personajes = personajes1()
lista_auxiliar = personajes2()

for personaje in personajes1:
    lista_personajes.insertar(personaje, 'nombre')

for personaje in personajes2:
    lista_auxiliar.insertar(personaje, 'nombre')

#A
pos = lista_personajes.busqueda('Thor', 'nombre')
if (pos != -1):
    print('Thor se encuentra en la lista en la posicion', pos)
else:
    print('Thor no se encuentra en la lista.')

print()

#B


#C
for i in range (lista_auxiliar.tamanio()):
    pos = lista_personajes.busqueda(lista_auxiliar.obtener_elemento(i)['nombre'], 'nombre')
    if pos == -1:
        lista_personajes.insertar(lista_auxiliar.obtener_elemento(i), 'nombre')
