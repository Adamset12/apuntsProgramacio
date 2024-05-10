from kernel import *
def main():
    frase_neta = procesar_input(input())
    paraules, num_paraules = contar_paraules(frase_neta)
    impressio(paraules, num_paraules)

main()