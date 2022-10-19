Vproduto= float(input("Digite o valor do produto: "))
if Vproduto<20:
    lucro=Vproduto*(45/100)
else:
    lucro=Vproduto*(30/100)
ValorVenda=Vproduto+lucro
print("O lucro é de: R$", lucro)
print("O valor de venda será de: R$", ValorVenda)
