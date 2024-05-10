"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:

Programa que lea 5 enteros, que compruebe que el primero y segundo crean un rango y que el tercero
y cuarto crean otro rango, después comprobar si el quinto número está dentro de algún rango,
si esta dentro marcar como True, si no lo está, poner False.
"""

# Pedimos al usuario que nos de 5 números
numero1 = int(input("Dime 1 numero: "))
numero2 = int(input("Dime 1 numero: "))
numero3 = int(input("Dime 1 numero: "))
numero4 = int(input("Dime 1 numero: "))
numero5 = int(input("Dime 1 numero: "))

# Define dos rangos de numeros dado el valor de las variables
rango1 = range(numero1, numero2)
rango2 = range(numero3, numero4)

# Coge la variable numero5 e indica si el valor esta dentro de los 2 rangos
if numero5 in rango1 and numero5 in rango2:
    print(True)
else:
    print(False)
