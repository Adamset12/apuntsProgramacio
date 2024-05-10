"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    nota = round(float(input()), 1)
    resultat = ""
    if nota <= 10 and nota >= 0:
        if nota < 5: resultat = "Suspès"
        if nota >= 5: resutat = "Suficient"
        if nota >= 6: resultat = "Bé"
        if nota >= 7: resultat = "Notable"
        if nota >= 9: resultat = "Excel·lent"
    print(resultat)
except ValueError or IndexError: print("Fica valors vàlids")