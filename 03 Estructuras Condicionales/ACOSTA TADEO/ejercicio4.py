#Ejercicio 4


"""Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""

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


