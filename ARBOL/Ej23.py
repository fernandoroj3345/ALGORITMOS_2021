from TDA_ArbolBin import Arbol
from TDA_Cola import Cola
'''
Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:

A)Listado inorden de las criaturas y quienes la derrotaron;
B) se debe permitir cargar una breve descripción sobre cada criatura;
C) mostrar toda la información de la criatura Talos;
D) Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
E) Listar las criaturas derrotadas por Heracles;
F) Listar las criaturas que no han sido derrotadas;
G) Además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
H) Modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
I) Se debe permitir búsquedas por coincidencia;
J) Eliminar al Basilisco y a las Sirenas;
K) Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
L) Modifique el nombre de la criatura Ladón por Dragón Ladón;
M) Realizar un listado por nivel del árbol;
N) Muestre las criaturas capturadas por Heracles.
'''
datos = [ 
    {'nombre' : 'Ceto', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Cerda de Cromión', 'capturada' : 'Teseo', 'descripcion' : ''},
    {'nombre' : 'Tifón', 'capturada' : 'Zeus', 'descripcion' : ''}, 
    {'nombre' : 'Ortro', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Equidna', 'capturada' : 'Argos Panoptes', 'descripcion' : ''}, 
    {'nombre' : 'Toro de Creta', 'capturada' : 'Teseo', 'descripcion' : ''},
    {'nombre' : 'Dino', 'capturada' : '', 'descripcion' : 'toro'}, 
    {'nombre' : 'Jabalí de Calidón', 'capturada' : 'Atalanta', 'descripcion' : ''},
    {'nombre' : 'Pefredo', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Carcinos', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Enio', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Gerión', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Escila', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Cloto', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Caribdis', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Laquesis', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Euríale', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Atropos', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Esteno', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Minotauro de Creta', 'capturada' : 'Teseo', 'descripcion' : ''},
    {'nombre' : 'Medusa', 'capturada' : 'Perseo', 'descripcion' : ''},
    {'nombre' : 'Harpías', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Ladón', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Argos Panoptes', 'capturada' : 'Hermes', 'descripcion' : ''},
    {'nombre' : 'Aguila del Cáucaso', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Aves del Estínfalo', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Quimera', 'capturada' : 'Belerofonte', 'descripcion' : ''},
    {'nombre' : 'Talos', 'capturada' : 'Medea', 'descripcion' : ''},
    {'nombre' : 'Hidra de Lerna', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Sirenas', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'León de Nemea', 'capturada' : 'Heracles', 'descripcion' : ''},
    {'nombre' : 'Pitón', 'capturada' : 'Apolo', 'descripcion' : ''},
    {'nombre' : 'Esfinge', 'capturada' : 'Edipo', 'descripcion' : ''},
    {'nombre' : 'Cierva de Cerinea', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Dragón de la Cólquida', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Basilisco', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Cerbero', 'capturada' : '', 'descripcion' : ''},
    {'nombre' : 'Jabalí de Erimanto', 'capturada' : '', 'descripcion' : ''} 
]

criaturas = Arbol()
for criatura in datos:# Armado del arbol
    criaturas = criaturas.insertar_nodo(criatura['nombre'], criatura) 

#A)Listado inorden de las criaturas y quienes la derrotaron;
print("\n")
criaturas.barrido_derrotados_por()


#B) se debe permitir cargar una breve descripción sobre cada criatura;
criatura = input('Ingrese Una Criatura Para Editar: ') 
criaturas.cargar_descripcion(criatura)


#C) mostrar toda la información de la criatura Talos;
print('Informacion De La Criatura Talos:')
criaturas.mostrar_informacion('Talos')


#D) Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
def ordenar(elemento): 
    return (elemento[1])

dic = {} #Hago diccionario vacio para poder cargar luego.
criaturas.contador_criaturas_derrotadas(dic)
lista = list(dic.items()) # Creo una lista con los items del diccionario
lista.sort(key=ordenar, reverse=True)

print('\nHeroes/Dioses que derrotaron a la mayor cantidad de criaturas:')
for pos in range (0,3):
	print(lista[pos][0], '(derroto a',  lista[pos][1], 'criatura(s))') # [i]:posicion en la lista... []:campo

#E) Listar las criaturas derrotadas por Heracles;
print('\nLista de criaturas derrotadas por Heracles:')
criaturas.criaturas_derrotadas('Heracles')


#F) Listar las criaturas que no han sido derrotadas;
print('\nLista de criaturas que no han sido derrotadas:')
criaturas.criaturas_no_derrotadas()


#H) Modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;

criaturas.modificar_captura('Cerbero','Heracles')
criaturas.modificar_captura('Toro de Creta','Heracles')
criaturas.modificar_captura('Cierva de Cerinea','Heracles')
criaturas.modificar_captura('Jabalí de Erimanto','Heracles')
print()
# criaturas.inorden_criaturas()

#I)Se debe permitir búsquedas por coincidencia;
clave = input('Comience a escribir parte del nombre de una criatura para buscarla: ')
print('Criaturas que contienen "', clave, '" en su nombre:' )
criaturas.busqueda_por_coincidencia(clave)
print()

#J) Eliminar al Basilisco y a las Sirenas;
info, datos = criaturas.eliminar_nodo('Basilisco')
print (info, 'ha sido eliminado')
info, datos = criaturas.eliminar_nodo('Sirenas')
print (info, 'ha sido eliminado')
print()
# criaturas.inorden_criaturas()

#K) Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias;
pos = criaturas.busqueda('Aves del Estínfalo')
if (pos):
    pos.datos['capturada'] = 'Heracles'
    pos.datos['descripcion'] = 'Heracles derrotó a varias.'
print ()

#L
pos = criaturas.busqueda('Ladón')
if (pos):
    nombre, datos = criaturas.eliminar_nodo('Ladón')
    datos['nombre'] = 'Dragón Ladón'
    criaturas = criaturas.insertar_nodo('Dragón Ladón', datos)
print()

#M) Realizar un listado por nivel del árbol;
print('\nBarrido por nivel del arbol:')
criaturas.barrido_por_nivel()
print()

#N) Muestre las criaturas capturadas por Heracles.
print('Lista de criaturas capturadas por Heracles:')
criaturas.criaturas_derrotadas('Heracles')
print()