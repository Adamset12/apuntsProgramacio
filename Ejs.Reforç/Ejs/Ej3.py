import math
c_a = int(input("Catet a:"))
c_b = int(input("Catet b:"))

hipotenusa = math.sqrt(c_a*c_a + c_b*c_b)
print("Hipotenusa:", str(round(hipotenusa, 2)))
