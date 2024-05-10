"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:

Forma alternativa de reemplazar las vocales por números de una palabra.
"""

word = input("Que palabra quieres codificar? ")  # Pedimos al usuario que nos diga una palabra.
word2 = "La palabra escogida es {}.".format(word)  # Guarda el input orginal y lo imprime por pantalla
print(word2)

if word != "":
    i = 0
    result = ""
    length = len(word)  # Mide la longitud del valor de la variable
    while i < length:
        if word[i] == 'a' or word[i] == 'A':  # Mira si en la palabra existen vocales y si las hay le suma un numero
            result += '1'
            i += 1
        elif word[i] == 'e' or word[i] == 'E':
            result += '2'
            i += 1
        elif word[i] == 'i' or word[i] == 'I':
            result += '3'
            i += 1
        elif word[i] == 'o' or word[i] == 'O':
            result += '4'
            i += 1
        elif word[i] == 'u' or word[i] == 'U':
            result += '5'
            i += 1
        else:
            result += chr(ord(word[i]))  # Une el result (con las vocales) con el resto de consonantes
            i += 1
    print("La palabra codificada es {}.".format(result))  # Imprime por pantalla la palabra codificada
else:
    print("Introduce una palabra!")  # Indica que si la palabra esta en blanco imprime por pantalla una advertencia
