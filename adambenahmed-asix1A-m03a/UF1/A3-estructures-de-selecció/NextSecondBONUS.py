"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    import time

    toadd = int(input("Quants segons vols sumar: "))

    t = time.localtime()
    print("Hora actual: " + str(time.strftime("%H:%M:%S", t)))
    current_time = (time.strftime("%H:%M:%S", t)).split(":")
    current_time[0] = int(current_time[0])
    current_time[1] = int(current_time[1])
    current_time[2] = int(current_time[2])
    current_time[2] += toadd
    while current_time[2] > 60:
        current_time[2] -= 60
        current_time[1] += 1
    while current_time[1] > 60:
        current_time[1] -= 60
        current_time[0] += 1
    while current_time[0] > 24:
        current_time[0] -= 24
    print(f"Hora després de sumar els segons: {current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d}")
except ValueError or IndexError: print("Fica valors vàlids")
