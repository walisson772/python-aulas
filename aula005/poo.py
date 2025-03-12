

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.idade = idade
        self.id = 17

    def diga_ola(self):
        print(f'Olá {self.nome} {self.sobrenome} é um prazer te conhecer')

    def diga_sua_idade(self):
        print(f'Olá meu nome é BOOT e minha idade é {self.id}')

        if self.idade > self.id:
            print(f'Nossa você tem {self.idade} você é mais velho que eu!')
        
        elif self.idade == self.id:
            print(f'Nossa temos a mesma idade eu tambem tenho {self.idade}!')

        else:
            print(f'Nossa eu sou mais velho que você {self.nome}')

# nome = 'walisson'
# sobrenome = 'santos'
# idade = 16


# pessoa1 = Pessoa(nome, sobrenome, idade)
# pessoa1.diga_ola()