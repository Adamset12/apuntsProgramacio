qp = int(input("Nota de la mitjana de les tres qualificacions parcials:"))
pf = int(input("Nota de la prova final:"))
tf = int(input("Nota del treball final:"))

qp = int((qp * 55)/10)
pf = int((pf * 30)/10)
tf = int((tf * 15)/10)

print("La nota final és:", qp+tf+pf)