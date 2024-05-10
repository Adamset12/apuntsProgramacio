"""
Axel Benitez Parra
Adam Benahmed
Oscar Bravo
M03 - Programacio
01/12/2023
"""
try:
    numero = input().split()
    longitud = len(numero)
    contador_0 = 0
    contador_p = 0
    contador_n = 0
    contador_a = 0
    if longitud == 10:
        while longitud != 0:

            if int(numero[contador_a]) == 0:
                contador_0 += 1
            elif int(numero[contador_a]) > 0:
                contador_p += 1
            elif int(numero[contador_a]) < 0:
                contador_n += 1
            contador_a += 1
            longitud -= 1
        print("Zeros: " + str(contador_0) + "\nPositius: " + str(contador_p) + "\nNegatius: " + str(contador_n))
    else:
        print("Pon valores válidos")
except:
    print("Pon valores válidos")