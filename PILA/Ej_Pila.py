from random import randint
from tdapila import Pila

# EJ 1 Determinar el número de ocurrencias de un determinado elemento en una pila.
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

###################################################################################################################

#EJ 14 ENTREGAR COMO TP

#Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente.
# Solo puede utilizar una pila auxiliar como estructura extra no se no pueden utilizar métodos de ordenamiento –.

def crecientes():
    p = Pila()#p es el objeto
    p_aux = Pila()#p_aux es el objeto
    for i in range (0, 5):
        dato = int(input('Ingrese un numero: '))
        if p.pila_vacia() or p.elemento_cima()<=dato:
            p.apilar(dato)
        else:
            while (not  p.pila_vacia() and p.elemento_cima() >= dato):
               # print(str(dato) + 'numero agregado')#str(dato)convierte el dato en un string
                
                if not p.pila_vacia():   # ingresa cuando hay al menos un elemento en P
                    while not p.pila_vacia() and p.elemento_cima() >= dato:
            
                        p_aux.apilar(p.desapilar())#el elemento que desapila en p lo apilo en p_aux
                
            p.apilar(dato)

            while not p_aux.pila_vacia():
                 p.apilar (p_aux.desapilar())
    print('pila ordenada de forma creciente')
    p.barrido_pila()

crecientes()


####################################################################################################################

#EJ 16 ENTREGAR COMO TP

#Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.
#tips:
#  esto seria loq tengoq hacer
#  desapilar una pila e ir comparando los elementos con los demas para veer si coinciden o no.

pila_empire = Pila()
pila_awakens = Pila()
pila_interseccion = Pila()
pila_aux = Pila()

empire = ['Han Solo', 'Luke Skywalker', 'Leia Organa', 'Lando Calrissian', 'Darth Vader', 
          'Chewbacca', 'Yoda', 'Boba Fett','Obi-Wan Kenobi', 'R2-D2', 'C-3PO']
awakens = ['Rey', 'Finn', 'Poe Dameron' ,'Leia Organa', 'Luke Skywalker', 'Han Solo', 'Kylo Ren',
           'Chewbacca', 'R2-D2', 'C-3PO', 'Maz Kanata']



for elemento in empire:
    pila_empire.apilar(elemento)

for elemento in awakens:
    pila_awakens.apilar(elemento)

while not pila_empire.pila_vacia():
    e = pila_empire.desapilar()
    
    while not pila_awakens.pila_vacia():
        a = pila_awakens.desapilar()
        if (e == a):
            pila_interseccion.apilar(e)
        else:
            pila_aux.apilar(a)

    while not pila_aux.pila_vacia():
        pila_awakens.apilar(pila_aux.desapilar())

print ('Los personajes que aparecen en ambas películas son:')
while not pila_interseccion.pila_vacia():
    print ('-', pila_interseccion.desapilar())

####################################################################################################################

#EJ 22 ENTREGAR COMO TP

#Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
#Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
#misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
#costo de la recompensa. Resolver las siguientes actividades:
#a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
#de los cazarrecompensas;
#b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
#quien obtuvo mayor fortuna;
#c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
#que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
#d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.

pila_bobaFett = Pila()
pila_Din_Djarin = Pila()
pila_auxbobafett = Pila()
credito_bobafett = 0
credito_din_djarin = 0

boba_Fett=[['Alderan','Leia',500],['Totooine','HanSolo',100000]]
Din_Jarin=[['Yarbin4','JarJarBinks',600],['Luke','Luna',30000]] 
for element in boba_Fett: # for element ,toma los arreglos que estan dentro
    pila_bobaFett.apilar(element)
for element in Din_Jarin: # for element ,toma los arreglos que estan dentro
    pila_Din_Djarin.apilar(element)    
i = 1
#PUNTO A

#Pasar toda la pila de de bobba fett a uan auxiliar para invertirla.dps desapilo y muestro.
while not pila_bobaFett.pila_vacia():#dos puntos cuando es un ciclo o un if 
     #aqui solo llamo al metodo no van los dos puntos
    pila_auxbobafett.apilar(pila_bobaFett.desapilar())
    ## muestro los planetas desde aca.
while not pila_auxbobafett.pila_vacia():
    print(pila_auxbobafett.desapilar()[0])

for element in boba_Fett: # for element ,toma los arreglos que estan dentro
    pila_bobaFett.apilar(element)
for element in Din_Jarin: # for element ,toma los arreglos que estan dentro
    pila_Din_Djarin.apilar(element)    

#PUNTO B
#determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
#quien obtuvo mayor fortuna
while not pila_bobaFett.pila_vacia():
    credito_bobafett = pila_bobaFett.desapilar()[2]+credito_bobafett

while not pila_Din_Djarin.pila_vacia():
    credito_din_djarin = pila_Din_Djarin.desapilar()[2]+credito_din_djarin

if credito_din_djarin > credito_bobafett:
    print('El Credito de Din Djarin es major al de Bobafett ', credito_din_djarin)
elif  credito_bobafett > credito_din_djarin : 
    print ('El Credito de BobaFett es major al de Din Djarin ', credito_bobafett)
else :
    print ('Ambos creditos son Iguales')

#C determinar el número de la misión es decir su posición desde el fondo de la pila en la
#que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;

for element in boba_Fett: # for element ,toma los arreglos que estan dentro
    pila_bobaFett.apilar(element)
    
i = 0

while not pila_bobaFett.pila_vacia():#dos puntos cuando es un ciclo o un if 
     #aqui solo llamo al metodo no van los dos puntos
    pila_auxbobafett.apilar(pila_bobaFett.desapilar())
while not pila_auxbobafett.pila_vacia():
    aux=pila_auxbobafett.desapilar()
    i = i+1
    if aux[1]== 'Han Solo':
        print ('Boba Fett lo capturo en la mision',i)


#D indicar la cantidad de capturas realizadas por cada cazarrecompensas.
for element in boba_Fett: # for element ,toma los arreglos que estan dentro
    pila_bobaFett.apilar(element)
for element in Din_Jarin: # for element ,toma los arreglos que estan dentro
    pila_Din_Djarin.apilar(element)    

print ('La Cantidad de capturas de Bobafet son', pila_bobaFett.tamanio())
print ('La Cantidad de capturas de Din Djarin son', pila_Din_Djarin.tamanio())


    
  
#################################################################################################################

#EJ 24 ENTREGAR COMO TP

#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#A. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;
#[86]
#B. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas 
# en la que aparece;
#C. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#D. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pila = Pila()
personajes = [['Rocket Raccoon', '4'],['Black Widow','5'],['Iron-Man','6'],['Groot','4'],['Thor','5']]
for i in range(0,5):
    personajes.apilar(pila, personajes[i])
i = 1
while not personajes.pila_vacia():
    personaje = personajes.desapilar(pila)
    #A Posicion en que se encuentran Rocket y Groot
    if(personaje[0] == 'Rocket Raccoon' or personaje[0] == 'Groot'):
        print(personaje[0], 'esta en la posicion', i)
    #B Personajes que participaron en más de 5 peliculas
    if(int(personaje[1]) > 5):
        print(personaje[0], 'participó en mas de 5 peliculas')
    #C Cantidad de pelis en las que participó Black Widow
    if(personaje[0] == 'Black Widow'):
        print(personaje[0], 'participo en', personaje[1], 'peliculas')
    #D Mostrar personjaes que empiecen con C, D o G
    if(personaje[0][0] in ['C', 'D', 'G']):
        print(personaje[0], 'comienza con', personaje[0][0])
    i += 1
