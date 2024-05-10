"""
Jofre Aleman Serra, Adam Ben Ahmed, Axel Benitez
23/02/24
Projecte: L'usuari introdueix una frase i el programa ha de randomatitzar les paraules i escriure-les randomaritzades
mantenint la lletra inicial i final en la mateixa posició, i printar la frase amb les paraules randomitzades.
"""
# region ----- IMPORTS -----
import re
from random import sample
import logging
import log_config
# endregion
# region ----- DEFINICIO FUNCIONS -----

def arreglar_frase(frase):
    result = []
    current_word = ""
    for char in frase:
        if char.isalpha():
            current_word += char
        elif current_word:
            result.append(current_word)
            current_word = ""
    if current_word:
        result.append(current_word)
    return frase, result

def recorrer_frase(frase, resultat):
    for i in frase:
        if len(i) > 2:
            ordenar_frase(i, randomitzar_frase(list(i[1:-1])), resultat)
        else:
            resultat[0] += i
def randomitzar_frase(frase):
    frase = sample(frase, len(frase))
    return frase
def ordenar_frase(frase, frase_rndm, resultat):
    for i in range(len(frase)):
        if i != 0 and i != len(frase) -1:
            resultat[0] += frase_rndm[i-1]
        else:
            resultat[0] += frase[i]
def pegar_resultat(frase, resultat, fitxer):
    resultat.append("")
    count = 0
    for n in range(len(frase)):
        if not frase[n].isalpha():
            resultat[1] += frase[n]
        else:
            resultat[1] += resultat[0][count]
            count += 1
    resultat[1] += "\n"
    with open(fitxer, "wt", encoding="utf-8") as f:
        f.write(resultat[1])
    log_config.log(__file__)
    logging.debug("Arxiu escrit correctament")
# endregion
