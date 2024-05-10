"""
Adam Ben Ahmed Belachi
06/10/2023
MO3 UF1 A2
El programa diu la quantitat de diners que en tenim."
"""

dos = (int(input("Quantitat de monedes de dos euros:")) * 2)
un = int(input("Quantitat de monedes d'un euro:"))
cinquanta = (int(input("Quantitat de monedes de cinquanta cèntims:")) * 0.5)
vint = (int(input("Quantitat de monedes de vint cèntims:")) * 0.2)
deu = (int(input("Quantitat de monedes de deu cèntims:")) * 0.1)
cinc = (int(input("Quantitat de monedes de cinc cèntims:")) * 0.05)
print(f"Tens: {(dos + un + cinquanta + vint + deu + cinc):.2f} euros")
