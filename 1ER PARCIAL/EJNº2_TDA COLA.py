import random
import string


class Nodo_Cola():#Defino la clase
    '''Crea una variable nodo cola'''
    def __init__(self):
        self.info = None
        self.sig = None


class Cola():
    '''Crea una cola vacia'''
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def encolar(cola, dato):
    '''Inserta un elemento al final de la cola'''
    nodo = Nodo_Cola()
    nodo.info = dato
    if cola.final is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1


def desencolar(cola):
    '''Quita un elemento desde el frente de la cola'''
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = cola.frente
    cola.tamanio -= 1
    return dato


def cola_vacia(cola):
    '''Devuelve true si la cola esta vacia'''
    return cola.tamanio == 0


def tamanio_cola(cola):
    '''Tamanio de la cola'''
    return cola.tamanio


def colaint(cola, cant):
    '''Carga una cola con numeros enteros randomicos'''
    for i in range(0, cant):
        encolar(cola, random.randint(0, 10))

def colaintpn(cola, cant):#cargo numero enteros negativos y positivos desde -10 a 10
    '''Carga una cola con numeros enteros randomicos'''
    for i in range(0, cant):
        encolar(cola, random.randint(-10, 10))


def colacadenas(cola, cant):
    """carga una cola con digitos y caracteres randomicos """
    for i in range(0, cant):
        encolar(cola, random.choice(string.printable))


def colastring(cola, cant):
    '''Carga una cola con letras randomicas'''
    for i in range(0, cant):
        encolar(cola, random.choice(string.ascii_letters))


def barrido_cola(cola):
    '''Muestra los elementos de una cola'''
    if tamanio_cola(cola) > 0:
        nodo = cola.frente
        while nodo:
            print(nodo.info)
            nodo = nodo.sig


def en_frente(cola):
    '''Muestra el dato que esta al frente en la cola'''
    if tamanio_cola(cola) > 0:
        return cola.frente.info


def mover_final(cola):
    '''Quita el elemento del frente y lo mueve al final'''
    if cola.tamanio > 0:
        encolar(cola, desencolar(cola))