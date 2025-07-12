#Ejercicio 3 

""" 
Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.


""" 
#Respuesta 

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

suma = 0

for i in range(numero1+1,numero2):
    suma += i
    
print(suma)