# Exercício 4: O Somatório de Pontos
# Um jogador de videojogos participou em 6 partidas e as suas pontuações foram guardadas na #lista: pontos = [120, 50, 80, 200, 150, 40].
# Usando um ciclo for e uma variável acumuladora (ex: soma = 0 criada antes do ciclo), #calcula e imprime a soma total de pontos que ele fez.

pontos = [120, 50, 80, 200, 150, 40]
soma = 0

for ponto in pontos:
    soma = soma + ponto
print(soma)
