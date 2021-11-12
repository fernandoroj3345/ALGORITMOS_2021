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

starwarsplanet()
