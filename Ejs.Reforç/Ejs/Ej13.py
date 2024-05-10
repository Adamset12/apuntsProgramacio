import math
numero = int(input("Introdueix un numero:"))

a_quadrada = math.sqrt(numero)
aux1 = 0.00001
aux2 = 0
while aux1 < numero and aux2 == 0:
    if int(aux1*aux1*aux1) == numero:
        aux2 = 1
    aux1 += 0.00001

print("L'arrel quadrada és: " + str(float(a_quadrada)) + "\nL'arrel cúbica és:" + str(float(aux1)))