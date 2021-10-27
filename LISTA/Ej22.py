from TDA_LISTA import eliminar,insertar,barrido_lista,Lista,randint
'''
Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
nombre, valoración del público es un valor comprendido entre 0-10–, año de estreno y recaudación.
Desarrolle los algoritmos necesarios para realizar las siguientes tareas:

A. permitir filtrar las películas por año es decir mostrar todas las películas de un determinado año.
B. mostrar los datos de la película que más recaudo;
C. indicar las películas con mayor valoración del público, puede ser más de una;
D. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
lista auxiliar–:
I. por nombre.
II. por recaudación.
III. por año de estreno.
IV. por valoración del público.
'''
class Peliculas():
    def __init__(self, nombre, valoracion, año_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.año_estreno = año_estreno
        self.recaudacion = recaudacion

    def __str__(self):
        return self.nombre + '  |  ' + str(self.valoracion) + '  |  ' + str(self.año_estreno) + ' | ' + str(self.recaudacion)


def lista_peliculas():
    lista, lista_ranking = Lista(), Lista()
    datos = Peliculas('The Shining', randint(0, 10), 1980, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Alien 3', randint(0, 10), 1992, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('Prometheus', randint(0, 10), 2012, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('2001', randint(0, 10), 1968, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    datos = Peliculas('The Raven', randint(0, 10), 2012, randint(50000000, 500000000))
    insertar(lista, datos, 'nombre')
    print('   NOMBRE   |  VALORACION(0-10) |  AÑO DE ESTRENO | RECAUDACION(USD)')
    barrido_lista(lista)
    print()

    # A)  permitir filtrar las películas por año es decir mostrar todas las películas de 
    # un determinado año.
    aux = lista.inicio
    buscado = int(input('Ingrese un año de estreno: '))
    while aux is not None:
        if buscado == aux.info.año_estreno:
            print(aux.info.nombre, 'se estreno en el año', buscado)
        aux = aux.sig
    print()

    # B mostrar los datos de la película que más recaudo
    mas_recuadacion = 0
    mayor_peli = ''
    aux = lista.inicio
    while aux is not None:
        if aux.info.recaudacion > mas_recuadacion:
            mayor_peli = aux.info
        aux = aux.sig
    print('Pelicula que mas recaudo y sus datos')
    print(' NOMBRE  | VALORACION(0-10)| AÑO DE ESTRENO | RECAUDACION(USD)')
    print(mayor_peli)
    print()

    # c indicar las películas con mayor valoración del público, puede ser más de una
    aux = lista.inicio
    mas_valor = 0
    while aux is not None:
        if aux.info.valoracion > mas_valor:
            mas_valor = aux.info.valoracion
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if aux.info.valoracion == mas_valor:
            print(aux.info.nombre, 'tiene la valoracion mas alta,', mas_valor, 'puntos')
        aux = aux.sig
    print()

    # d  mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
#lista auxiliar–:
#I. por nombre,
#II. por recaudación,
#III. por año de estreno,
#IV. por valoración del público.
    print('Ingrese criterio de orden: ')
    print('* nombre')
    print('* valoracion')
    print('* año_estreno')
    print('* recaudacion')
    criterio = input()
    aux = lista.inicio
    while aux is not None:
        insertar(lista_ranking, aux.info, criterio)
        aux = aux.sig
    print()
    if criterio == 'nombre':
        print('Lista ordenada por nombre:')
        barrido_lista(lista_ranking)
    elif criterio == 'valoracion':
        print('Lista ordenada por valoracion:')
        barrido_lista(lista_ranking)
    elif criterio == 'año_estreno':
        print('Lista ordenada por año de estreno:')
        barrido_lista(lista_ranking)
    elif criterio == 'recaudacion':
        print('Lista ordenada por recaudacion:')
        barrido_lista(lista_ranking)

lista_peliculas()
