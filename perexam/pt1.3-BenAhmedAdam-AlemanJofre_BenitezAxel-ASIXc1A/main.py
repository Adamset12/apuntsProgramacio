"""
Jofre Aleman Serra, Adam Ben Ahmed, Axel Benitez
06/05/24
Projecte: L'usuari introdueix una frase i el programa ha de randomatitzar les paraules i escriure-les randomaritzades
mantenint la lletra inicial i final en la mateixa posició, i printar la frase amb les paraules randomitzades.
"""
import crazy_words
import data_source
import log_config
import logging
import os
import datetime
# region ----- PROGRAMA PRINCIPAL -----

def barrejaparaules(nom_fitxer, directori_entrada, directori_sortida):
    resultat = [""]
    if nom_fitxer.endswith(".txt"):
        fitxer_output = os.path.join(directori_sortida, (os.path.splitext(nom_fitxer)[0] + "_boges.txt"))
        log_config.log(__file__)
        logging.debug(f"Llegint arxiu \"{nom_fitxer}\"")
        text = data_source.get_data_from_file(os.path.join(directori_entrada, nom_fitxer))
        try:
            text, frase_per_operar = crazy_words.arreglar_frase(text)
            crazy_words.recorrer_frase(frase_per_operar, resultat)
            crazy_words.pegar_resultat(text, resultat, fitxer_output)
        except TypeError:
            "Falla perquè no li arriba text perquè no s'ha pogut obrir el fitxer."

def main():
    temps_inicial = datetime.datetime.now()
    try:
        log_config.log(__file__)
        logging.info("L'aplicació ha iniciat")
        if os.path.isfile(PARAULES_TEXT):
            barrejaparaules(PARAULES_TEXT, DIRECTORI_ACTUAL, DIRECTORI_ACTUAL)
        else:
            log_config.log(__file__)
            logging.error("El fitxer \"paraules.txt\" no existeix.")
        if os.path.isdir(DIRECTORI_ENTRADA):
            if os.path.isdir(DIRECTORI_SORTIDA):
                for nom_fitxer in os.listdir(DIRECTORI_ENTRADA):
                    barrejaparaules(nom_fitxer, DIRECTORI_ENTRADA, DIRECTORI_SORTIDA)
            else:
                log_config.log(__file__)
                logging.error(f"El directori \"{DIRECTORI_SORTIDA}\" no existeix.")
        else:
            log_config.log(__file__)
            logging.error(f"El directori \"{DIRECTORI_ENTRADA}\" no existeix.")
    except FileNotFoundError:
        print("Has de crear un fitxer \"log.txt\" dins de un directori \"log\" en aquest directori")
    except:
        if os.path.isfile("log/log.txt"):
            log_config.log(__file__)
            logging.error("El procés ha fallat")
    if os.path.isfile("log/log.txt"):
        temps_final = datetime.datetime.now()
        temps_transcrregut = temps_final - temps_inicial
        log_config.log(__file__)
        logging.info(f"Programa finalitzat, Temps total d'execució: {temps_transcrregut}\n----------------------------------------------------------------------------------------------------------------------------------------------")

DIRECTORI_ENTRADA = "entrada"
DIRECTORI_SORTIDA = "sortida"
DIRECTORI_ACTUAL = os.getcwd()
PARAULES_TEXT = "paraules.txt"
main()
# endregion
