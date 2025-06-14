#EJERCICIO 10

while True:

    hemisferio = input("¿En qué hemisferio se encuentra? (norte/sur)")
    mes = input("¿Qué mes es? (1-12): ")
    dia = input("Que dia es? ")


    if hemisferio.lower() == "norte":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            print ("Invierno")

        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            print ("Primera")

        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            print ("Verano")
        
        elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
            print ("Otoño")
    elif hemisferio.lower() == "sur":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 2) or (mes == 3 and dia <= 20):
            print("Verano")
        elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <= 20):
            print("Otoño")
        elif (mes == 6 and dia >= 21) or (7 <= mes <= 8) or (mes == 9 and dia <= 20):
            print ("Invierno")
        elif (mes == 9 and dia >= 21) or (10 <= mes <= 11) or (mes == 12 and dia <= 20):
            print ("Primavera")
    else: 
        print("Hemisferio no valido")


