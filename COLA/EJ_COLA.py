from TDA_COLA import Cola,encolar,desencolar,cola_vacia,tamanio_cola,colaint,colaintpn,colacadenas,colastring,barrido_cola,en_frente,mover_final

'''
#EJ Nº11
Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
A. mostrar los personajes del planeta Alderaan, Endor y Tatooine
B. indicar el plantea natal de Luke Skywalker y Han Solo
C. insertar un nuevo personaje antes del maestro Yoda
D. eliminar el personaje ubicado después de Jar Jar Binks'''
'''

def starwarsplanet(): 
    starwars = Cola()
    tatooine = Cola()
    endor = Cola()
    alderaan = Cola()
    luke_han = Cola()
    aux = Cola()


    character = ['Luke Skywalker','Han Solo','Yoda','Jar Jar Binks','Nippet','Leila Organa','Chewbacca']
    planet =    ['Tatooine', 'Corellia', 'Dagobah', 'Naboo', 'Endor', 'Alderaan', 'Kashyyyk']



    for elemento in range(0,7):
        personaje, planeta = character[elemento], planet[elemento]
        encolar(starwars, [personaje, planeta])#Personaje es posicion 0 y planeta posicion 1
    print('Cola de personajes con su planeta origen:')
    barrido_cola(starwars)

    while not cola_vacia(starwars):
        charac = desencolar(starwars)#Desencolo un personaje de la cola starwars.
        encolar(aux, charac)
        if charac[0] == 'Luke Skywalker' or charac[0] == 'Han Solo':
            encolar(luke_han, charac)
        if charac[1] == 'Tatooine':
            print('')
#Punto A        
            encolar(tatooine, charac[0])
            print('personajes del planeta Tatooine')
            barrido_cola(tatooine)
        if charac[1] == 'Endor':
            print('')
            encolar(endor, charac[0])
            print('personajes del planeta Endor')
            barrido_cola(endor)
        if charac[1] == 'Alderaan':
            encolar(alderaan, charac[0])
            print('')
            print('personajes del planeta Alderaan')
            barrido_cola(alderaan)
        
#Punto B    
    while not cola_vacia(luke_han):
        charac = desencolar(luke_han)
        if charac[0] == 'Luke Skywalker':
            print('')
            print('el planete de origen de',charac[0],'es',charac[1])
        if charac[0] == 'Han Solo':
            print('el planete de origen de',charac[0],'es',charac[1])


#PUNTO C



#PUNTO D
'''
'''

############################################################################################################
#EJ Nº12

Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
ni métodos de ordenamiento.
'''
def ordenados():
    cola1 = Cola()
    cola2 = Cola()

    while tamanio_cola(cola1)<5:
        dato = int(input('ingrese un numero '))
        encolar(cola1, dato)
    print('cola 1')
    barrido_cola(cola1)
    while tamanio_cola(cola2)<7:
        dato = int(input('ingrese un numero '))
        encolar(cola2, dato)
    print('cola 2')
    barrido_cola(cola2)
    cant = tamanio_cola(cola1)
    for i in range(0, tamanio_cola(cola1)):
        if en_frente(cola1) < en_frente(cola2):
            mover_final(cola1)
        else:
            while en_frente(cola1)>en_frente(cola2):
                dato = desencolar(cola2)
                encolar(cola1,dato)
            mover_final(cola1)
    while not cola_vacia(cola2):
        dato = desencolar(cola2)
        encolar(cola1, dato)
    print('colas ordenadas')
    barrido_cola(cola1)

############################################################################################################
#EJ Nº16
'''
Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. 
imprima todos los documentos de la cola de impresión.
'''

#############################################################################################################
#EJ Nº22
'''
Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
–por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
A. determinar el nombre del personaje de la superhéroe Capitana Marvel;
B. mostrar los nombre de los superhéroes femeninos;
C. mostrar los nombres de los personajes masculinos;
D. determinar el nombre del superhéroe del personaje Scott Lang;
E. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
con la letra S;
F. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
de superhéroes.
'''

def MarvelUniverse():   
    personajes = Cola()
    femenino = Cola()
    masculino = Cola()
    aux = Cola()
    aux_2 = Cola()

    personaje = ['The Beyonder','Franklin Richards','The Chaos King','Phoenix','Mystique','X-23','Wolverine','Ant-Man','Captain Marvel']
    sexo = ['M','M','M','F','F','F','M','M','F']
    nombre = ['Frank','Franklin Benjamin Richards','Amatsu-Mikaboshi','Jean Grey SUmmers','Raven Darkholme','Laura Kinney',
    'James Howlett','Scott Lang','Carol Danvers']

    for x in range(0,9):
        character,sex,name = personaje[x],sexo[x],nombre[x]
        encolar(personajes, [name,character,sex])
    print('personajes de Marvel')
    barrido_cola(personajes)
    while not cola_vacia(personajes):
        c = desencolar(personajes)
        encolar(aux, c)
        if c[1] == 'Captain Marvel':
            print('')
            print('el nombre de',c[1],'es',c[0])
        if c[2] == 'F':
            encolar(femenino,c[1])
        if c[2] == 'M':
            encolar(masculino, c[1])
    print('')
    print('personajes femeninos')
    barrido_cola(femenino)     
    print('')
    print('personajes masculinos')
    barrido_cola(masculino)     
    print('')
    while not cola_vacia(aux):
        c = desencolar(aux)
        encolar(aux_2, c)
        letra = c[0]
        if c[0] == 'Scott Lang':
            print('el nombre del personaje', c[0], 'es', c[1])
        if letra[0] == 'S':
            print('personajes que empiezan con S', c) 
    print('')
    while not cola_vacia(aux_2):
        CarolDanvers = False
        c = desencolar(aux_2)
        if c[0] == 'Carol Danvers':
            CarolDanvers = True
    if CarolDanvers:
        print('el personaje',c[0],'se encuentra y su nombre es',c[1])
    else:
        print('el personaje', c[0],'no se encuentra')