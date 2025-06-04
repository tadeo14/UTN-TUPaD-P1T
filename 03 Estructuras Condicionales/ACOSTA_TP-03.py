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
como una lista o un string. 

#Respuesta 
# Solicita al usuario que ingrese una contraseña
contraseña = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verifica la longitud de la contraseña utilizando len()
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



#Ejercicio 6

import random
from statistics import mode, median, mean

# Crear una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la media, la mediana y la moda
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Imprimir los valores
print(f"Números aleatorios: {numeros_aleatorios}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

# Determinar el sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo a la derecha.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo a la izquierda.")
else:
    print("Sin sesgo.")

"""

#Ejercicio 7


#Ejercicio 8

#Ejercicio 9 

#Ejercicio 10