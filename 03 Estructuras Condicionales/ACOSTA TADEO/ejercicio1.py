#Ejercicio 1 
"""Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

#Respuesta 

edad = input("Coloque su edad: ") #Se le pide al usuario que coloque su edad

#Creo el condicional para que analice la entrada del usuario. 
if int(edad) >= 18:
    print("Es mayor")
else: 
    print("Es menor")
