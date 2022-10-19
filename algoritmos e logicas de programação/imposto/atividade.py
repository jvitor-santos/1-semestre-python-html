i=0
for i in range(1,10,1):
    nome=str(input("Digite seu nome: "))
    salario=float(input("Digite sua renda: "))
    if salario<600:
        print(nome)
        print("Isento")
    else:
        if salario>=1500:
            x=salario-(salario*0.15)
            print(nome)
            print("O valor aliquota do imposto é de: ", x)
        else:
            x=salario-(salario*0.10)
            print(nome)
            print("O valor aliquota do imposto é de: ", x)
