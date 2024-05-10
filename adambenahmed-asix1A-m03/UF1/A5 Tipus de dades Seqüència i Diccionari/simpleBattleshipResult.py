'''
Adam Ben Ahmed
ASIXc1A
simpleBattleshipResult
'''
try:
    dimensions = 6
    vaixells  = ("0 0", "0 1", "0 6", "1 2", "1 6", "2 6", "3 1", "3 2" ,"3 3", "3 6", "4 4", "4 5", "6 0")
    posicion = [int(x) for x in input().split()]
    if posicion[0] in range(dimensions + 1) and posicion[1] in range(dimensions + 1) and len(posicion) == 2:
        solucion = str(posicion[0]) + " " + str(posicion[1])
        if solucion in vaixells:
            print("vaixell")
        else:
            print("aigua")
    else:
        print("Fica valors vàlids.")
except:
    print("Fica valors vàlids.")