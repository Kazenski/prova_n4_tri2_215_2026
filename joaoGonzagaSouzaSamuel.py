# ##Exercício 7: A Festa para Maiores
# #O segurança da discoteca tem uma lista com as idades das pessoas na fila: idades = [15, 22, 17, 18, 30, 14, 25].
# Usa um ciclo for para percorrer esta lista e imprimir apenas as idades de quem tem 18 anos ou mais.

idades = [14, 15, 22, 17, 18, 30, 14, 25, 23, 59]


for idade in idades:
    if idade >= 18:
        print(idade)
