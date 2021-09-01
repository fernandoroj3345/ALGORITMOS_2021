from TDA_COLA import Cola,encolar,desencolar,cola_vacia,tamanio_cola,colaint,colaintpn,colacadenas,colastring,barrido_cola,en_frente,mover_final


#EJ Nº11

#Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
#A. mostrar los personajes del planeta Alderaan, Endor y Tatooine.
#B. indicar el planeta natal de Luke Skywalker y Han Solo.
#C. insertar un nuevo personaje antes del maestro Yoda.
#D. eliminar el personaje ubicado después de Jar Jar Binks.

def starwarsplanet(): 
    starwars = Cola()
    starwars1 = Cola()
    starwars2 = Cola()
    aux = Cola()
    


    personajes = ['Luke Skywalker','Han Solo','Yoda','Jar Jar Binks','Nippet','Leila Organa','Chewbacca','C3P0','R2D2']
    planet =    ['Tatooine', 'Corellia', 'Dagobah', 'Naboo', 'Endor', 'Alderaan', 'Kashyyyk','None','Moon']



    for elemento in range(0,8):
        personaje, planeta = personajes[elemento], planet[elemento]
        encolar(starwars, [personaje, planeta])#Personaje es posicion 0 y planeta posicion 1 

#PUNTO A B y C
    while not cola_vacia(starwars):
        dato=desencolar(starwars)
        #PUNTO A Y B
        if dato[1]=='Alderaan' or dato[1]=='Tatooine' or dato[1]=='Endor':
            print(dato[0],'Es del Planeta',dato[1])
        if dato[0]=='Luke Skywalker':
            print('El planeta de Luke Skywalker es',dato[1])
        if dato[0]=='Han Solo':
            print('El planeta de Han Solo es',dato[1])
        #PUNTO C
        if dato[0] != 'Yoda':
            encolar(aux,dato)      
        else:
            encolar(starwars1, ['Sheev Palpatine','Naboo'])
            encolar(starwars1,dato)
        encolar(aux,dato)
        while not cola_vacia(aux):
            dato = desencolar(aux)
            #PUNTO D
            if dato[0] == 'Jar Jar Binks' and not cola_vacia(aux):
                desencolar(aux)
            encolar(starwars2,dato)
    print()
    print('Agregar personaje antes de Yoda')
    #PUNTO C
#if(dato[0] == 'Jar jar Binks'):
    #encolar(nuevo personaje 2) #muestra la condicion de la linea 62 y 63

    cola_aux = Cola()
    while (not cola_vacia(starwars2)):
        dato = desencolar(starwars2)
        if (dato[0]=='Yoda'):
            encolar(cola_aux, ["nuevo personaje 2", "planeta nuevo personaje 2"])
        encolar(cola_aux,dato)
    
    while (not cola_vacia(cola_aux)):#paso los datos de la cola auxilar a la cola starwars2 para volver a tener los datos en la cola incial
        encolar(starwars2,desencolar(cola_aux))
    print("Barrido punto C")#comprueba si agrego al personaje nuevo
    barrido_cola(starwars2)

    barrido_cola(starwars1)
    print()
    print('Eliminar personaje despues de Jar Jar Binks')
    barrido_cola(starwars2)

#D. eliminar el personaje ubicado después de Jar Jar Binks
    cola_aux = Cola()
    while (not cola_vacia(starwars2)):
        dato = desencolar(starwars2)
        if (dato[0]=='Jar Jar Binks'):
            desencolar(starwars2)
        encolar(cola_aux,dato)
    while (not cola_vacia(cola_aux)):#paso los datos de la cola auxilar a la cola starwars2 para volver a tener los datos en la cola incial
        encolar(starwars2,desencolar(cola_aux))
    print("Barrido punto D")#comprueba la eliminacion de jar jar Bins
    barrido_cola(starwars2)


############################################################################################################
#EJ Nº12

#Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
#nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
#ni métodos de ordenamiento.


def ordenados():
    cola1 = Cola()
    cola2 = Cola()

# ver si poder usar vector
# vector numeros_enteros [cargargo los datos]
    
    while tamanio_cola(cola1)<5:
        dato = int(input('ingrese un numero '))
        encolar(cola1, dato)
    print('cola 1')
    barrido_cola(cola1)# en lugar de print utilizo el tda
    while tamanio_cola(cola2)<5:#cargo menos de 7 elementos
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

#NO HAECER AUN
#Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
#criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
#siguiente situación:
#a. cargue tres documentos de empleados (cada documento se representa solamente con
#un nombre).
#b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#c. cargue dos documentos del staff de TI.
#d. cargue un documento del gerente.
#e. imprima los dos primeros documentos de la cola.
#f. cargue dos documentos de empleados y uno de gerente.
#g. imprima todos los documentos de la cola de impresión.


#############################################################################################################
#EJ Nº22

#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
#ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino F) 
#–por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
#manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
#A. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#B. mostrar los nombre de los superhéroes femeninos;
#C. mostrar los nombres de los personajes masculinos;
#D. determinar el nombre del superhéroe del personaje Scott Lang;
#E. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
#F. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#de superhéroes.


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




