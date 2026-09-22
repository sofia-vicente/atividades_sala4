def registrarTentativas():
    tentativas = []
    for i in range(10):
        valor = int(input("Resultado da tentativa " + str(i + 1) + " (0, 1, 2 ou 3): "))
        while valor not in (0, 1, 2, 3):
            print("Valor inválido. Digite 0, 1, 2 ou 3.")
            valor = int(input("Resultado da tentativa " + str(i + 1) + " (0, 1, 2 ou 3): "))
        tentativas.append(valor)
    return tentativas


def calcularPontuacao(tentativas):
    pontos = 0
    for valor in tentativas:
        pontos += valor
    return pontos


def calcularAproveitamento(tentativas):
    convertidos = 0
    for valor in tentativas:
        if valor != 0:
            convertidos += 1
    return (convertidos / len(tentativas)) * 100


def encontrarCestaMaisFrequente(tentativas):
    cesta1 = 0
    cesta2 = 0
    cesta3 = 0
    for valor in tentativas:
        if valor == 1:
            cesta1 += 1
        elif valor == 2:
            cesta2 += 1
        elif valor == 3:
            cesta3 += 1

    maior = cesta1
    if cesta2 > maior:
        maior = cesta2
    if cesta3 > maior:
        maior = cesta3

    if maior == 0:
        return "Nenhuma cesta convertida"

    tipos = []
    if cesta1 == maior:
        tipos.append(1)
    if cesta2 == maior:
        tipos.append(2)
    if cesta3 == maior:
        tipos.append(3)
    return tipos


tentativas = registrarTentativas()

pontuacao = calcularPontuacao(tentativas)
aproveitamento = calcularAproveitamento(tentativas)
cesta_frequente = encontrarCestaMaisFrequente(tentativas)

print("Tentativas:", tentativas)
print("Pontuação total:", pontuacao)
print("Aproveitamento:", aproveitamento, "%")
print("Cesta mais frequente:", cesta_frequente)