class Pessoa:
    def __init__(self, *filhos, nome=None, idade=56):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    nilton = Pessoa(nome='Nilton')
    matheus = Pessoa(nome='Matheus', idade=34)
    print(Pessoa.cumprimentar(matheus))
    print(id(matheus))
    print(matheus.cumprimentar())
    print(matheus.nome)
    print(matheus.idade)
    for filho in matheus.filhos:
        print(filho.nome)
