"""
Jofre Aleman Serra, Adam Ben Ahmed, Axel Benitez
23/02/24
Projecte: L'usuari introdueix una frase i el programa ha de randomatitzar les paraules i escriure-les randomaritzades
mantenint la lletra inicial i final en la mateixa posició, i printar la frase amb les paraules randomitzades.
"""
# region ----- IMPORTS -----
import re
from random import sample
# endregion
# region ----- DEFINICIO FUNCIONS -----
import data_source
def arreglar_frase(frase):
    frase_on_operar = re.split("[^a-zA-ZàáÀÁèÈéÉíìÌÍóòÒÓúùÙÚñÑ]", frase)
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
def imprimir_resultat(frase, resultat):
    count = 0
    for n in range(len(frase)):
        if not frase[n].isalpha():
            print(end=frase[n])
        else:
            print(end=resultat[0][count])
            count += 1
    print()
# endregion
