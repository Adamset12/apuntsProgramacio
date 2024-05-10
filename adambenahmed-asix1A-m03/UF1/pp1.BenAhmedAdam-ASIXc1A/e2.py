"""
Adam Ben Ahmed Belachi
20/10/2023
MO3 UF1 pp1
ej2
"""
Pp1 = float(input("Quina nota ha tingut a la Pp1?"))
Pr1_2 = float(input("Quina nota ha tingut a la Pr1.2?"))
Pt1_1 = float(input("Quina nota ha tingut a la Pt1.1?"))
#recullo les dades
#no es posible nombrar a les variables amb el punt numero llavors opto pel guió baix
print(f"La nota final queda en: {round((Pp1*0.7 + Pr1_2*0.15 + Pt1_1*0.15), 2):.2f}")
#imprimeixo la nota final "QUF2"