'''
Adam Ben Ahmed ASIXc1A
15/12/2023
pp2
E2/MyReplace
'''
frase = input("Introdueix una frase?\n")
perreemplaçar = input("Quin caràcter vols reemplaçar?\n")
persubstituir = input("Quin és el caràcter de substitució?\n")
operacions = 0
if frase == "": print("Fica una frase >:(")
if len(perreemplaçar) > 1 or len(persubstituir) > 1:
    print("Fica només un caràcter.")
else:
    for i in range(0, len(frase)):
        if frase[i] == perreemplaçar:
            operacions += 1
    if operacions != 0:
        for j in range(0, len(frase)):
            if frase[j] == perreemplaçar:
                print(persubstituir, end="")
            else:
                print(frase[j], end="")
    else:
        print("El caràcter a reemplaçar no existeix a la cadena introduida.")