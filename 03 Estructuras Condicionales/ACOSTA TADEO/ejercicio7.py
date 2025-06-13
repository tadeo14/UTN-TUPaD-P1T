#EJERCICIO 7

"""
Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla. """

#RESPUESTA

while True:

    frase = input("Coloque una frase o palabra: ");

    if frase[-1].lower() in "a,e,i,o,u": #toma la ultima letra y la convierte a minuscula, luego verifica si esa letra esta en la cadena de vocales
        print (frase + "!") #si esta lo agrega, sino lo deja tal cual esta. 
    else:
        print(frase)
