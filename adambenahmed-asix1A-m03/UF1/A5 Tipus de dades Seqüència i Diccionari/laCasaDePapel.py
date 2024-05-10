'''
Adam Ben Ahmed
ASIXc1A
laCasaDePapel
'''
try:
    i, aux, list_aux = 0, [int(x) for x in input().split()], [0]*11
    while aux[i] in range(len(list_aux)):
            list_aux[aux[i]] += 1
            i += 1
    if aux[i] == -1: print(list_aux)
    else: print("Fica valors vàlids.")
except: print("Fica valors vàlids.")