vec_recursivo = [ 'Palpatine','Luke SkY Walker','Dart Vader,Yoda,Darth Maul',' BB 8' ]

'''
Dado un vector con personaje de las películas de la saga de Star Wars resolver las
siguientes actividades:
A.
Realizar un barrido recursivo del vector.
B.
Realizar una función recursiva que permita determinar si ‘Yoda’ está en el
vector y en que posición.
'''
#Punto A
def barrido(vec_recursivo):
    if(len(vec_recursivo)>0):
        print(vec_recursivo[0])
        barrido(vec_recursivo[1:])

#Punto B
vec_recursivo = [ 'Palpatine','Luke SkY Walker','Dart Vader,Yoda,Darth Maul',' BB 8' ]
def (vec_recursivo, pos):
    if(pos< len(vec_recursivo)):
        if(vec_recursivo[pos] == 'Yoda'):
            return pos
        else:
            return vec_recursivo(vec_recursivo, pos+1)
    else:
        return -1








   



