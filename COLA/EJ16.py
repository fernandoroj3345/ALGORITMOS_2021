from TDA_COLA import Cola,encolar,desencolar,cola_vacia,tamanio_cola,colaint,colaintpn,colacadenas,colastring,barrido_cola,en_frente,mover_final
from TDA_HEAP import *

cola_prioridad = HeapMax()

from TDA_COLA import Cola,encolar,desencolar,cola_vacia,tamanio_cola,colaint,colaintpn,colacadenas,colastring,barrido_cola,en_frente,mover_final
from TDA_HEAP import *
#EJ Nº16

#Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
#criterio (1- empleados, 2- Staff de tecnologías de la información “TI”, 3- Gerente), y resuelva la
#siguiente situación:
#A. cargue tres documentos de empleados (cada documento se representa solamente con
#un nombre).
#B. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
#C. cargue dos documentos del staff de TI.
#D. cargue un documento del gerente.
#E. imprima los dos primeros documentos de la cola.
#F. cargue dos documentos de empleados y uno de gerente.
#G. imprima todos los documentos de la cola de impresión.

# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:

cola_prioridad = HeapMax()#clase HeapMax defino la cola de prioridad.

#A)
#Cargue tres documentos de empleados (cada documento se representa solamente con
#un nombre).
print('Punto A, Los Datos De los Empleados Fueron Cargados')
cola_prioridad.encolar('DocumentoPepitoNº1',1)#3 el de la prioridad.
cola_prioridad.encolar('DocumentoJuanNº2',1)
cola_prioridad.encolar('DocumentoNanoNº3',1)#este tipo tambien tiene prioridad
print(cola_prioridad.elementos)
print()

#B)
#Imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print('Punto B,El Primer Documento Es:')
print(cola_prioridad.desencolar()[1])#muestro lo que saco en la posicion 1 (pepito)
print()

#C)
#Cargue dos documentos del staff de TI.
print('Punto C,Se Cargaron los Documentos del Staff TI')
cola_prioridad.encolar('DocumentoTI1_Moncho', 2)
cola_prioridad.encolar('DocumentoTI2_Rufo', 2)
print(cola_prioridad.elementos)
print()

#D)
#Cargue un documento del gerente.
print('Punto D:Se Cargaron los Datos del Gerente General')
cola_prioridad.encolar('DocumentoGerente1_Fernando', 3)
print(cola_prioridad.elementos)
print()

#E)
#Imprima los dos primeros documentos de la cola.
print('Punto E:Los 2 primeros Documentos son:')
print(cola_prioridad.desencolar()[1])
print(cola_prioridad.desencolar()[1])
print()

#F)
#Cargue dos documentos de empleados y uno de gerente.
print('Punto F:Se Cargo un Empleado y Un Gerente:')
cola_prioridad.encolar('DocumentoEmpleado4', 1)
cola_prioridad.encolar('DocumentoEmpleado5', 1)
cola_prioridad.encolar('DocumentoGerente_N°2', 3)
print(cola_prioridad.elementos)
print()

#G)
#Imprima todos los documentos de la cola de impresión.
print('Los Documentos de la Cola de Impresion son:')
while (not cola_prioridad.vacio()):#mientras no este vacia,osea que tenga elementos, muestro los desencolados.
    print(cola_prioridad.desencolar()[1])

print()