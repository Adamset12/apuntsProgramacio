import crazy_words
import data_source
import log_config
import logging
import os
import time
# region ----- PROGRAMA PRINCIPAL -----
def main():
    log_config.log(__file__)
    logging.info("L'aplicació ha iniciat")
    try:
        if os.path.isdir("entrada"):
            for nom_fitxer in os.listdir("entrada"):
                resultat = [""]
                if nom_fitxer.endswith(".txt"):
                    fitxer_output = os.path.join("sortida", (os.path.splitext(nom_fitxer)[0] + "_boges.txt"))
                    log_config.log(__file__)
                    logging.debug(f"Llegint arxiu \"{nom_fitxer}\"")
                    text = data_source.get_data_from_file(os.path.join("entrada", nom_fitxer))
                    try:
                        text, frase_per_operar = crazy_words.arreglar_frase(text)
                        crazy_words.recorrer_frase(frase_per_operar, resultat)
                        crazy_words.pegar_resultat(text, resultat, fitxer_output)
                    except TypeError:
                        "Falla perquè no li arriba text perquè no s'ha pogut obrir el fitxer."
        else:
            log_config.log(__file__)
            logging.error("El directori \"entrada\" no existeix.")
    except FileNotFoundError:
        print("Has de crear un fitxer \"log.txt\" dins de un directori \"log\" en aquest directori")
    except:
        log_config.log(__file__)
        logging.error("El procés ha fallat")
    log_config.log(__file__)
    logging.info(f"Finalitzat.\n----------------------------------------------------------------------------------------------------------------------------------------------")
main()
# endregion
