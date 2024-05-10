"""
Adam Ben Ahmed Belachi
11/12/2023
e2
"""
try:
    import random
    number = random.randint(1, 100)
    #para comprobar, quitar el comentario de la linea de debajo
    print(number)
    guess = int(input())
    counter = 1
    while guess != number and counter != 10:
        if guess < number: print("Prueba un numero más alto. Llevas " + str(counter) + " intentos.")
        if guess > number: print("Prueba un numero más bajo. Llevas " + str(counter) + " intentos.")
        guess = int(input())
        counter += 1
    if guess == number: print("Lo has conseguido en " + str(counter) + " intentos.")
    elif counter == 1: print("Lo has conseguido en " + str(counter) + " intento.")
    else: print("Te quedaste sin intentos, el numero era: " + str(number))
except:print("Utiliza valores válidos.")