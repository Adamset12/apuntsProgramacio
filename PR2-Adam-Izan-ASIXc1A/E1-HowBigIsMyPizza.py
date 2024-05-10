"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:

Hacer un programa que calcule la superfície de una pizza.
"""

import math  # Importamos la librería math para poder aplicar PI y varios parámetros de ayuda.

diametro = int(input("Dime el diametro en centimetros: "))  # Pedimos al usuario que nos diga el diametro en entero.

radio = diametro / 2  # El Radio lo obtenemos diviendo entre dos el diametro.
superficie = math.pi * (radio ** 2)  # Calcula la superficie multiplicando PI por radio elevado al cuadrado.
superficie = round(superficie, 2)  # Redondea la superficie a dos decimales.

print(superficie)  # Mostramos por pantalla el resultado.
