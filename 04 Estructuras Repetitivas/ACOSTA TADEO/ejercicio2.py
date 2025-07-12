#Ejercicio 2 

""" Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

#Respuesta 
numero = int(input("Ingrese un número entero: "))

print(f"El numero {numero} tiene {len(str(abs(numero)))} dígitos.")

