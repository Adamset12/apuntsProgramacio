'''
Adam Ben Ahmed
ASIXc1A
Palindrom
'''
accents = ('á', 'é', 'í', 'ó', 'ú')
vocals = ('a', 'e', 'i', 'o', 'u')
paraula = "".join([str(x) for x in input().split()])
for x in paraula:
    if x in accents:
        paraula.replace(x, vocals[accents.index(x)])
aux = 0
palindrom = "És un palindrom"
while aux != len(paraula):
    if paraula[aux].upper() != paraula[len(paraula)-1-aux].upper():
        palindrom = "No és un palindrom"
    aux += 1
print(palindrom)