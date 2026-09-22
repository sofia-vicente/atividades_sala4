def calcularTotalGols(gols):
    total = 0
    for gol in gols:
        total += gol
    return total


def calcularMediaGols(gols):
    total = calcularTotalGols(gols)
    return total / len(gols)


def encontrarArtilheiros(jogadores, gols):
    maior = gols[0]
    for gol in gols:
        if gol > maior:
            maior = gol

    artilheiros = []
    for i in range(len(jogadores)):
        if gols[i] == maior:
            artilheiros.append(jogadores[i])
    return artilheiros


def mostrarRelatorio(jogadores, gols):
    for i in range(len(jogadores)):
        print(jogadores[i], "-", gols[i], "gols")

    total = calcularTotalGols(gols)
    media = calcularMediaGols(gols)
    artilheiros = encontrarArtilheiros(jogadores, gols)

    print("Total de gols:", total)
    print("Média de gols:", media)

    print("Jogadores acima da média:")
    for i in range(len(jogadores)):
        if gols[i] > media:
            print(jogadores[i])

    if len(artilheiros) > 1:
        print("Empate na artilharia entre:", artilheiros)
    else:
        print("Artilheiro:", artilheiros[0])


jogadores = ["Vicente", "Creitin", "Junin", "Caleb", "Josué"]
gols = [100, 4, 9, 8, 5]

mostrarRelatorio(jogadores, gols)