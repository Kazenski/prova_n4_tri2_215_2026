
# Exercício 6: Quantos tiveram positiva?
# Dada uma lista com as notas finais de vários alunos: turma = [15, 7, 18, 14, 9, 13, 6, 10].
# Usa um ciclo for juntamente com uma estrutura condicional (if) para contar quantos alunos
# tiveram nota maior ou igual a 10. Imprime apenas essa quantidade final.

turma = [15, 7, 18, 14, 9, 13, 6, 10]

contador = 0

for nota in turma:
    if nota >= 10:
        contador = contador + 1
print(contador)
