string = ("LUMU")
#La variable string es la que recibe la cadena, en este caso "LUMU"


def recursiveReverseString(string):
    #Esta es la linea que hace la creacion de la funcion teniendo en cuenta la variable "String"
    inverted_string = string[::-1]
    #La funcion inverted_string hace que tome en cuenta el string con el posicionamiento "::-1" desde el ultimo caracter
    #y lo imprime en orden contrario
    print(inverted_string)
    #esta funcion lo que hace es imprimir la anterior variable "inverted string"

recursiveReverseString(string)
#invoca la funcion teniendo en cuenta el string






