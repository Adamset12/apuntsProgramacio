'''
Adam Ben Ahmed ASIXc1A
15/12/2023
pp2
E3/MatrixDiagonals
'''
for y in range(0, 8):
    for x in range(0, 8):
        if x == y:print(end="1")
        elif x + y == 7: print(end="2")
        else: print(end="0")
        if x == 7: print(end="\n")
        else: print(end=" ")