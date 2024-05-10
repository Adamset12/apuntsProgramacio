import json
districtes_amb_platja = []
pltj_cv = 0
with open("opendatabcn_NP-NASIA_Platges-js.json", "rt") as f:
    datos = json.load(f)
    for platja in datos:
        districte = platja['addresses'][0]['district_name']
        if districte == "Ciutat Vella":
            pltj_cv += 1
        if districte not in districtes_amb_platja:
            districtes_amb_platja.append(districte)
solucio = districtes_amb_platja[0]
solucio += ", " + districtes_amb_platja[1]
print(solucio)
print(pltj_cv)