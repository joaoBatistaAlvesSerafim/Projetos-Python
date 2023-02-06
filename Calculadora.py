import os

print("============== PROGRAMA CALCULADORA ==============")
print("======== BEM VINDO AO PROGRAMA CALCULADORA =======")
print("Para Subtração digite: '-'")
print("Para Adição digite: '+'")
print("Para Divisão digite: '/'")
print("Para Multiplicação digite: '*'")

operacao = input("Digite a sua opção")
while operacao not in ('-', '+', '/', '*'):
    print('\n')
    print("Opção incorreta um dos valores a seguir: ")
    print("Para Subtração digite: '-'")
    print("Para Adição digite: '+'")
    print("Para Divisão digite: '/'")
    print("Para Multiplicação digite: '*'")
    print('\n')
    operacao = input("Digite a sua opção")
print("")
if operacao == '-':
    print("Opção escolhida 'Subtração'")
    n1 = float(input("Qual o primeiro valor ? "))
    print("Valor 1 digitado:", n1)
    n2 = float(input("Qual o segundo valor ? "))
    print("Valor 2 digitado:", n2)
    resultado = n1 - n2
    print("O resultado é:", "%.2f" % resultado)
    print('\n')

if operacao == '+':
    print("Opção escolhida 'Adição'")
    n1 = float(input("Qual o primeiro valor ? "))
    print("Valor 1 digitado:", n1)
    n2 = float(input("Qual o segundo valor ? "))
    print("Valor 2 digitado:", n2)
    resultado = n1 + n2
    print("O resultado é:", "%.2f" % resultado)
    print('\n')

if operacao == '/':
    print("Opção escolhida 'Divisão'")
    n1 = float(input("Qual o primeiro valor ? "))
    print("Valor 1 digitado:", n1)
    n2 = float(input("Qual o segundo valor ? "))
    print("Valor 2 digitado:", n2)
    resultado = n1 / n2
    print("O resultado é:", "%.2f" % resultado)
    print('\n')

if operacao == '*':
    print("Opção escolhida 'Multiplicação'")
    n1 = float(input("Qual o primeiro valor ? "))
    print("Valor 1 digitado:", n1)
    n2 = float(input("Qual o segundo valor ? "))
    print("Valor 2 digitado:", n2)
    resultado = n1 * n2
    print("O resultado é:", "%.2f" % resultado)
    print('\n')
print("")
continuar = input("Deseja continuar ? 'S / N' ?")

while continuar != 's' and continuar != 'n':
    continuar = input("Valor incorreto, digite novamente: 'S / N' ?")

while continuar == 's' or continuar == 'S':
    print("Para Subtração digite: '-'")
    print("Para Adição digite: '+'")
    print("Para Divisão digite: '/'")
    print("Para Multiplicação digite: '*'")
    operacao = input("Digite a sua opção")
    print("")
    if operacao == '-':
        print("Opção escolhida 'Subtração'")
        n1 = float(input("Qual o primeiro valor ? "))
        print("Valor 1 digitado:", n1)
        n2 = float(input("Qual o segundo valor ? "))
        print("Valor 2 digitado:", n2)
        resultado = n1 - n2
        print("O resultado é:", "%.2f" % resultado)
        print('\n')

    if operacao == '+':
        print("Opção escolhida 'Adição'")
        n1 = float(input("Qual o primeiro valor ? "))
        print("Valor 1 digitado:", n1)
        n2 = float(input("Qual o segundo valor ? "))
        print("Valor 2 digitado:", n2)
        resultado = n1 + n2
        print("O resultado é:", "%.2f" % resultado)
        print('\n')

    if operacao == '/':
        print("Opção escolhida 'Divisão'")
        n1 = float(input("Qual o primeiro valor ? "))
        print("Valor 1 digitado:", n1)
        n2 = float(input("Qual o segundo valor ? "))
        print("Valor 2 digitado:", n2)
        resultado = n1 / n2
        print("O resultado é:", "%.2f" % resultado)
        print('\n')
    if operacao == '*':
        print("Opção escolhida 'Multiplicação'")
        n1 = float(input("Qual o primeiro valor ? "))
        print("Valor 1 digitado:", n1)
        n2 = float(input("Qual o segundo valor ? "))
        print("Valor 2 digitado:", n2)
        resultado = n1 * n2
        print("O resultado é:", "%.2f" % resultado)
        print('\n')

    continuar = input("Deseja continuar ? 'S / N'")
    while continuar != 's' and continuar != 'n':
        continuar = input("Valor incorreto, digite novamente: 'S / N' ?")
    print("")

else:
    print("Obrigado por usar a calculadora")
