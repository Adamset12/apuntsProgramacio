"""
Axel Benitez Parra
Adam Benahmed
Oscar Bravo
M03 - Programacio
04/12/2023
"""
try:
    alçada = int(input("Alçada del triangle: "))

    if 2 <= alçada <= 9:
        print(1)
        for i in range(2, alçada + 1):
            cantidad = ((2 * (i)))
            espacios = " " * (((2 * (i - 1))) - 1)
            if i != alçada:
                print(str(i) + str(espacios) + str(i))
            else:
                for j in range(1, cantidad):
                    if j % 2: print(i, end="")
                    else: print(' ', end="")
    else: print("DEL 2 AL 9")
except:
    print("LAS CAGAO BACALAO")