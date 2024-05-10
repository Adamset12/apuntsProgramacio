"""
Axel Benitez Parra
Adam Benahmed
Oscar Bravo
M03 - Programacio
01/12/2023
"""
n = 8
for i in range(4):
    print(n, end=" ")
    n -= 1
    for j in range(4):
        print("██", end="")
        print("  ", end="")
    print("")
    print(n, end=" ")
    n -= 1
    for j in range(4):
        print("  ", end="")
        print("██", end="")
    print("")
print("  ", end="")
for j in range(8):
    print(chr(j + 65), end=" ")