integers = [3, 6, 9, 12, 4, 1]
#La variable integers crea la lista con los numeros que estan en ella
target = 15
#La variable target crea el objetivo 15

def find_target(integers, target):
    #Esta linea de codigo crea la funcion "find_target" teniendo en cuenta la lista "integers" y el objetivo "trigger"
    for i in range (len(integers)):
        #Esta crea el bucle "for" que tiene en cuenta el tamaño de la lista, es decir sus caracteres
        for j in range (i + 1, len(integers)):
            #esta linea crea el bucle "for" y recorre los elementos de la lista despues del elemento en el que se ubico, es decir que 
            #la primera vez lo recorre desde el 3 de la lista "integers"
            if integers[i] + integers[j] == target:
                #Este if revisa si el numero que esta ubicado el bucle "i" mas el numero que esta ubicado el bucle "j" es igual al 
                #objetivo "target"
                return (integers[i], integers[j])
                #retorna los dos numeros que hacen la suma del objetivo que estan ubicados en la lista
    return None
    #si alguno de los dos numeros no se encuentra retornara none

num1, num2 = find_target(integers, target)
#crea las variables "num1" y "num2" como la funcion con la lista "integers" y el objetivo "target"
if num1 is not None and num2 is not None:
#si el "num1" no es nulo y el "num2" tampoco es nulo reproduce la siguiente funcion
    print("Los números que suman ",target,"son: ",num1,"y",num2)
    #imprime la solucion
else:
    print("No se encontraron números que sumen el objetivo.")
    #imprime lo que esta dentro del print si no se encontraron los numeros