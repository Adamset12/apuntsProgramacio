import pandas
resultat = pandas.read_csv("username.csv", sep = ';')
print(list(resultat[" Identifier"]).index(4081))