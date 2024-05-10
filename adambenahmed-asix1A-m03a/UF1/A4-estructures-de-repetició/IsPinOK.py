PWD = "1234"

clave = input("Dime la clave:")
tries = 1
while clave != PWD and tries != 3:
   print("Clave incorrecta!!!")
   clave = input("Dime la clave:")
   tries += 1
if tries == 3 and clave != PWD: print("LAS CAGAO BACALAO")
else: print("Benvingut")
print("Programa terminado")