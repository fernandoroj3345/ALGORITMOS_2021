from TDA_ArbolBinario import *
from TDA_Cola import *
'''
Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
A. listado inorden de las criaturas y quienes la derrotaron;
B. se debe permitir cargar una breve descripción sobre cada criatura;
C. mostrar toda la información de la criatura Talos;
D. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
E. listar las criaturas derrotadas por Heracles;
F. listar las criaturas que no han sido derrotadas;
G. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
H. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
I. se debe permitir búsquedas por coincidencia;
J. eliminar al Basilisco y a las Sirenas;
K. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
L. modifique el nombre de la criatura Ladón por Dragón Ladón;
M. realizar un listado por nivel del árbol;
N. muestre las criaturas capturadas por Heracles.
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

arbol_criaturas = Arbol()

for criatura in datos:
    arbol_criaturas = arbol_criaturas.insertar_nodo(criatura['nombre'], criatura) 

#! ---- PUNTO A ----!#
arbol_criaturas.inorden_criaturas()
print()

#! ---- PUNTO B ----!#
criatura = input('Ingrese una criatura para agregarle una breve descripcion: ')
arbol_criaturas.cargar_descripcion(criatura)
print()

#! ---- PUNTO C ----!#
print('Informacion de la criatura Talos:')
arbol_criaturas.mostrar_informacion('Talos')
print()

#! ---- PUNTO D ----!#
def ordenar(elemento):
    return elemento[1]

dic = {}
arbol_criaturas.contador_criaturas_derrotadas(dic)
lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)

print('Los 3 heroes o dioses que derrotaron a la mayor cantidad de criaturas son:')
for i in range (3):
	print(lista[i][0], '(derroto a',  lista[i][1], 'criatura(s))')
print()


#! ---- PUNTO E ----!#
print('Lista de criaturas derrotadas por Heracles:')
arbol_criaturas.criaturas_derrotadas('Heracles')
print()

#! ---- PUNTO F ----!#
print('Lista de criaturas que no han sido derrotadas:')
arbol_criaturas.criaturas_no_derrotadas()
print()

#! ---- PUNTO H ----!#
arbol_criaturas.modificar_captura('Cerbero', 'Heracles')
arbol_criaturas.modificar_captura('Toro de Creta', 'Heracles')
arbol_criaturas.modificar_captura('Cierva de Cerinea', 'Heracles')
arbol_criaturas.modificar_captura('Jabalí de Erimanto', 'Heracles')
print()
# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO I ----!#
clave = input('Comience a escribir parte del nombre de una criatura para buscarla: ')
print('Criaturas que contienen "', clave, '" en su nombre:' )
arbol_criaturas.busqueda_por_coincidencia(clave)
print()

#! ---- PUNTO J ----!#
info, datos = arbol_criaturas.eliminar_nodo('Basilisco')
print (info, 'ha sido eliminado')
info, datos = arbol_criaturas.eliminar_nodo('Sirenas')
print (info, 'ha sido eliminado')
print()
# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO K ----!#
pos = arbol_criaturas.busqueda('Aves del Estínfalo')
if (pos):
    pos.datos['capturada'] = 'Heracles'
    pos.datos['descripcion'] = 'Heracles derrotó a varias.'
# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO L ----!#
pos = arbol_criaturas.busqueda('Ladón')
if (pos):
    nombre, datos = arbol_criaturas.eliminar_nodo('Ladón')
    datos['nombre'] = 'Dragón Ladón'
    arbol_criaturas = arbol_criaturas.insertar_nodo('Dragón Ladón', datos)

# arbol_criaturas.inorden_criaturas()

#! ---- PUNTO M ----!#
print('Barrido por nivel del arbol:')
arbol_criaturas.barrido_por_nivel()
print()


#! ---- PUNTO N ----!#
print('Lista de criaturas capturadas por Heracles:')
arbol_criaturas.criaturas_derrotadas('Heracles')
print()