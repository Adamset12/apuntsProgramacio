correcte = int(input("Quantes respostes correctes tens:"))
incorrecte = int(input("Queantes respostes incorrectes tens:"))
blanc = int(input("Quantes preguntes has deixat en blanc:"))

correcte = correcte * 5
nota = 0
if incorrecte <= correcte:
    nota = correcte - incorrecte

print("La teva nota és de:", nota)