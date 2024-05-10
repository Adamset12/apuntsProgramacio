CAP= "....\...../ ...."
ULLS= "...╚⊙ ⊙╝..."
COS = "╚═(███)═╝"
CUA =  " ═V═ "
mida_serp = int(input())
if mida_serp >= 5:
    print(CAP, "\n ", ULLS, "\n", end = "")
    i = 0
    zigzag = 3
    while i != mida_serp:
        while zigzag != 4 and i != mida_serp:
            aux = zigzag
            while aux != 0:
                print(".", end = "")
                aux -= 1
            print(COS)
            zigzag += 1
            i += 1
        if zigzag == 4:
            zigzag -= 1
            while zigzag != 0 and i != mida_serp:
                aux = zigzag
                while aux != 0:
                    print(".", end = "")
                    aux -= 1
                print(COS)
                zigzag -= 1
                i += 1
    print(CUA)
