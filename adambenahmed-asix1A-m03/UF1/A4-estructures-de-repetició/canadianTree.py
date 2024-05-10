'''
canadianTree
Adam
'''
try:
    from time import sleep
    mida = int(input())
    aux = 1
    if mida > 2:
        mida_fulles = round(mida * 0.75)
        mida_tronc = mida - mida_fulles
        amplada_tronc = round(mida_fulles*0.33)
        for x in range(mida_fulles, 0, -1):
            if x == mida_fulles:
                print(" " * x + "🌟" * aux)
            else:
                print(" " * x + "🎄" * aux)
            aux += 1
            sleep(0.5)
        while mida_tronc != 0:
            print(" " * (aux - amplada_tronc) + "🪵" * amplada_tronc)
            mida_tronc -= 1
            sleep(0.7)
    else:
        print("Fica un valor major a 2.")
except:
    print("Fica valors vàlids.")