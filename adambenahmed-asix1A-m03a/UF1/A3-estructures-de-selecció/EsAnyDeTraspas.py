"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    any = int(input("Any a tractar: "))

    if any < 1582:
        any = "Data anterior a Gregori"
    elif any // 4 != any / 4:
        any = "Any comú"
    elif any // 100 != any / 100:
        any = "Any de traspàs"
    elif any // 400 != any / 400:
        any = "Any comú"
    else:
        any = "Any de traspàs"
    print(any)
except ValueError:
    print("L'any ha de ser en format numéric")
