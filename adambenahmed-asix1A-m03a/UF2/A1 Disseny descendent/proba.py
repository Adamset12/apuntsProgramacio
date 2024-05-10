import re
from random import sample
def pedir_frase():
    frase = input()
    frase_on_operar = re.split("[^a-zA-ZàáÀÁèÈéÉíìÌÍóòÒÓúùÙÚ]", frase)
    frase_on_operar = [item for item in frase_on_operar if item]
    return frase, frase_on_operar
def recorrer_frase(frase, resultat):
    for i in frase:
        if len(i) > 2:
            ordenar_frase(i, randomitzar_frase(list(i[1:-1])), resultat)
        else:
            resultat[0] += i
def randomitzar_frase(frase):
    return sample(frase, len(frase))
def ordenar_frase(frase, frase_rndm, resultat):
    for i in range(len(frase)):
        if i != 0 and i != len(frase) -1:
            resultat[0] += frase_rndm[i-1]
        else:
            resultat[0] += frase[i]
count = 0
resultat = [""]
frase, frase_per_operar = pedir_frase()
recorrer_frase(frase_per_operar, resultat)

for n in range(len(frase)):
    if not frase[n].isalpha(): print(end=frase[n])
    else:
        print(end=resultat[0][count])
        count += 1