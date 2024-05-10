'''
Adam Ben Ahmed
ASIXc1A
swap
'''
try:
    swap = [int(x) for x in input().split()]
    swap[0], swap[-1] = swap[-1], swap[0]
    print(swap)
except:print("Fica valors vàlids.")