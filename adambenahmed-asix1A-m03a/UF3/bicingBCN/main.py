import pandas
FITXER = "2023_03_Marc_BicingNou_INFORMACIO.csv"
resultat = pandas.read_csv(FITXER)
max_valor = list(resultat["capacity"]).index(54)
min_valor = list(resultat["capacity"]).index(0)
print(resultat["name"][min_valor], resultat["capacity"][min_valor])
print(sum(resultat["capacity"][0:520]))
#, resultat["capacity"].index(max_valor)