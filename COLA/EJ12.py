from TDA_COLA import Cola,encolar,desencolar,cola_vacia,tamanio_cola,colaint,colaintpn,colacadenas,colastring,barrido_cola,en_frente,mover_final
#EJ Nº12

#Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
#nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
#ni métodos de ordenamiento.


def ordenados():
    cola1 = Cola()
    cola2 = Cola()

# ver si poder usar vector
# vector numeros_enteros [cargargo los datos]
    print("Cargo Datos")
    while tamanio_cola(cola1)<5:
        dato = int(input('ingrese un numero '))
        encolar(cola1, dato)
    print('cola 1')
    barrido_cola(cola1)# en lugar de print utilizo el tda
    print()
    print("Cargo Datos")
    while tamanio_cola(cola2)<5:#cargo menos de 7 elementos
        dato = int(input('ingrese un numero '))
        encolar(cola2, dato)
    print('cola 2')
    print()
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
ordenados()