def menu(memoria):
    print('----------------------------------------')
    print('Estado da Memória: '+ str(memoria))
    print('Opções: ')
    print('  ')
    print('(1) Somar')
    print('(2) Subtrair')
    print('(3) Multiplicar')
    print('(4) Dividir')
    print('(5) Limpar Memória')
    print('(6) Sair do programa')
    print(' ')
    return int(input('Qual opção você deseja? '))

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a / b

memoria = 0
Sair = False
while not Sair:
    opcao = menu(memoria)
    if opcao == 1:
        valor = float(input('Qual o valor a somar? '))
        memoria = somar(memoria,valor)
        print('----------------------------------')
    elif opcao == 2:
        valor = float(input('Qual o valor a subtrair? '))
        memoria = subtrair(memoria, valor)
        print('----------------------------------------')
    elif opcao == 3:
        valor = float(input('Qual o valor a multiplicar? '))
        memoria = multiplicar(memoria, valor)
        print('----------------------------------------')
    elif opcao == 4:
        valor = float(input('Qual o valor a dividir? '))
        memoria = dividir(memoria,valor)
        print('----------------------------------------')
    elif opcao == 5:
        memoria = 0
        print('----------------------------------------')
    elif opcao == 6:
        Sair = True

