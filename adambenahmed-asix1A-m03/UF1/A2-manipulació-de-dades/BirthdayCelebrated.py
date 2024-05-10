"""
Adam Ben Ahmed Belachi
02/10/2023
MO3 UF1 A2
El programa diu si ja ha passat el teu aniversari"
"""


diaAniversari = int(input("Quin dia del mes és el teu aniversari:"))
mesAniversari = int(input("Quin mes és el teu aniversari:"))
diaActual = int(input("Quin dia és avui:"))
mesActual = int(input("En quin mes estem:"))

aniversari = False
if mesAniversari < mesActual or mesAniversari == mesActual and diaAniversari <= diaActual:
    aniversari = True
if aniversari:
    print("El teu aniversari ja ha passat.")
else:
    print("El teu aniversari encara no ha passat.")
