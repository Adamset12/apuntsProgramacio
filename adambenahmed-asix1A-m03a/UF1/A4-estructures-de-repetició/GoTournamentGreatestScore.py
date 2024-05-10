end = False
nom_aux = input()
if nom_aux.upper() == "END": end = True
puntuació = 0
valid = False
while not end:
    valid = True
    puntuació_aux = int(input())
    if puntuació_aux > puntuació:
        puntuació = puntuació_aux
        nom = nom_aux
    nom_aux = input()
    if nom_aux.upper() == "END": end = True
if valid:
    print(nom + ":", puntuació)
