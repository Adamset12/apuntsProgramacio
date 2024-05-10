"""
Jofre Aleman Serra, Adam Ben Ahmed, Axel Benitez
06/05/24
Projecte: L'usuari introdueix una frase i el programa ha de randomatitzar les paraules i escriure-les randomaritzades
mantenint la lletra inicial i final en la mateixa posició, i printar la frase amb les paraules randomitzades.
"""
import logging
import log_config
def get_data_from_file(file_name):
    log_config.log(__file__)
    try:
        with open(file_name, mode='rt', encoding='utf-8') as f:
            text = f.read()
            return text
        logging.debug("Arxiu llegit correctament")
    except FileNotFoundError:
        logging.error(f"No se ha encontrado el archivo {file_name}")
    except UnicodeDecodeError:
        logging.error(f"No se pudo leer el archivo {file_name}, mal encoding.")
    except PermissionError:
        logging.error(f"No se pudo leer el archivo {file_name}, permisos inadecuados.")
    except:
        logging.error(f"Error al leer el archivo {file_name} inesperado.")
