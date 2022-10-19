#A Loja Compre Bem vende produtos pela Internet. Elabore um algoritmo que receba 3 pedidos de clientes diferentes. Cada pedido é composto pelos seguintes itens:
#Código do produto, descrição do produto, preço unitário e quantidade.
#Calcule o valor da compra. Se o valor da compra for acima de 100,00 dar um desconto de 10% senão o desconto deve ser de 5%.
#Imprimir o desconto e o valor da compra de cada cliente com o desconto.
i=1
while i<=3:
    pedido=int(input("Digite o numero do pedido: "))
    codigo=int(input("Digite o codigo do produto: "))
    descricao=str(input("Descreve o produto: "))
    p=float(input("Digite o preço do produto: "))
    q=int(input("Informe a quantidade de produto: "))
    x=q*p
    if x>100:
        desconto=x*0.1
        print("Desconto de: ",desconto)
        print("Valor da compra: ",x-desconto)
    else:
        desconto=x*0.05
        print("Desconto de: ",desconto)
        print("Valor da compra: ",x-desconto)
    i=i+1
