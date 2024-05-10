"""
Axel Benitez Parra
Adam Benahmed
Oscar Bravo
M03 - Programacio
04/12/2023
"""
try:
    limit = int(input("Introdueix un número límit: "))
    suma_parells = 0
    suma_senars = 0
    for num in range(limit):
        if num % 2 == 0:
            suma_parells += num
        else:
            suma_senars += num
    print("Suma dels parells: " + str(suma_parells),"\nSuma dels senars: " + str(suma_senars))
except:
    print("Posa valors vàlids.")