'''
Una empresa de nano satélites dedicada al monitoreo de lotes campo destinados al agro, tiene
problemas para la transmisión de los datos recolectados, dado que la ventana de tiempo que
dispone para enviar los datos antes de una nueva medición es muy corta, por lo que nos solicita
desarrollar un algoritmo que permita comprimir la información para poder enviarla más rápi-
do, para lo cual se debe tener en cuenta los siguientes requerimientos:
a. la información transmitida por el nano satélite son estado del tiempo, humedad del suelo,
y tres dígitos que identifican el lote al cual pertenecen los datos;
b. desarrollar un árbol de Huffman que permita comprimir la información para transmitirla,
la frecuencia de la información transmitida se observa en la siguiente tabla:
'''
arbol= None