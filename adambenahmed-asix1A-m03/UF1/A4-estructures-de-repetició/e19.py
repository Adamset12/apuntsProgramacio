try:
    menu = "1. Literatura\n2. Cinema\n3. Música\n4. Videojocs\n5. Sortir\n"
    Literatura = "Don Quijote"
    Cinema = "Titanic"
    Música = "Shape Of You"
    Videojocs = "Minecraft"
    print(menu)
    opció = input("Escull una opció: ")
    sortir = False
    while opció in range(1, 6) and not sortir:
        match opció:
            case 1:print("\n" + Literatura + "\n")
            case 2:print("\n" + Cinema + "\n")
            case 3:print("\n" + Música + "\n")
            case 4:print("\n" + Videojocs + "\n")
            case 5: sortir = True
        if opció == 5: print("\nSortint del menú.")
        else:
            print(menu)
            opció = int(input("Escull una altre opció: "))
    if opció not in range(1, 6): print("\nFica valors vàlids.")
except: print("\nFica valors vàlids.")
