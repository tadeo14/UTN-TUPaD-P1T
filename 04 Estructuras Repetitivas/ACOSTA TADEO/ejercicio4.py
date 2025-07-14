#Ejercicio 4

"""Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""

#Respuesta 


numero1 = int(input("Ingrese el primer número: "))


suma = 0

while numero1 != 0:
    suma += numero1
    print(f"Suma acumulada: {suma}")
    numero1 = int(input("Ingrese un número (0 para terminar): "))