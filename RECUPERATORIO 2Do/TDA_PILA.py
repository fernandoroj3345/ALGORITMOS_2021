class Pila(object):
    
    def __init__(self):#init convierte en libreria para poder inportar.
        '''Crea Una Pila Vacia'''
        self.__elementos = []
        self.__nombre = ''

    def apilar(self, dato):#self atributo padre para  no dejar vacia la funcion
        """Apila el dato sobre la cima de la pila."""   
        self.__elementos.append(dato)#Agrego un elemento al array(pila) en el tope de la pila

    def desapilar(self):
        '''desapila el elemento de la cima y lo devuelve'''
        return self.__elementos.pop()#pop elimina el elemento que esta en la cima.
    
    def pila_vacia(self):#Retorna un verdadero o falso
        """Devuelve True si la pila esta vacía.""" 
        return len(self.__elementos) == 0 #len si el tamañao de la pila es = 0 retorna true

    def tamanio(self):#tamanio retorna el tamaño de la pila.
        """Devuelve el número de elementos en la pila."""
        return len(self.__elementos)

    def elemento_cima(self):#elemento cima, retorna el elemento en la cima de la pila el 1ro.
         """Devuelve el valor almacenado en la cima de la pila."""
         return (self.__elementos)[-1]#si fuera 0 seria el elemento del fondo por eso es -1

      
    def barrido_pila(self): # realiza un barrido de la pila y la reconstruye
        paux = Pila()
        while (not self.pila_vacia()):
            dato = self.desapilar()
            print(dato)
            paux.apilar(dato)

        while (not paux.pila_vacia()):
            dato = paux.desapilar()
            self.apilar(dato)
