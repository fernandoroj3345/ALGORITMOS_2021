from TDA_LISTA import eliminar,insertar,barrido_lista,Lista
'''
Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:
a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic.
'''

def comics():
    '''LISTA DE LOS SUPERHEROES DE COMICS'''
    comic = Lista()#defino la lista comic
    nombre = ['Linterna Verde', 'Wolverine', 'Dr. Strange', 'Capitana Marvel',
              'Mujer Maravilla', 'Flash', 'Star-Lord', 'Joker']
    anio = [1940, 1974, 1963, 1968, 1941, 1940, 1976, 1940]
    casacomic = ['DC', 'Marvel', 'DC', 'Marvel', 'DC', 'DC', 'Marvel', 'DC']
    biografia = ['traje : color verde, arma : anillo de poder',
                 'poderosa capacidad de regeneracion, tres garras retractiles en cada mano',
                 'hechicero supremo', 'guerrera extraterrestre de la civilizacion Kree',
                 'princesa guerrera de las Amazonas',
                 'capacidad de correr, moverse y pensar extremadamente rapido',
                 'policia interplanetario', 'criminal mas notable de Gotham City']
    
    marvel, dc = 0, 0 # inicializo en cero las casas de los superheroes
    for i in range(len(nombre)):
        insertar(comic, [nombre[i], anio[i], casacomic[i], biografia[i]])
    barrido_lista(comic)#Esto es un array dentro de otro array#
    print()
    aux = comic.inicio
    while aux is not None:
        dato = aux.info# info son mis datos cargados
        #a. eliminar el nodo que contiene la información de Linterna Verde#
        if dato[0] == 'Linterna Verde':
            eliminar(comic, aux.info)
            print('Se elimino:', dato[0])
        #b. mostrar el año de aparición de Wolverine#
        if dato[0] == 'Wolverine':
            print(dato[0], ': aparecio en el anio', str(dato[1]))
        #c. cambiar la casa de Dr. Strange a Marvel#
        if dato[0] == 'Dr. Strange':
            dato[2] = 'Marvel'
            print(dato)
        #d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”#
        if dato[3].find('traje') >= 0 or dato[3].find('armadura') >= 0:
            print(dato[0], 'lleva la palabra armadura/traje en su bio')
        #e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparició sea anterior a 1963#
        if dato[1] < 1963:
            print('El personaje', dato[0], 'de la casa ',
                  dato[2], 'aparecio antes del anio 1963')
       # f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla#
        if dato[0] == 'Capitana Marvel' or dato[0] == 'Mujer Maravilla':
            print(dato[0], 'pertenece a la casa', dato[2])
        #g. mostrar toda la información de Flash y Star-Lord#
        if dato[0] == 'Flash' or dato[0] == 'Star-Lord':
            print('Info de', dato[0], ':', dato[3])
        #h. listar los superhéroes que comienzan con la letra B, M y S# con cad asigno la 1er letra del nombre
        cad = dato[0]# dato[0] esto es el nombre      
        if cad[0] == 'B' or cad[0] == 'M' or cad[0] == 'S':
            print(dato[0], 'comienza con la letra B, M o S')
        #i. determinar cuántos superhéroes hay de cada casa de comic.#
        if dato[2] == 'Marvel':
            marvel += 1
        if dato[2] == 'DC':
            dc += 1
        aux = aux.sig # aux.sig pasa al siguiente nodo
    print('En la casa DC hay', dc, 'personajes')
    print('En la casa Marvel hay', marvel, 'personajes')

comics()