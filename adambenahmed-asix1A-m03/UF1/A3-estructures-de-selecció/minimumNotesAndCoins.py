try:
    import decimal
    money = input()
    i = 0
    while i < len(money) and money[i] != ".": i += 1
    aux = money[0:i]
    if len(str(decimal.Decimal(money) % int(aux))) > 4: exit(1)
    money = float(money)
    values = [float('500'), float('200'), float('100'), float('50'), float('20'), float('10'), float('5'), float('2'), float('1'), float('0.50'), float('0.20'), float('0.10'), float('0.05'), float('0.02'), float('0.01')]
    efectivo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i in range(len(values)):
        if money >= values[i]:
            efectivo[i] += money // values[i]
            money -= values[i] * (money //values[i])
        i += 1
    i = 0
    while i in range(len(efectivo)):
        if int(values[i]) > 2 and efectivo[i] > 1: print(str(efectivo[i]) + " bitllets de " + str(values[i]) + "€")
        elif int(values[i]) > 2 and efectivo[i] == 1: print(str(efectivo[i]) + " bitllet de " + str(values[i]) + "€")
        elif int(values[i]) > 0.50 and efectivo[i] > 1: print(str(efectivo[i]) + " monedes de " + str(values[i]) + "€")
        elif int(values[i]) > 0.50 and efectivo[i] == 1: print(str(efectivo[i]) + " moneda de " + str(values[i]) + "€")
        elif efectivo[i] > 1: print(str(efectivo[i]) + " monedes de " + str(values[i]) + " cèntims")
        elif efectivo[i] == 1: print(str(efectivo[i]) + " moneda de " + str(values[i]) + " cèntims")
        i += 1
except: print("Pon un valor vàlido")
