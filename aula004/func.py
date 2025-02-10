import os
soma = lambda x, y: x + y
divisao = lambda x, y: x / y
multiplicar = lambda x, y: x * y
subtrair = lambda x, y: x - y

while True:
    print('1) somar')
    print('2) dividir')
    print('3) multiplicar')
    print('4) subtrair')
    print('5) sair')
    try:
        resposta = int(input('Qual a escolha: '))
        if resposta == 5:
            break
        num = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        
        if resposta == 1:
            os.system('cls')
            print(soma(num, num2))
            
        elif resposta == 2:
            os.system('cls')
            print(divisao(num, num2))

        elif resposta == 3:
            os.system('cls')
            print(multiplicar(num, num2))

        elif resposta == 4:
            os.system('cls')
            print(subtrair(num, num2))
        
        

        else:
            print('Opção invalida essa opção não existe.')

    except ZeroDivisionError:
        print('Não tem como dividir por zero')

    except ValueError:
        print('Digite apenas numeros inteiros')