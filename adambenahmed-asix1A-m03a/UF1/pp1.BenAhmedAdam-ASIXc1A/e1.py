"""
Adam Ben Ahmed Belachi
20/10/2023
MO3 UF1 pp1
ej1
"""
import math
#import math per utilitzar arrels quadrades
Altura = float(input("Quina és l'altura del triangle quadrangular?"))
Long_Costat = float(input("Quina és la longitud dels costats del triangle quadrangular?"))
#recullo les dades
print("L'Àrea el triangle és de: " + str(round((Long_Costat * (Long_Costat + math.sqrt(4*Altura **2 + Long_Costat **2))), 2)) + " unitats") math.
print("El Volum del triangle és de: " + str(round(((Long_Costat**2 * Altura)/3), 2)) + " unitats")
#imprimeixo per pantalla els resultats en unitats generals perquè no s'ha especificat cap a l'enunciat