'''
Desarrollar un algoritmo que implemente dos funciones, una para obtener el mínimo nodo del
árbol y la segunda para obtener el máximo.
'''
arbol = None
for i in range(0, 10):
    arbol = insertar_nodo(arbol, randint(0, 100))
print('Arbol')
inorden(arbol)
print()

min = nodo_minimo(arbol)
max = nodo_maximo(arbol)
print('Nodo minimo del arbol:', min.info)
print('Nodo maximo del arbol:', max.info)


