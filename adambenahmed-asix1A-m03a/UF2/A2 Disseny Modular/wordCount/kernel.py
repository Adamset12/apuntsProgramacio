import re
def procesar_input(frase):
    frase_neta = re.split("[^a-zA-Z0-9ñÑ']", frase)
    frase_neta = [paraula.lower() for paraula in frase_neta if paraula]
    #frase_neta_2 = []
    return (frase_neta)
def contar_paraules(frase_neta):
    paraules = []
    num_paraules = []
    for paraula in frase_neta:
        aux = paraula
        if aux[0] == "'":
            aux = aux[1:]
        if aux[-1] == "'":
            aux = aux[:-1]
        if aux not in paraules:
            paraules.append(aux)
            num_paraules.append(1)
        else:
            num_paraules[paraules.index(aux)] = num_paraules[paraules.index(aux)] + 1
    return paraules, num_paraules
def impressio(paraules, num_paraules):
    for x in range(len(paraules)):
       print(f"{paraules[x]}: {num_paraules[x]}")
