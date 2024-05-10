number = int(input("Dame los minutos:"))
if number >= 0:
    hora = number / 60
    minutes = number - int(hora)
    print("Son " + str(int(hora)) + " horas y " + str(int(minutes)) + " minutos.")
else:
    print("Dame un número valido de minutos")