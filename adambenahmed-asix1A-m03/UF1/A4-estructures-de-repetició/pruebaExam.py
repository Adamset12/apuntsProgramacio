coords = input().split()
pieza = "*"
cord_x = int(coords[0]) - 1
cord_y = int(coords[1]) - 1
for y in range(0,8):
    if y//2 == y/2:
        aux1 = "B"
        aux2 = "N"
    else:
        aux1 = "N"
        aux2 = "B"
    for x in range(0,8):
        if (x == cord_x or y == cord_y) and x == 7:
            print(pieza)
        elif x == cord_x or y == cord_y:
            print(pieza, end=" ")
        elif x == 7:
            print(aux2)
        elif x//2 == x/2:
            print(aux1, end=" ")
        else:
            print(aux2, end=" ")









'''        if x//2 == x/2:
            casilla = "B"
        else:
            casilla = "N"
        if x != 8:
            print(casilla, end=" ")
        else:
            print()'''