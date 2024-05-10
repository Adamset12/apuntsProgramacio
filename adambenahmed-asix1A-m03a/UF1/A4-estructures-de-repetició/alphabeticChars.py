char = 'A'
i = 1
while i != 27:
    for x in range(i):
        print(chr(ord(char) + x) + " ", end = "")
        x += 1
    print("\n", end = "")
    i += 1