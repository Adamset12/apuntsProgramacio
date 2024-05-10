str = input("El que vols codificar: ")
if str != "":
    i = 0
    length = len(str)
    encoded = ""
    while i < length:
        if str[i] == 'a' or str[i] == 'A':
            encoded += '1'
            i += 1
        elif str[i] == 'e' or str[i] == 'E':
            encoded += '2'
            i += 1
        elif str[i] == 'i' or str[i] == 'I':
            encoded += '3'
            i += 1
        elif str[i] == 'o' or str[i] == 'O':
            encoded += '4'
            i += 1
        elif str[i] == 'u' or str[i] == 'U':
            encoded += '5'
            i += 1
        else:
            encoded += chr(ord(str[i]))
            i += 1
    print("L'input codificat és: ", encoded)