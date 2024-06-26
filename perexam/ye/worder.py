"""
09/05/2024
Ayman Dghoughi Nouri
ASIXcB
M03 UF3 pp1
Descripció: len detector
"""

from data_source import *
from logger import *

def word_leght_2(text):
    try:
        file = os.path.join('.', 'paraules-2.txt')
        with open(file, 'wt', encoding="utf-8") as file:
            for i in text:
                lenght = len(i)
                if lenght == 2:
                    file.write(i + "\n")

    except Exception as e:
        logger('error', e)
    logger('info', f'Results saved to: {file}')


def word_leght_4(text):
    try:
        file = os.path.join('.', 'paraules-4.txt')
        with open(file, 'wt', encoding="utf-8") as file:
            for i in text:
                lenght = len(i)
                if lenght == 4:
                    file.write(i + "\n")

    except Exception as e:
        logger('error', e)
    logger('info', f'Results saved to: {file}')

def word_leght_6(text):
    try:
        file = os.path.join('.', 'paraules-6.txt')
        with open(file, 'wt', encoding="utf-8") as file:
            for i in text:
                lenght = len(i)
                if lenght == 6:
                    file.write(i + "\n")

    except Exception as e:
        logger('error', e)
    logger('info', f'Results saved to: {file}')


def word_leght_8(text):
    try:
        file = os.path.join('.', 'paraules-8.txt')
        with open(file, 'wt', encoding="utf-8") as file:
            for i in text:
                lenght = len(i)
                if lenght == 8:
                    file.write(i + "\n")
    except Exception as e:
        logger('error', e)
    logger('info', f'Results saved to: {file}')

def word_leght_10(text):
    try:
        proba = 10
        file = os.path.join('.', f"paraules-{proba}.txt")
        with open(file, 'wt', encoding="utf-8") as file:
            for i in text:
                lenght = len(i)
                if lenght == 10:
                    file.write(i + "\n")
    except Exception as e:
        logger('error', e)
    logger('info', f'Results saved to: {file}')

