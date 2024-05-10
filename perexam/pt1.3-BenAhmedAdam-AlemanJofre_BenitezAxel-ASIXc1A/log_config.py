"""
Jofre Aleman Serra, Adam Ben Ahmed, Axel Benitez
06/05/24
Projecte: L'usuari introdueix una frase i el programa ha de randomatitzar les paraules i escriure-les randomaritzades
mantenint la lletra inicial i final en la mateixa posició, i printar la frase amb les paraules randomitzades.
"""
import logging
import os
def log(filename):
    logFile = os.path.join('log', 'log.txt')
    logFormat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logLevel = logging.DEBUG
    logMode = 'a'
    date_format = '%Y-%m-%d %H:%M:%S'
    logging.getLogger().name = (filename.split(os.sep)[-1]).split('.')[0]
    logging.basicConfig(level=logLevel, format=logFormat, filename=logFile, filemode=logMode, datefmt=date_format)