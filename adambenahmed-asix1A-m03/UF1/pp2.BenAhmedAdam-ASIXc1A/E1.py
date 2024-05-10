'''
Adam Ben Ahmed ASIXc1A
15/12/2023
pp2
E1/ClassRoomStatus
'''
try:
    notes = input()
    if notes != "":
        notes = notes.split()
        aprovats = 0
        suspesos = 0
        llistaaprovats = ""
        llistasuspesos = ""
        valid = True
        for j in range(0, len(notes)):
            if int(notes[j]) >= 5:
                ultimaprovat = j
            else:
                ultimsuspes = j
            if int(notes[j]) not in range(0, 11):
                print("Fica notes vàlides")
                valid = False
        if valid:
            for i in range(0, len(notes)):
                if int(notes[i]) not in range(0, 11):
                    print("Fica valors vàlids.")
                elif int(notes[i]) >= 5:
                    aprovats += 1
                    if i != ultimaprovat:
                        llistaaprovats += notes[i] + ", "
                    else:
                        llistaaprovats += notes[i]
                else:
                    suspesos += 1
                    if i != ultimsuspes:
                        llistasuspesos += notes[i] + ", "
                    else:
                        llistasuspesos += notes[i]
            print(f":( Suspesos: {suspesos}\n{llistasuspesos}\n:) Aprovats: {aprovats}\n{llistaaprovats}")
    else: print("Posa alguna cosa >:(")
except:
    print("Fica valors vàlids.")