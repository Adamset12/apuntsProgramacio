"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:

Ejercicio opcional -- Programa para hacer un print de un literal.
"""

"""
Esto es un código de escape ANSI que indica el inicio de una secuencia de formato.
- '0;32' se refiere al estilo de formato, donde 0 significa estilo normal y 32 es el código de color para verde.
- '?' se refiere al literal que queremos cambiar de color.
- '-033[m' otro código de escape ANSI que indica el final de la secuencia de formato. 
"""
print('\033[0;32m?\033[m')