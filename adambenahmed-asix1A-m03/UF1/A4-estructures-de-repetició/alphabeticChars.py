char = 'A'
i = 1
while i <= (ord('Z') - ord('A') + 1):
    for x in range(i):
        print(chr(ord(char) + x) + " ", end = "")
    print("\n", end = "")
    i += 1