#opcoes = '0 - Mostrar Portifolio | 1 - Alugar um Carro | 2 - Devolver um carro'
import os
lista_Carros = ['Chevrolet Tracker - R$120,00 /Dia',
                'Chevrolet Onix - R$90,00 /Dia',
                'Chevrolet Spin - R$150 /Dia',
                'Hyundai HB20 - R$85,00 /Dia',
                'Hyundai Tucson - R$120,00 /Dia',
                'Fiat Uno - R$60,00 /Dia',
                'Fiat Mobi - R$70,00 /Dia',
                'Fiat Pulse - R$130,00 /Dia']


os.system('cls' if os.name == 'nt' else 'clear')

valores = [120.00, 90.00, 150, 85.00, 120.00, 60.00, 70.00, 130.00]
alugados = ""
print(alugados)

continuar = 0

while continuar == 0:

    print('===============================')
    print('Bem Vindo a Locadora de Carros! ')
    print('===============================')
    print('O que deseja fazer ?\n')

    opcoes = int(input(print(
        '0 - Mostrar Portifolio | 1 - Alugar um Carro | 2 - Devolver um carro \n')))

    if opcoes == 0:
        print('[PORTIFOLIO]\n')
        for x in (lista_Carros):
            print("[", lista_Carros.index(x), "]", (x))
        print('Deseja continuar ?\n')

    elif opcoes == 1:
        print('Veja nosso Portifolio de carros disponiveis! \n')
        for x in (lista_Carros):
            print("[", lista_Carros.index(x), "]", (x))
        print('\n')

        aluguel = int(input('Qual carro deseja alugar ?\n'))

        print('A opção escolhida foi ', lista_Carros[aluguel], '\n')
        lista_Carros.pop(aluguel)
        valores.pop(aluguel)

        print('o valor da diaria é R$',
              "%.2f" % valores[aluguel])
        dias = float(input("Gostaria de alugar por quantos dias ?\n"))
        print("O valor total do Aluguel será R$",
              (float(valores[aluguel])*dias), '\n')
        print('Obrigado por alugar conosco!\n')

        alugados = alugados + "\n" + (lista_Carros[aluguel])
        print('Deseja continuar ?\n')

    elif opcoes == 2:
        print('Você alugou os carros:')
        for x in [alugados]:
            print(x)
        print('deseja devolver ?\n')

    continuar = int(input('0 - Continuar | 1 - Sair\n'))
os.system('cls')
