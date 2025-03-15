import os

class Calculadora:
    def __init__(self, num1, num2):
        self.numero1 = num1
        self.numero2 = num2

    def opcoes(self):
        print('1)Somar')
        print('2)Multiplicar')
        print('3)Dividir')
        print('4)Subtrair')
        print('5)Sair')
        try:
            op = int(input('O que deseja: '))
            return op
        except ValueError:
            print('Digite apenas numeros')

    def somar(self):
        return f'{self.numero1 + self.numero2:.2f}'
    
    def multiplicar(self):
        return f'{self.numero1 * self.numero2:.2f}'
    
    def dividir(self):
        try:
            return f'{self.numero1 / self.numero2:.2f}'
        
        except ZeroDivisionError:
            return 'Não é possivel dividir por zero'
        
    def subtrair(self):
        return self.numero1 - self.numero2
    

while True:
    try:
        num1 = float(input('Digite um numero: '))
        num2 = float(input('Digite outro numero: '))
        cal = Calculadora(num1, num2)
        escolha_user = cal.opcoes()

        if escolha_user == 1:
            os.system('cls')
            print(cal.somar())

        elif escolha_user == 2:
            os.system('cls')
            print(cal.multiplicar())

        elif escolha_user == 3:
            os.system('cls')
            print(cal.dividir())

        elif escolha_user == 4:
            os.system('cls')
            print(cal.subtrair())

        elif escolha_user == 5:
            break

        else:
            print('Essa opção não existe')

    except ValueError:
        print('Por favor digite apenas numeros.')