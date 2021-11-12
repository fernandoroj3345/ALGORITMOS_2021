from TDA_COLA import Cola,encolar,desencolar,cola_vacia,tamanio_cola,colaint,colaintpn,colacadenas,colastring,barrido_cola,en_frente,mover_final


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
MarvelUniverse()