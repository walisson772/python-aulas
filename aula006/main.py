
def inverter_nome(nome):    
    c = len(nome) - 1
    nome_invertido = ''
    while True:
        invertido = nome[c]
        c = c - 1
        nome_invertido += invertido
        if c < 0:
            break
    return nome_invertido

def verificar_palindromo(nome):
    nome_invertido = inverter_nome(nome)
    if nome == nome_invertido:
        print('Seu nome é um palindromo')
        print(f'Nome original: {nome}')
        print(f'Nome invertido: {nome_invertido}')
    
    else:
        print('Seu nome não é um palindromo')
        print(f'Nome original: {nome}')
        print(f'Nome invertido: {nome_invertido}')

verificar_palindromo('ana')