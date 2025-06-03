#Ejercicio 1 
"""Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Respuesta 

edad = input("Coloque su edad: "): #Se le pide al usuario que coloque su edad

#Creo el condicional para que analice la entrada del usuario. 
if int(edad) >= 18:
    print("Es mayor")
else: 
    print("Es menor")

"""
#Ejercicio 2 

""" Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.

#Respuesta 

while True:
    nota = input ("Coloque su nota: "):

    if int(nota) >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")    
"""

#Ejercicio 3 

""" 
Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar

#Respuesta 

while True:

    num_par= input ("Coloque un numero par: ")

    if int(num_par) % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
        """ 

#Ejercicio 4


"""Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.

#Respuesta 

while True:

    edad = int(input ("Coloque su edad: ")) 

    if edad < 12:
        print ("Niño/a: menor de 12 años.")
    elif   12 <= edad < 18:
        print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
    elif 18 <= edad <30:
        print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
    else: 
        print("Adulto/a: mayor o igual que 30 años.")

"""

#Ejercicio 5

""" Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string. """

#Respuesta 




#Ejercicio 6


#Ejercicio 7


#Ejercicio 8

#Ejercicio 9 

#Ejercicio 10