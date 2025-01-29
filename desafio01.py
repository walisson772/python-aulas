# Desafio -> fazer uma função que receba o valor minimo e valor maximo
# Criar um dic com produtos e valores e no final mostrar somente os produtos que ficam entre o valor minimo e o valor maximo.
import os

def filtro_de_valores(minimo, maximo, produtos):
    for valor in produtos:
        if valor['Valor'] > minimo and valor['Valor'] < maximo:
            print(f'{valor['Item']} -> {valor["Valor"]}')
            return
    
def opcoes():
    print('1) Filtrar preços')
    print('2) Mostrar produtos sem filtrar valor')
    print('3) Sair')

def mostrar_produtos(produtos):
    for produto in produtos:
        print(f'{produto['Item']} {produto['Valor']}')
PRODUTOS = [
    {'Item': 'Iphone', 'Valor': 5500},
    {'Item': 'Sansung s24', 'Valor': 7500},
    {'Item': 'Lg ultragear', 'Valor': 1000},
    {'Item': 'Tv 65pl', 'Valor': 3500},
    {'Item': 'Tablet', 'Valor': 2500},
]
while True:
    opcoes()
    escolha = int(input('O que deseja: '))
    if escolha == 1:
        try:
            os.system('cls')
            minimo = float(input('Digite o valor minimo do produto: '))
            maximo = float(input('Dogote o valor maximo do produto: '))

            print(f'Os produtos entre {minimo} e {maximo}:')
            filtro_de_valores(minimo, maximo, PRODUTOS)
        except ValueError:
            print('Digite apenas valores numericos')
            
    elif escolha == 2:
        os.system('cls')
        mostrar_produtos(PRODUTOS)

    elif escolha == 3:
        break

    else:
        print('Essa opção não existe')
    # Desafio concluido.