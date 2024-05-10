import crazy_words
import data_source
# region ----- PROGRAMA PRINCIPAL -----
def main():
    CYAN = "\033[36m"
    RESET = "\033[0m"
    resultat = [""]
    exec = True
    while exec:
        print(CYAN+"MENÚ:\n     1. Introduir text per pantalla\n     2. Introduir URL\n     3. Fer pregunta a ChatGPT\n "
                   "    4. EN PROCÉS\n     5. SORTIR"+RESET)
        eleccio = input()
        resultat = [""]
        match eleccio:
            case "1": frase = data_source.get_data__from_keyboard()
            case "2":
                    frase = data_source.get_data_from_server(input())
                    #https://clientes.api.greenborn.com.ar/public-random-word
            case "3":
                    frase = data_source.get_data_from_chatGPT(input())
            case "4": print("Tranquilo gormiti, pronto se prende heavy.")
            case "5":
                    exec = False
                    print("Dew")
            case _: print("Fica un numero valid.\nDato: Sabias que los profes (Javi) no viven en el cole? raro vrd?")
        if eleccio in ["1", "2", "3"]:
            frase, frase_per_operar = crazy_words.arreglar_frase(frase)
            crazy_words.recorrer_frase(frase_per_operar, resultat)
            crazy_words.imprimir_resultat(frase, resultat)
main()
# endregion