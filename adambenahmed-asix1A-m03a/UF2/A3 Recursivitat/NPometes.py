try:
    def getAppleSongStanza(applesCount):
        if applesCount == 1:
            pomes = "pometa"
        else:
            pomes = "pometes"
        stanza =f"{applesCount} {pomes} té el pomer,\n" \
              f"de {applesCount} una, de {applesCount} una,\n" \
              f"{applesCount} {pomes} té el pomer,\n" \
              f"de {applesCount} una en caigué.\n\n" \
              f"Si mireu el vent d'on vé\n" \
              f"veureu el pomer com dansa,\n" \
              f"si mireu el vent d'on vé\n" \
              f"veureu com dansa el pomer.\n"
        return stanza
    def getAppleSong(applesCount):
        """
        :param applesCount: Number of apples
        :return: All the song text
        """
        print(getAppleSongStanza(applesCount))
        if applesCount != 1:
            getAppleSong(applesCount-1)

    def main():
        pomes = abs(int(input()))
        if pomes > 500:
            print("pero tu cuanto comes chaval")
        else:
            getAppleSong(pomes)
    main()
except:
    print("sioque")