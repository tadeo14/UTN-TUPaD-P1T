#Ejercicio 2 

""" Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”."""

#Respuesta 

while True:
    nota = input ("Coloque su nota: ");

    if int(nota) >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")    
