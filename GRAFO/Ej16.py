'''Se dispone del acervo bibliográfico de tesis de carreras de una facultad de informática. Implementar
los algoritmos necesarios para satisfacer los requerimientos que nos solicitan:
a. cada vértice tendrá el nombre de la tesis, el autor de la misma y cuatro palabras claves;
b. las aristas representan la relación entre dos tesis cuyo contenido es similar, para lo cual
consideramos como mínimo dos palabras claves en común –se deben cargar al menos tres
aristas por vértice–;
c. realizar un barrido en profundidad desde una tesis que contenga la palabra clave “programación”
o “inteligencia artificial”, considerar solamente las tesis que son accesibles desde
el inicio sin reiniciar el barrido (si quedaron sin tratar);
d. obtener el árbol de expansión máximo partiendo desde un vértice que tenga la palabra
clave “minería de datos”.
'''