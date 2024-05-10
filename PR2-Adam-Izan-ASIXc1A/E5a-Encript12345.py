"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:
Programa que reemplace las letras vocales de una palabra por orden del 1 al 5.
"""

word = input("Dime una palabra para codificar: ")  # Pedimos al usuario que nos diga una palabra.

# Remplaza las vocales de una palabra por numeros del 1 al 5 independientemente si son mayusculas o minusculas
word = word.replace('a', '1')
word = word.replace('e', '2')
word = word.replace('i', '3')
word = word.replace('o', '4')
word = word.replace('u', '5')
word = word.replace('A', '1')
word = word.replace('E', '2')
word = word.replace('I', '3')
word = word.replace('O', '4')
word = word.replace('U', '5')

print("La palabra codificada es {}.".format(word))
# format() indica que la variable word la inserte como string entre las {}
