import crazy_words
import data_source
import log_config
import logging
import os
import time
# region ----- PROGRAMA PRINCIPAL -----
FITXER = "paraules.txt"
FITXER_OUTPUT = "paraules_boges.txt"

def main():
    log_config.log(__file__)
    logging.info("L'aplicació ha iniciat")
    try:
        resultat = [""]
        log_config.log(__file__)
        logging.debug("Llegint arxiu")
        text = data_source.get_data_from_file(FITXER)
        text, frase_per_operar = crazy_words.arreglar_frase(text)
        crazy_words.recorrer_frase(frase_per_operar, resultat)
        crazy_words.pegar_resultat(text, resultat, FITXER_OUTPUT)
    except FileNotFoundError:
        print("Has de crear un fitxer \"log.txt\" dins de un directori \"log\" en aquest directori")
    except:
        log_config.log(__file__)
        logging.error("El procés ha fallat")
    log_config.log(__file__)
    logging.info(
        f"Finalitzat.\n----------------------------------------------------------------------------------------------------------------------------------------------")

main()
# endregion
