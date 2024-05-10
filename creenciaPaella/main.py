import logging

from kernel import *

def main():
    if not os.path.exists(INPUT_DIR):
        logging.error(f'Input directory {INPUT_DIR} not exists')
        return
    if not os.path.exists(OUTPUT_DIR):
        logging.error(f'Input directory {OUTPUT_DIR} not exists')
        return
    """Función principal que coordina la lectura, procesamiento y escritura de palabras"""
    words = read_from_file(FILE_IN)
    process_words(words)

if __name__ == "__main__":
    main()
