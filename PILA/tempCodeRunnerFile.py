def ocurrencia():
    pila_1 = Pila()#inicializo la pila
    for i in range(0, 5):
        pila_1.apilar(randint(0, 3))#.apilar es mi funcion.
    cantidad = 0
    contar = int(input('ingrese el numero que desea contar '))
    while(not pila_1.pila_vacia()):
        x = pila_1.desapilar()
        if(x == contar):
            cantidad += 1
    print("Cantidad de elementos: ", cantidad)       

ocurrencia()