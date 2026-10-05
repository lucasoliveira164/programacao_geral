#O que é uma função?

#Uma função é um bloco de código criado para realizar uma determinada tarefa.

#Ela permite organizar e reutilizar o código.

#1. Criando uma função

#Utilizar a palavra def para uma função

print("Teste")

def saudacao():
    print("Olá, seja bem-vindo")

    #Para executar a função, chamamos seu nome
saudacao()

#2. Função com parâmetro

def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("Lucas")
saudacao("Carlos")

#3. Mais de um parâmetro

def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Lucas", 18)

# 4. Função com cálculo

def somar(numero1: int, numero2: int):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

# Chamada correta com argumentos nomeados
somar(numero1=10, numero2=20)

    #5. Retornando um valor
    #0 return devolve um valor para o local onde a função foi chamada

def somar(numero1 , numero2):
    return numero1 + numero2

resultado = somar(10 , 20)
print(resultado)

#6. Função com condição

def verificaridade(idade    ):
    if idade >=18:
        return "Maior idade"
    else:
        return "Menor idade"

resultado = verificaridade(18)
print(resultado)

#Parâmetro com valor padrão
#podemos definir yum valor padrao para um parametro

def saudacao(nome:str="aluno"):
    print(f"ola, {nome}")

    saudacao()
    saudacao("João")

    #8. Vários parâmetros

def calcularmedia(nota1, nota2, nota3):
        media = (nota1 + nota2 +nota3)/3
        return media

print(calcularmedia(8,7,9))

#9. Funcoes para organizar um programa

def cadastraproduto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    return nome, preco

def exibirproduto(nome , preco):
    print("\n ======== Produto =========")
    print(f"nome {nome}")
    print(f"Preço: R${preco}")

nome , preco = cadastraproduto()
exibirproduto(nome , preco)

