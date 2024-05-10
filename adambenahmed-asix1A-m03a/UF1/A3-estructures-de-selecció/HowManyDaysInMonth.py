"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
mes = input()

if mes in ["1", "3", "5", "7", "8", "10", "12"]: print("31")
elif mes in ["4", "6", "9", "11"]: print("30")
elif mes == "2": print("28, 29")
else: print("No es un mes valido")
