#Ejercicio 5

""" Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

#Respuesta 

import random
numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    
    if intento < numero_aleatorio:
        print("Demasiado bajo, intenta de nuevo.")
    elif intento > numero_aleatorio:
        print("Demasiado alto, intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
        break