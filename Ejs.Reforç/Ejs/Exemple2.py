diaAniversari = int(input("Quin dia del mes és el teu aniversari:"))
mesAniversari = int(input("Quin mes és el teu aniversari:"))
diaActual = int(input("Quin dia és avui:"))
mesActual = int(input("En quin mes estem:"))

aniversari = False
if mesAniversari <= mesActual and diaAniversari <= diaActual:
    aniversari = True
if aniversari:
    print("El teu aniversari ja ha passat.")
else:
    print("El teu aniversari encara no ha passat.")
