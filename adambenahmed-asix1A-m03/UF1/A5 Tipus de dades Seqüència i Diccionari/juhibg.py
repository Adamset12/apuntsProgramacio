'''
Adam Ben Ahmed ASIXc1A
02/02/2023
Pp3
E3
'''
MIDA = 333
llista_paraules = ['']*MIDA
tupla = list(())
mitjana = 0
print(llista_paraules)
paraula = input()
contador = 0
while paraula != '\q':
    llista_paraules[contador] = paraula
    contador += 1
    paraula = input()
print(llista_paraules)
contador = 0
while llista_paraules[contador] != '':
    mitjana += len(llista_paraules[contador])
    contador += 1
mitjana = mitjana/(contador+1)
print("Mitjana de les paraules: ", mitjana)
contador = 0
while llista_paraules[contador] != '':
    if len(llista_paraules[contador]) < mitjana:
        tupla.append(llista_paraules[contador]+", mida: "+ str(len(llista_paraules[contador])))
    contador += 1
tupla = tuple(tupla)
print("La tupla queda aixi: ", tupla)