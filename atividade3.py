nomes = ["Dipirona", "Paracetamol", "Loratadina", "Amoxicilina", "Ibuprofeno"]
precos = [12.50, 9.90, 18.75, 25.00, 14.30]
estoques = [20, 15, 8, 3, 12]


def buscarIndice(nome):
    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            return i
    return -1


def listarMedicamentos():
    for i in range(len(nomes)):
        if estoques[i] < 5:
            situacao = "Estoque baixo"
        else:
            situacao = "Estoque normal"
        print(nomes[i], "- Preço: R$", precos[i], "- Estoque:", estoques[i], "-", situacao)


def pesquisarMedicamento():
    nome = input("Nome do medicamento: ")
    i = buscarIndice(nome)
    if i == -1:
        print("Medicamento não encontrado.")
    else:
        print(nomes[i], "- Preço: R$", precos[i], "- Estoque:", estoques[i])


def registrarVenda():
    nome = input("Nome do medicamento: ")
    i = buscarIndice(nome)
    if i == -1:
        print("Medicamento não encontrado.")
        return

    quantidade = int(input("Quantidade a vender: "))
    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    if quantidade > estoques[i]:
        print("Estoque insuficiente.")
        return

    estoques[i] -= quantidade
    print("Venda realizada. Novo estoque:", estoques[i])


def reporEstoque():
    nome = input("Nome do medicamento: ")
    i = buscarIndice(nome)
    if i == -1:
        print("Medicamento não encontrado.")
        return

    quantidade = int(input("Quantidade a repor: "))
    if quantidade <= 0:
        print("Quantidade inválida.")
        return

    estoques[i] += quantidade
    print("Estoque reposto. Novo estoque:", estoques[i])


def verificarEstoqueBaixo():
    for i in range(len(nomes)):
        if estoques[i] < 5:
            print(nomes[i], "-", estoques[i], "unidades")


while True:
    print("\n1 - Listar medicamentos")
    print("2 - Pesquisar medicamento")
    print("3 - Registrar venda")
    print("4 - Repor estoque")
    print("5 - Mostrar estoque baixo")
    print("6 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listarMedicamentos()
    elif opcao == "2":
        pesquisarMedicamento()
    elif opcao == "3":
        registrarVenda()
    elif opcao == "4":
        reporEstoque()
    elif opcao == "5":
        verificarEstoqueBaixo()
    elif opcao == "6":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")