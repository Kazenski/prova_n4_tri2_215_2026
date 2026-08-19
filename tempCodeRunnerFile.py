#  Exercício 10: O Gerente de Promoção
# Uma loja de roupa tem a seguinte lista de preços: precos = [100.0, 50.0, 80.0, 200.0, 150.0].
# Hoje é dia de Black Friday! Cria uma lista vazia chamada precos_com_desconto. Usa um ciclo for para pegar em cada preço, aplicar um desconto de 20 %, e guardar esse novo valor na nova lista. No final, imprime a lista com os preços reduzidos.
precos = [100.0, 50.0, 80.0, 200.0, 150.0]
precos_com_desconto = []
for preco in precos:
    novo_preco = preco * 0.8
    precos_com_desconto.append(novo_preco)
print(precos_com_desconto)