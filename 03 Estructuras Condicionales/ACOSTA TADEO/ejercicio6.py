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

