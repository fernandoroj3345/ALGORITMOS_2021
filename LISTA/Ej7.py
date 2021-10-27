from TDA_LISTA import Lista,insertar,barrido_lista,eliminar,busqueda_lista,tamanio_lista

'''
Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
'''
def dos_listas(l1, l2):
    print('Lista 1')
    barrido_lista(l1)
    print('Lista 2')
    barrido_lista(l2)

    # a)
    def lista_concatenada(l1, l2):
        '''Concatena dos listas, una atras de la otra'''
        lconc = Lista()
        lconc = l1
        aux = lconc.inicio
        while aux.sig is not None:
            aux = aux.sig
        aux.sig = l2.inicio
        print('Lista concantenada')
        barrido_lista(lconc)

    # b) y c)
    def lista_sin_repetidos(l1, l2):
        '''Concatena dos listas en una sola omitiendo los datos repetidos'''
        lsr = Lista()
        aux = l1.inicio
        while aux is not None:
            if busqueda_lista(lsr, aux.info) is None:
                insertar(lsr, aux.info)
            aux = aux.sig
        aux = l2.inicio
        while aux is not None:
            if busqueda_lista(lsr, aux.info) is None:
                insertar(lsr, aux.info)
            aux = aux.sig
        print('Lista concatenada sin repetidos')
        barrido_lista(lsr)
        print('Datos repetidos:', tamanio_lista(lsr))

    # d)
    def eliminar_nodos(l1):
        '''Elimina los nodos de una lista'''
        aux = l1.inicio
        while aux is not None:
            eliminar(l1, aux.info)
            print('Se elimino:', aux.info)
            aux = aux.sig


    lista_concatenada(l1, l2)
    lista_sin_repetidos(l1, l2)
    eliminar_nodos(l1)
