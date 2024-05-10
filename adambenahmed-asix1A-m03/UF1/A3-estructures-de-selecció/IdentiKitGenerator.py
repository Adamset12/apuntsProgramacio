"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
cabells = input()
ulls = input()
nas = input()
boca = input()
dibuix = ""
valid = True
match cabells.lower():
    case "arrissats": dibuix += "@@@@@\n"
    case "llisos": dibuix += "VVVVV\n"
    case "pentinats": dibuix += "XXXXX\n"
    case _: valid = False
match ulls.lower():
    case "aclucats": dibuix += ".-.-.\n"
    case "rodons": dibuix += ".o-o.\n"
    case "estrellats": dibuix += ".*-*.\n"
    case _: valid = False
match nas.lower():
    case "aixafat": dibuix += "..0..\n"
    case "arromangat": dibuix += "..C..\n"
    case "agilenc": dibuix += "..V..\n"
    case _: valid = False
match boca.lower():
    case "normal": dibuix += ".===."
    case "bigoti": dibuix += ".∼∼∼."
    case "dents-sortides": dibuix += ".www."
    case _: valid = False
if valid: print(dibuix)
else: print("No dibuixable :-)")

