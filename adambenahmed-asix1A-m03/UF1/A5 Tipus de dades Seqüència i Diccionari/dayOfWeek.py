'''
Adam Ben Ahmed
ASIXc1A
dayOfWeek
'''
try:
    dies = ('dilluns\nlunes\nmonday ', 'diamrts\nmartes\ntuesday', 'dimecres\nmiercoles\nwednesday',
            'dijous\njueves\nthursday', 'divendres\nviernes\nfriday', 'dissabte\nsabado\nsaturday', 'diumenge\ndomingo\nsunday')
    dia = int(input())
    if dia not in range(1, 8): dia = 'a' - 1
    print(dies[dia-1])
except: print("Fica valors vàlids.")