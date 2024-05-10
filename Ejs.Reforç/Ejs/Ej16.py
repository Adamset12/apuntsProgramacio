vB = int(input("Indica la velocitat del vehicle B:"))
vA = int(input("Indica la velocitat del vehicle A:"))
Distancia = int(input("Indica la distancia entre el vehicle A i B:"))

tof = 0
aux = 0
temps = 0
while tof != 1:
    temps += 0.000001
    aux = (vB - vA) * temps
    if aux == Distancia:
        tof = 1

if vB > vA:
    print("El temps necessari per a que estiguin a distancia zero és de:", str(temps))

else :
    print("No he pogut trobar la resposta, asegurat de que has ficat valors vàlids.")
