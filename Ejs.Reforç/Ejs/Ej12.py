import math
A = (input("Coordenades del punt A separades per coma:"))
B = (input("Coordenades del punt B separades per coma:"))

distancia = math.sqrt((int(B.split(',')[0]) - int(A.split(',')[0])) **2 + (int(B.split(',')[1]) - int(A.split(',')[1])) **2)

print("La distancia entre els punts és de : " + str(round(distancia, 2)) + " unitats")
