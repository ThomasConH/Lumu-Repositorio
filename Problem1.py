array1 = [4, 2, 9, 1, 7]
sorted_array = sorted(array1)
#print(sorted_array)


#La lista "array1" toma la lista con los numeros 4, 2, 9, 1 y 7, la variable "sorted_array" es la que utiliza la funcion "sorted" 
#teniendo en cuenta lista de "array1",  luego se eso se imprime con la funcion print y imrime la variable "sorted_array"


def array_numbers(array1):
    tamaño = len(array1)
    for i in range (tamaño - 1):
        for j in range (tamaño - 1 - i):
            if array1[j] > array1 [j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
array_numbers(array1)
print(array1)

#La funcion "array_numbers" es la que contiene la lista "array1", luego de eso con la variable "tamaño" que contiene el numero de
#de valores que tiene la lista "array1" esto con el fin de tener en cuenta sus posiciones para intercambiarlas
#luego de eso se crea el bucle "for" con la variable "i" con rango del tamaño y que entienda el ultimo valor
#luego se crea otro bucle "for" con la variable "j" es el que mide si se realizan mas pasadas del bucle "i" y hace que se excluyan
#los ultimos de la lista
#por ultimo, los numeros se intercambian utilizando cambiando de lugares de array1[j], array1[j + 1] = array1[j + 1], array1[j]

