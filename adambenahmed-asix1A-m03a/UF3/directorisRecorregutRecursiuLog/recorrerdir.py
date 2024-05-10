"""
Fet per Adam Ben Ahmed
"""
import os
import logging
import time

logging.basicConfig(
    filename='recorregut.log',
    filemode='w',
    level=logging.DEBUG,  # Set level to DEBUG to capture all levels of logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
def recorrer_arbol_directorios(directorio):
    try:
        contenido = os.listdir(directorio)
        for elemento in contenido:
            ruta_elemento = os.path.join(directorio, elemento)
            if os.path.isdir(ruta_elemento):
                logging.info("Directorio: %s", ruta_elemento)
                recorrer_arbol_directorios(ruta_elemento)
            else:
                logging.info("Archivo: %s", ruta_elemento)
    except Exception as e:
        logging.error("Error: %s", str(e))


def main():
    directorio_inicial = input("")  # Replace with your directory path
    if not os.path.isdir(directorio_inicial):
        logging.error("El directorio especificado no existe.")
    else:
        logging.info("Recorrido del árbol de directorios:")
        start_time = time.time()
        recorrer_arbol_directorios(directorio_inicial)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logging.info("Tiempo transcurrido: %s segundos", elapsed_time)