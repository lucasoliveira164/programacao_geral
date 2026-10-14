class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: au au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome}  Raça: {self.raca}  Idade: {self.idade} anos")

cachorro1 = Cachorro(nome="Rex", raca="Pastor Alemão", idade=3)
cachorro2 = Cachorro(nome="Mel", raca="Poodle", idade=5)

print("Cachorro 1:")
cachorro1.latir()
cachorro1.mostrar_info()

print()

print("Cachorro 2:")
cachorro2.latir()
cachorro2.mostrar_info()

print()

cachorro1.idade = 4

print("Após alterar a idade do Rex: ")
cachorro1.mostrar_info()