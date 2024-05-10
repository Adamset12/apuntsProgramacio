"""
09/05/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF3 pp1
Descripció: get data
"""

import os
from logger import *

inputFIle = os.path.join('.', 'paraules.txt')
allWords = []

def get_data_from_file():
    if os.path.exists(inputFIle):
        with open(inputFIle, 'r', encoding="utf-8") as file:
            text = file.read().split()
    else:
        print(f'File "{inputFIle}" not found.')
        logger('error', f'File {inputFIle} not found.')
        exit(1)
    logger('info', 'Succesfully loaded the data.')
    return text
