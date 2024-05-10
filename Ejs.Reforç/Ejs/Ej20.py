dos = int(input("Quantitat de monedes de dos euros:"))
un = int(input("Quantitat de monedes d'un euro:"))
cinquanta = int(input("Quantitat de monedes de cinquanta cèntims:"))
vint = int(input("Quantitat de monedes de vint cèntims:"))
deu = int(input("Quantitat de monedes de deu cèntims:"))

dos *= 2
cinquanta *= 0.5
vint *= 0.2
deu *= 0.1

diners = dos + un + cinquanta + vint + deu
euros = int(diners)
centims = round((diners - diners) * 100)

print("Son " + str(euros) + " euros i " + str(centims) + " cèntims.")