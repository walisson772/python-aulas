# Desafio -> fazer uma função que receba o valor minimo e valor maximo
# Criar um dic com produtos e valores e no final mostrar somente os produtos que ficam entre o valor minimo e o valor maximo.

def filtro_de_valores(minimo, maximo, produtos):
    for valor in produtos:
        if valor['Valor'] > minimo and valor['Valor'] < maximo:
            print(f'{valor['Item']} -> {valor["Valor"]}')

PRODUTOS = [
    {'Item': 'Iphone', 'Valor': 5500},
    {'Item': 'Sansung s24', 'Valor': 7500},
    {'Item': 'Lg ultragear', 'Valor': 1000},
    {'Item': 'Tv 65pl', 'Valor': 3500},
    {'Item': 'Tablet', 'Valor': 2500},
]

minimo = float(input('Digite o valor minimo do produto: '))
maximo = float(input('Dogote o valor maximo do produto: '))

print(f'Os produtos entre {minimo} e {maximo}:')
filtro_de_valores(minimo, maximo, PRODUTOS)

# Desafio concluido.