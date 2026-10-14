# 1. Classe: o modelo (planta)

class Celular:
    def __init__(self, marca, modelo, cor, bateria: int = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

        # 4. Métodos: os métodos são os comportamentos do objeto
        def ligar(self):
            # O método consulta um atributo do próprio objeto
            if self.bateria == 0:
                print("sem bateria! Coloque para carregar!")
            else:
                self.ligado = True
                print("Ligado")

        def desligar(self):
            self.ligado = False
            print("Desligado")


# 5. Objetos: criados a partir da classe
celular1 = Celular(marca="Samsung", modelo="a23", cor="Preto")
celular2 = Celular(marca="Motorola", modelo="g54", cor="azul")

# 6. Acessando e alterando atributos
# Usamos objeto.atributo
print(celular1.marca)
print(celular1.modelo)
print(celular1.cor)

print(celular2.marca)
print(celular2.modelo)
print(celular2.cor)

#7. Chamando métodos
#Usamos objeto.metodo() para pedir que o objeto faça algo
celular2.ligar()


