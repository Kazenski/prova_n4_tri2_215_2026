#Exercício 9: Separando os Pares
#Dada uma lista mista de números: numeros = [10, 15, 22, 33, 40, 55, 60].
#Cria uma segunda lista vazia chamada pares = []. Usa um ciclo for para percorrer a primeira lista. Se o número for par, #adiciona-o na lista pares (usando o comando .append()). No final, imprime a lista pares.

numeros = [10, 15, 22, 33, 40, 55, 60]
pares = []

for i in numeros:
    if i % 2 == 0:
        pares.append(i)

print(pares)