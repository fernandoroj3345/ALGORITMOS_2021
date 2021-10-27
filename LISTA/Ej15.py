from TDA_LISTA import randint,insertar,busqueda_lista,Lista,barrido_lista,tamanio_lista,choice,barrido_sublista

'''
Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
rrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos;
'''
class Entrenador():
    def __init__(self, entrandor, t_ganados, b_ganadas, b_perdidas):
        self.entrenador = entrandor
        self.t_ganados = t_ganados
        self.b_ganadas = b_ganadas
        self.b_perdidas = b_perdidas

    def __str__(self):# muestra la informacion de la lista
        return self.entrenador + ' | ' + str(self.t_ganados) + ' | ' + str(self.b_ganadas) + ' | ' + str(self.b_perdidas)


class Pokemon():
    def __init__(self, pokemon, nivel, tipo, subtipo):
        self.pokemon = pokemon
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return self.pokemon + ' | ' + str(self.nivel) + ' | ' + self.tipo + ' | ' + self.subtipo

#cargo la lista con todos los  datos
def pokemon():
    lista = Lista()
    pokemon = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Spearow',
               'Dugtrio', 'Primeape', 'Terrakion', 'Tyrantrum', 'Wingull']
    tipo = ['Fuego', 'Agua', 'Electrico', 'Normal', 'Veneno']
    subtipo = ['Tierra', '-', 'Planta', 'Agua', '-', 'Volador']
    dato = Entrenador('Ranchero', randint(0, 20), randint(50, 150), randint(0, 180))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Alevin', randint(0, 20), randint(50, 150), randint(0, 180))
    insertar(lista, dato, 'entrenador')
    dato = Entrenador('Pescador', randint(0, 20), randint(50, 150), randint(0, 180))
    insertar(lista, dato, 'entrenador')
    for i in range(2):#cargo 2 pokemons
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Ranchero', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(3):#cargo 3 pokemons
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Alevin', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    for i in range(4):#cargo 4 pokemons
        poke = Pokemon(choice(pokemon), randint(1, 20), choice(tipo), choice(subtipo))
        pos = busqueda_lista(lista, 'Pescador', 'entrenador')
        insertar(pos.sublista, poke, 'pokemon')
    # d mostrar todos los datos de un entrenador y sus Pokémos
    print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
    barrido_lista(lista)
    print()
    aux = lista.inicio# aux guardo en inicio de la lista
    # barrido sublista
    while aux is not None:
        print('Entrenador:', aux.info.entrenador)
        print('NOMBRE | NIVEL | TIPO | SUBTIPO')
        barrido_sublista(aux.sublista)
        print()
        aux = aux.sig

    # a obtener la cantidad de Pokémons de un determinado entrenador
    aux = lista.inicio
    print('Cantidad de Pokemons de un determinado entrenador')
    entr = input('Ingrese nombre del entrenador: ')
    while aux is not None:
        pos = busqueda_lista(lista, entr, 'entrenador')
        if pos is not None:
            print(aux.info.entrenador, 'posee', tamanio_lista(aux.sublista), 'pokemones')
        else:
            print('El entrenador no existe')
            break
        aux = aux.sig
    print()

    # b listar los entrenadores que hayan ganado más de tres torneos
    aux = lista.inicio
    print('Entrenadores que ganaron mas de 3 torneos')
    while aux is not None:
        if aux.info.t_ganados >= 3:
            print(aux.info.entrenador + ':', aux.info.t_ganados, 'torneos')
        aux = aux.sig
    print()

    # c el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
    aux = lista.inicio
    mg, mn = 0, 0
    while aux is not None:
        if aux.info.t_ganados > mg:
            mg = aux.info.t_ganados
            mas_ganador = aux.info.entrenador
        buscado = busqueda_lista(aux.info.entrenador, mas_ganador, 'entrenador')
        if buscado is not None:
            sublista = aux.sublista.inicio
            while sublista is not None:
                if sublista.info.nivel > mn:
                    mn = sublista.info.nivel
                    mayor_nivel = sublista.info.pokemon
                sublista = sublista.sig
        aux = aux.sig
    print('El entrenador mas ganador es', mas_ganador, 'con', mg, 'torneos')
    print('Su pokemon de mayor nivel es', mayor_nivel, 'con nivel', mn)
    print()

    # e mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %
    aux = lista.inicio
    while aux is not None:
        batallas_totales = aux.info.b_ganadas + aux.info.b_perdidas
        porcentaje_batallas = (aux.info.b_ganadas * 100)/batallas_totales
        if porcentaje_batallas > 79:
            print(aux.info.entrenador, 'tiene un porcentaje de batalladas ganadas mayor a 79%')
        aux = aux.sig
    print()

    # f los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
    #(tipo y subtipo)
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.tipo == 'Fuego' and sublista.info.subtipo == 'Planta':
                print(aux.info.entrenador, 'posee un pokemon tipo fuego y subtipo planta, llamado', sublista.info.pokemon)
            if sublista.info.tipo == 'Agua' and sublista.info.subtipo == 'Volador':
                print(aux.info.entrenador, 'posee un pokemon tipo agua y subtipo volador, llamado', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # g  el promedio de nivel de los Pokémons de un determinado entrenador
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        cont_nivel = 0
        while sublista is not None:
            cont_nivel += sublista.info.nivel
            prom_nivel = cont_nivel / tamanio_lista(aux.sublista)
            sublista = sublista.sig
        # round redondea el valor prom_nivel a 2 digitos despues de la coma
        print(aux.info.entrenador + ', promedio de nivel de sus pokemons:', round(prom_nivel, 2))
        aux = aux.sig
    print()

    # h determinar cuántos entrenadores tienen a un determinado Pokémon
    aux = lista.inicio
    cont = 0
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        pos = busqueda_lista(aux.sublista, poke, 'pokemon')
        if pos is not None:
            cont += 1
        aux = aux.sig
    print(cont, 'entrenadores tienen al pokemon', poke)
    print()

    #I mostrar los entrenadores que tienen Pokémons repetidos


    # j determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
    #rrakion o Wingull
    aux = lista.inicio
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if sublista.info.pokemon == 'Tyrantrum' or sublista.info.pokemon == 'Terrakion' or sublista.info.pokemon == 'Wingull':
                print(aux.info.entrenador, 'tiene al pokemon', sublista.info.pokemon)
            sublista = sublista.sig
        aux = aux.sig
    print()

    # k determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
    #como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
    #deberán mostrar los datos de ambos
    aux = lista.inicio
    print('Busca un entrenador y sus pokemones')
    entr = input('Ingrese nombre de entrenador a buscar: ')
    poke = input('Ingrese nombre de pokemon a buscar: ')
    while aux is not None:
        sublista = aux.sublista.inicio
        while sublista is not None:
            if entr == aux.info.entrenador and poke == sublista.info.pokemon:
                print()
                print('NOMBRE | TORNEOS GAN. | VICTORIAS | DERROTAS')
                print(aux.info)
                print()
                print('NOMBRE | NIVEL | TIPO | SUBTIPO')
                print(sublista.info)
            sublista = sublista.sig
        aux = aux.sig

pokemon()