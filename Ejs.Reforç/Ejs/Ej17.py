Temps = int(input("Quin és el temps que triga el ciclista en arribar a la ciutat B (en segons):"))
Hora = int(input("A quina hora parteix:"))
Minuts = int(input("Amb quants minuts:"))
Segons = int(input("Amb quants segons:"))

horatotal = Hora * 3600 + Minuts * 60 + Segons + Temps

if horatotal >= 86400:
    horatotal -= 86400
Hora = int(horatotal // 3600)
Minuts = int((horatotal - Hora * 3600) // 60)
Segons = int(horatotal - Hora * 3600 - Minuts * 60)

if Hora > 0:
    print(Hora, "h ", end='')
else:
    print("0 h ", end='')
if Minuts > 0:
    print(Minuts, "min ", end='')
else:
    print("0 min ", end='')
if Segons > 0:
    print(Segons, "s ", end='')
else:
    print("0 s ", end='')

