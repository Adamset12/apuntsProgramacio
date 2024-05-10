import requests
# region Funcions
def verificar_lletra(lletra, paraula):

# endregion
# region Preparació
paraula = requests.get("https://clientes.api.greenborn.com.ar/public-random-word").text.split("\"")[1]
len_paraula = len(paraula)
solucio = ["_"] * len_paraula
end = False
print(solucio)
# endregion
while not end:
    jugada = input("Fica una lletra o intenta endevinar la paraula!")
    if len(jugada) != 1 or len(jugada) != len_paraula or not jugada.isalpha():
        print("Input invàlid, fica un altre")
    elif jugada == paraula:
        #Ben jugat
        end = True
    else:
        verificar_lletra(jugada, paraula)