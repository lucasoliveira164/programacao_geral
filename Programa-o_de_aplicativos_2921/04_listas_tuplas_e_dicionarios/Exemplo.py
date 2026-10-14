#Listas, Tuplas e Dicionarios

#1. Listas

#  Listas são utilizadas para armazenar vários valores
#  dentro de uma unica váriavel.

nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)

#2. Acessando elementos da lista

print(nomes[0])

print(nomes[1])

#Podemos acessar o ultimo elemento usando -1

print(nomes[-1])

#3. Alterando elementos

# As listas são mutáveis, ou seja, os elementos podem ser alterados

nomes[0] = "Pedro"
print(nomes)

#4. Adicionando elementos

#append() adiciona um elemento novo no final da lista.

nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma determinada posição.

nomes.insert(1, "Mariana")
print(nomes)

#10. Lista de números
notas = [7.5, 8.0, 6.5, 9.0]
soma = 0

for nota in notas:
    soma += nota

    media = soma / len(notas)
    print(f"Média: {media:.1f}")

#11. Tuplas
#Tuplas são semelhantes às listas.
#A principal diferença é que tuplas nã podem
#ser alteradas depois de criadas

coordenadas = (10,20)
print(coordenadas)

# Acessando elementos
print (coordenadas[0])
print (coordenadas[1])

#12. Dicionários
# Dicionários armazenam informações no formato:
# chave: valor

aluno = {
    "nome": "Ana",
    "idade": 18,
    "nota": 8.5
}
print(aluno)

