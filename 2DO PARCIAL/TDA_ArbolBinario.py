from TDA_Cola import Cola
from TDA_Lista import Lista

class Arbol (object):

    def __init__(self, info = None, datos = None, frecuencia = None):
        self.info = info
        self.datos = datos 
        self.frecuencia = frecuencia
        self.der = None
        self.izq = None
        self._altura = 0

    def arbol_vacio(self):
        """Devuelve True si el arbol vacio."""
        return self.info is None

    def altura (self, arbol):
        """Devuelve la altura de un nodo."""
        if (arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura (self):
        """Actualiza la altura de un nodo."""
        if (self is not None):
            alt_izq = self.altura(self.izq)
            alt_der = self.altura(self.der)
            self._altura = (alt_izq if alt_izq > alt_der else alt_der) + 1

    def rotacion_simple (self, control):
        if (control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else: 
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura() 
        aux.actualizar_altura() 
        return aux

    def rotacion_doble (self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos = None): 
        """Inserta un dato clave al ??rbol y opcionalmente hay un campo datos en el que se puede insertar mas informaci??n."""
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden (self):#Esta funcion es la principal para crear los demas in orden.
        """Realiza el barrido inorden del arbol.
        Los elementos se listan en orden ascendente (menor a mayor)."""
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.inorden()
            print (self.info, self.datos)
            if (self.der is not None):
                self.der.inorden()

    def postorden (self):
        """Realiza el barrido postorden del arbol.
        Los elementos se listan en orden descendente (mayor a menor)."""
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden (self):
        """Realiza el barrido preorden del arbol.
        Los elementos se listan en el orden en que fueron cargados."""
        if (self.info is not None):
            print (self.info, self._altura)
            if (self.izq is not None):
                self.izq.preorden()
            if (self.der is not None):
                self.der.preorden()         

    def busqueda (self, clave):
        """Devuelve la direccion del elemento buscado."""
        pos = None
        if (self.info is not None):
            if(self.info == clave):
                pos = self
            elif (clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif (self.der is not None):
                pos = self.der.busqueda(clave)
        return pos

    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)

    def reemplazar (self):
        """Determina el nodo que remplazar?? al que se elimina."""
        aux = None
        if (self.der is None): 
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.reemplazar()
        return info, datos

    def eliminar_nodo (self, clave):
        """Elimina un elemento del ??rbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.reemplazar()
                    self.info = info_aux
                    self.datos = datos_aux
        self = self.balancear()
        self.actualizar_altura()
        return info, datos

    def barrido_por_nivel (self):
        """Realiza el barrido por nivel del arbol."""
        pendientes = Cola()
        pendientes.arribo(self)
        while (not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print (nodo.info)
            if (nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if (nodo.der is not None):
                pendientes.arribo(nodo.der)

    def barrido_por_nivel_huff (self):
        """Realiza el barrido por nivel del arbol con codigos de Huffman."""
        pendientes = Cola()
        pendientes.arribo(self)
        while (not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print (nodo.info, nodo.frecuencia)
            if (nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if (nodo.der is not None):
                pendientes.arribo(nodo.der)               


###################################################################################



#Funciones EJ N??5  

    def inorden_solo_villanos (self):
        """Realiza el barrido inorden del arbol mostrando solo a los villanos.
        Los elementos se listan en orden descendiente (menor a mayor)."""
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.inorden_solo_villanos()
            if (not self.datos['Bando']): 
                print (self.info)
            if (self.der is not None):
                self.der.inorden_solo_villanos()

    def inorden_heroes_LetraC (self):
        """Realiza el barrido inorden del arbol mostrando solo a los heroes cuyo nombre comienza con C.
        Los elementos se listan en orden ascendente (menor a mayor)."""
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.inorden_heroes_LetraC() #ordeno de menor a mayor
            if (self.info[0]=='C'):#en el .info guardo la informacion del nodo.
                print (self.info)
            if (self.der is not None):
                self.der.inorden_heroes_LetraC()

    def contar_nodos (self, categoria):#categoria= campo que le paso (true o false)
        """Cuenta la cantidad de nodos (villanos o heroes) en el arbol, dependiendo de la categoria dada (True para heroes, False para villanos)."""
        cantidad = 0
        if (self.info is not None):#si la raiz el 1er nodo del arbol no esa vacia.
            if (self.datos['Bando'] == categoria):
                cantidad += 1
            #recorro los nodos y llamo a la funcion. 
            if (self.izq is not None):
                cantidad += self.izq.contar_nodos(categoria)
            if (self.der is not None):
                cantidad += self.der.contar_nodos(categoria)
        return cantidad #retorna la cantidad total.

    def postorden_heroes (self):
        """Realiza el barrido postorden del los superheroes en el arbol.
        Los elementos se listan en orden descendente (mayor a menor)."""
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden_heroes()
            if (self.datos['Bando']):
                print(self.info)
            if(self.izq is not None):
                self.izq.postorden_heroes()

    def separar_arbol (self, arbol_aux, categoria):
        """Separa los elementos del arbol en base a la categoria dada (True para heroes, False para villanos)."""
        if(self.info is not None):
            if (self.datos['Bando'] == categoria):
                arbol_aux = arbol_aux.insertar_nodo(self.info, self.datos)#asigno el arbol_auxiliar al insertar nodo
            if(self.izq is not None):
                arbol_aux = self.izq.separar_arbol(arbol_aux, categoria)
            if(self.der is not None):
                arbol_aux = self.der.separar_arbol(arbol_aux, categoria)
        return arbol_aux




#Funciones EJ N?? 23
    
    def barrido_derrotados_por(self):
        #Realiza el barrido inorden del arbol de criaturas mostrando la criatura y quien la capturo.
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.barrido_derrotados_por()
            if(self.datos['capturada']!=''):
                print (self.info, 'fue derrotada por ', self.datos['capturada'])
            if (self.der is not None):
                self.der.barrido_derrotados_por()
    
    def cargar_descripcion (self, criatura):
        """Carga una breve descripcion de la criatura si ??sta existe en el arbol."""
        pos = self.busqueda(criatura)
        if (pos):
            desc = input('Ingrese una breve descricpion de la criatura: ')
            pos.datos['descripcion'] = desc
        else:
            print('No hay ninguna criatura con ese nombre en el arbol.')

    def mostrar_informacion (self, criatura):
        pos = self.busqueda(criatura)
        if (pos):
            print(pos.info, '?? Capturada por:' ,pos.datos['capturada'], '?? Descripcion:' , pos.datos['descripcion'])
        else:
            print('No hay ninguna criatura con ese nombre.')

    def contador_criaturas_derrotadas(self, dic):
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.contador_criaturas_derrotadas(dic)
            if (self.datos['capturada'] in dic and self.datos['capturada'] != ''):
                dic[self.datos['capturada']] += 1 #el dic tiene un solo campo, el nombre del heroe, al que se le asigna un valor numericoo (Cantidad de capturas)
            elif (self.datos['capturada'] != ''):
                dic[self.datos['capturada']] = 1
            if (self.der is not None):
                self.der.contador_criaturas_derrotadas(dic)

    def criaturas_derrotadas (self, heroe):
        """Muestra las criaturas derrotadas por un heroe dado."""  
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.criaturas_derrotadas(heroe)
            if (self.datos['capturada'] == heroe):
                print (self.info)
            if (self.der is not None):
                self.der.criaturas_derrotadas(heroe)

    def criaturas_no_derrotadas (self):
        """Muestra las criaturas que no han sido derrotadas."""  
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.criaturas_no_derrotadas()
            if (self.datos['capturada'] == ''):
                print (self.info)
            if (self.der is not None):
                self.der.criaturas_no_derrotadas()

    def modificar_captura (self, criatura, heroe):
        """Modifica quien capturo a la criatura dada por el heroe dado."""
        pos = self.busqueda(criatura)
        if (pos):
            pos.datos['capturada'] = heroe
        else:
            print('No hay ninguna criatura con el nombre', criatura, 'en el arbol.')

    def busqueda_por_coincidencia(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_por_coincidencia(clave)
            if(clave in self.info):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_por_coincidencia(clave)
