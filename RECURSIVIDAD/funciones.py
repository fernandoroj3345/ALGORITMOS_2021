#EJ 5
#Desarrollar una función que permita convertir un número romano en un número decimal.
def romano(n):
  if n == "":
    return 0
  elif n == "M":
    return 1000
  elif n == "D":
    return 500
  elif n == "C":
    return 100
  elif n == "L":
    return 50
  elif n == "X":
    return 10
  elif n == "V":
    return 5
  elif n == "I":
    return 1
  else:
    if romano(n[0])<romano(n[1]):
      return (romano(n[1])-romano(n[0]))+romano(n[2:])
    else:
      return romano(n[0])+romano(n[1:])

(romano("DI"))

#################################################################################################################

#EJ 8
#Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def decimal_binario(numero):
    if numero == 0:
        return ""
    else:
        return decimal_binario(numero//2) + str(numero % 2)
assert decimal_binario["se cargo mal"]
#################################################################################################################

#EJ 22
#El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;
#c. Utilizar un vector para representar la mochila.

def Usarlafuerza(arr,x,indice):
        if arr[indice] == x:
            print(x)
            print('se sacaron ',indice,'objetos')
        else:
            print(arr[indice])
            Usarlafuerza(arr,x,indice+1)
mochila = ['enano','ryzen9','piedra','sable de luz','papel']
Usarlafuerza(mochila,'sable de luz',0)



#################################################################################################################

#EJ 23
#Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
#matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
#y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
#y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
#avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo.

laberinto = [[0, 0, 0],
	          [1,  1, 0],
	          [1,  0, 2]]

def buscar_salida(x, y):
    if laberinto[x][y] == 2:
        print('salida en '+ str((x,y)))
        return True
    elif laberinto[x][y] == 1:
        print("pared en " + str((x,y)))
        return False 
    elif laberinto[x][y] == '*':
        return False
    laberinto[x][y] = '*'
    print ('visitando ' + str((x,y)))
    # buscar salidas recursivas
    if((x < len(laberinto)-1 and buscar_salida(x+1, y)) #derecha
	        or (y > 0 and buscar_salida(x, y-1))    # abajo
	        or (x > 0 and buscar_salida(x-1, y))    # izquierda
	        or (y < len(laberinto)-1 and buscar_salida(x, y+1))): #arriba
	        return True
    else:
        return False

####################################################################################################################

#EJ 24
#En el momento de la creación del mundo, los sacerdotes del templo de Brahma recibieron una
#plataforma de bronce sobre la cual había tres agujas de diamante. En la primera aguja estaban
#apilados setenta y cuatro discos de oro, cada una ligeramente menor que la que estaba debajo.
#A los sacerdotes se les encomendó la tarea de pasarlos todos desde la primera aguja a la tercera,
#con dos condiciones, solo puede moverse un disco a la vez, y ningún disco podrá ponerse en-
#cima de otro más pequeño. Se dijo a los sacerdotes que, cuando hubieran terminado de mover
#los discos, llegaría el fin del mundo. Resolver este problema de la Torre de Hanói.

def hanoi(n,  origen,auxiliar, destino):
    if n == 1:
        print("mover disco de " + str(origen) + " a " + str(destino))
    else:
        hanoi(n-1, origen, destino, auxiliar);
        print("mover disco de "+ str(origen) + " a " + str(destino))
        hanoi(n-1, auxiliar, origen, destino)

print (romano('DI'))