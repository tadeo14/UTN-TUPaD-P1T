#EJERCICIO 9
"""
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""
#Respuesta 

for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    if i == 0:
        suma = numero
    else:
        suma += numero
        media = suma / (i + 1)
print(f"La media de los números ingresados es: {media:.2f}")
