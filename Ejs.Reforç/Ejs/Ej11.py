num_1 = int(input("Primer punt:"))
num_2 = int(input("Segon punt:"))

Distancia = num_1 - num_2
if Distancia < 0:
    Distancia = Distancia * -1
print("La distancia entre els dos punts és de:", Distancia)