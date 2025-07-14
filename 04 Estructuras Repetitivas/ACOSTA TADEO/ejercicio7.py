#EJERCICIO 7

"""
Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
 """

#RESPUESTA

numero = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(0, numero + 1):
    suma += i
    
print(f"La suma de todos los números comprendidos entre 0 y {numero} es: {suma}")