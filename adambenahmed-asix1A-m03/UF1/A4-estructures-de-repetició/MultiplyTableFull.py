for x in range(1, 10):
    for y in range(1, 10):
        nmbr = str(x * y)
        if len(nmbr) != 2:
            print(" " + nmbr + " ", end = "")
        else:
            print(nmbr + " ", end="")
    print("\n", end = "")