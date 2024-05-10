'''
Adam Ben Ahmed
ASIXc1A
DniCalculator
'''
try:
    dni_letters = ("T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
                   "N", "J", "Z", "S", "Q", "v", "H", "L", "C", "K", "E")
    dni = int(input())
    if len(str(dni)) <= 8: print(dni_letters[dni % 23])
    else: s = a - 1
except: print("Fica valors vàlids")