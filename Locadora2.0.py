import os

carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
]


def lista_carros(lista_carros):
    for id, nome_carro in enumerate(lista_carros):
        print(f'[{id}] - {nome_carro[0]}, R${(nome_carro[1]):.2f} /dia')


continuar = 0

alugados = []

while continuar == 0:

    print("\n========================================")
    print("Bem vindo a agência de aluguel de carros")
    print("========================================\n")

    print("Escolha uma das opções a seguir:\n")
    opcoes = int(input(
        "'0 - Mostrar Portifolio | 1 - Alugar um Carro | 2 - Devolver um carro ')\n"))

    if opcoes == 0:
        print("========================================")
        print("Catálogo de carros disponiveis")
        print("========================================\n")
        lista_carros(carros)

    if opcoes == 1:
        lista_carros(carros)
        escolha = int(
            input("\nDigite o numero correspondente ao carro desejado\n"))

        print(
            f"Você escolheu a opção {carros[escolha][0]} no valor de R${carros[escolha][1]:.2f}\n")
        dias = int(input("Por quantos dias você deseja ficar com o carro ?\n"))
        print(
            f"O valor total do aluguel será R${(carros[escolha][1] * dias):.2f}\n")
        alugar = int(
            input("Deseja confirmar o aluguel ?\n 0 = sim | 1 = Não\n"))

        if alugar == 0:
            print(
                f"Parabens você acabou de alugar o carro: {carros[escolha][0]} no valor de R${carros[escolha][1]:.2f}")
            alugados.append(carros.pop(escolha))
        else:
            print(f"Você desistiu de alugar o carro: {carros[escolha][0]}")

    if opcoes == 2:
        if len(alugados) == 0:
            print("Voce não possui carros alugados")

        else:
            print(
                "Você possui os seguintes carros alugados:")
            print(lista_carros(alugados))

            devolver = int(input(
                "Qual carro deseja devolver ?\n"))
            confirma = int(input(
                f"Você escolheu devolver o carro {alugados[devolver][0]} confirma a opção ?\n 0 = sim | 1 = não\n"))

            if confirma == 0:
                print("Obrigado por alugar conosco !")
                carros.append(alugados.pop(devolver))

            if confirma == 1:
                print("Você desistiu de devolder o carro")

    continuar = int(
        input("\nDeseja retornar ao inicio ? 0 = retornar | 1 = encerrar\n"))
    os.system('cls')
