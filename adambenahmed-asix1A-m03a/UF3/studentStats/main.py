import os
def verificar_llista(notes):
    notes = notes.split()
    notes_final = []
    try:
        for nota in notes:
            notes_final.append(int(nota))
    except:
        print("Fica una llista vàlida")
        return False, notes
    return True, notes_final
def notes_stats(notes):
    minima = notes[0]
    maxima = notes[0]
    mitjana = 0
    for nota in notes:
        if nota < minima:
            minima = nota
        elif nota > maxima:
            maxima = nota
        mitjana += nota
    mitjana = round(mitjana / len(notes), 1)
    if len(notes) == 1:
        mitjana = notes[0]
    return minima, maxima, mitjana
def imprimir_stats(minima, maxima, mitjana):
    print(f"Nota mínima: {minima}\nNota màxima: {maxima}\nNota mitjana: {mitjana}")
def main():
    file = input()
    if os.path.exists(file):
        try:
            with open(file, mode='rt', encoding='utf-8') as f:
                notes = f.read()
                valid, notes = verificar_llista(notes)
                if valid:
                    minima, maxima, mitjana = notes_stats(notes)
                    imprimir_stats(minima, maxima, mitjana)
        except:
            print("Error inesperat")
    else:
        print("No existeix l'arxiu")

main()
