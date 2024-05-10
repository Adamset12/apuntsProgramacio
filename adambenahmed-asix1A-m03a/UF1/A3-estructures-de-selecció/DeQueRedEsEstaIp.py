def whatsTheMask(ip):
    ip = ip.split("/")
    shortMask = int(ip[1])
    maskref = ["00000000", "00000000", "00000000", "00000000"]
    mask = ""
    thirtytwo = 32
    while thirtytwo != 0:
        i, j = 0, 0
        while j < 8:
            if shortMask != 0:
                mask += (str(chr(ord(maskref[i][j]) + 1)))
                j += 1
                shortMask -= 1
                thirtytwo -= 1
            else:
                mask += maskref[i][j]
                thirtytwo -= 1
                j += 1
        i += 1
    return(mask)
def iptobinary(ip):
    ip = (ip.split("/")[0]).split(".")
    i = 0
    ipbin = ""
    while i < len(ip):
        ipbin += format(int(ip[i]), '08b')
        i += 1
    return (ipbin)
def whatstheipnet (ip, mask):
    i = 0
    ipnet = ""
    while i < 32:
        if mask[i] == '1' and ip[i] == '1': ipnet += '1'
        else: ipnet += '0'
        i+=1
    return (ipnet)
def binaryToDecimal(binary):

    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return(decimal)
def formatipnettodecimal (binipnet):
    ipnet = ""
    ipnet += str(binaryToDecimal(int(binipnet[0:8]))) + "."
    ipnet += str(binaryToDecimal(int(binipnet[8:16]))) + "."
    ipnet += str(binaryToDecimal(int(binipnet[16:24]))) + "."
    ipnet += str(binaryToDecimal(int(binipnet[24:32])))
    return(ipnet)
try:
    ip = input("Cual es la ip separada por ""."" y su mascara indicada con una / detras del último digito de la ip?\n- ")
    print(formatipnettodecimal(whatstheipnet(iptobinary(ip), whatsTheMask(ip))))
except: print("Pon un valor válido.")