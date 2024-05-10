"""
Axel Benitez Parra
Adam Benahmed
Oscar Bravo
M03 - Programacio
01/12/2023
"""
try:
    clave = int(input())
    clave2 = int(input())
    answer = 0
    for i in range(abs(clave2)):
        answer += abs(clave)
    if clave < 0 or clave2 < 0: answer = answer * -1
    print(answer)
except:
    print("Posa valors vàlids")
