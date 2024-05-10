'''
Adam Ben Ahmed
ASIXc1A
MathAnalizer
'''
# region FUNCIONES
def obtenir_puntuacions(validesa, aux, equips, llista_resultats):
    puntuacions = [int(x) for x in input().split()]
    if len(puntuacions) == 2:
        comparar_puntuacions(puntuacions, aux, validesa, equips, llista_resultats)
    elif puntuacions == [-1]:
        validesa[0] = "Final"
        mostrar_guanyador(aux, equips, validesa, llista_resultats)
    else:
        validesa[0] = "Invalid"
def obtenir_equips():
    equip1 = input()
    equip2 = input()
    if not equip1:
        equip1 = "local"
    if not equip2:
        equip2 = "Visitante"
    if equip1 == equip2:
        equip1 = "local"
        equip2 = "Visitante"
    return equip1, equip2
def comparar_puntuacions(puntuacio_actual, aux, validesa, equips, llista_resultats):
    comprovacio = [(puntuacio_actual[0]-aux[0]),(puntuacio_actual[1]-aux[1])]
    if comprovacio[0] == 0 and comprovacio[1] in [1, 2, 3] or comprovacio[0] in [1, 2, 3] and comprovacio[1] == 0:
        aux[0], aux[1] = puntuacio_actual[0], puntuacio_actual[1]
        mostrar_resultats(comprovacio, equips, llista_resultats)
    else:
        validesa[0] = "Invalid"
def mostrar_resultats(comprovacio, equips, llista_resultats):
    resultats = ["Tir lliure", "Cistella", "Triple"]
    if comprovacio[1] != 0:
        llista_resultats.append(f"{resultats[comprovacio[1] - 1]} de {equips[1]}")
    elif comprovacio[0] != 0:
        llista_resultats.append(f"{resultats[comprovacio[0] - 1]} de {equips[0]}")
def mostrar_guanyador(puntuacions, equips, validesa, llista_resultats):
    if puntuacions[0] > puntuacions[1]:
        for x in llista_resultats: print(x)
        print(f"L'equip guanyador és: {equips[0]}")
    elif puntuacions[1] > puntuacions[0]:
        for x in llista_resultats: print(x)
        print(f"L'equip guanyador és: {equips[1]}")
    else:
        validesa[0] = "Invalid"
#endregion
#region Programa i definicions
try:
    aux = [0, 0]
    validesa = ["Valid"]
    equips = obtenir_equips()
    llista_resultats = []
    while validesa[0] == "Valid":
        puntuacions = obtenir_puntuacions(validesa, aux, equips, llista_resultats)
    if validesa[0] == "Invalid":
        print("Assegurat de que has ficat valors vàlids.")
except:
    print("Assegurat de que has ficat valors vàlids.")
#endregion