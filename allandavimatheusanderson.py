# Exercício 5: A Média da Prova
# Dada a lista de classificações de um aluno: notas = [14.5, 18.0, 12.5, 9.0].
# Usa um ciclo for para somar as notas e, no final do ciclo, divide esse valor pelo tamanho da lista (podes usar a função len(notas)) para exibir a média final.

notas = [14.5, 18.0, 12.5, 9.0]
soma = 0
for i in notas:
    soma = soma + i
media = soma / len(notas)
print(f"A sua média é {media}")
