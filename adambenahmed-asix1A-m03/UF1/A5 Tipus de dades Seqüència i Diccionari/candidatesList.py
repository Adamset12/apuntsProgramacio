quantitat = int(input())
consulta = False
toprint = []
candidat = [input() for x in range(quantitat)]
while consulta != -1:
    consulta = int(input())
    if consulta != -1:
        toprint += [consulta]
for x in toprint:
    print(candidat[x-1])