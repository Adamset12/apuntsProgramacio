"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:

Programa que calcule el volumen de una aula vacía.
"""

ancho = int(input("Dime el ancho: "))  # Pedimos al usuario el ancho del aula.
altura = int(input("Dime la altura: "))  # Pedimos al usuario la altura del aula.
largo = int(input("Dime el largo: "))  # Pedimos al usuario el largo del aula.

# Para obtener el volumen de aire dentro de una habitacion deberemos multiplicar el ancho por la altura por el largo.
aire = ancho * altura * largo

print("El volum de l'aula es {} m³".format(aire))
# format() indica que la variable aire la inserte como string entre las {}
