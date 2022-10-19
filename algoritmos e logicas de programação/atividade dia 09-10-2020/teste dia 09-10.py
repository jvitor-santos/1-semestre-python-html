sm=int(input("Digite seu saldo médio: "))
if sm<=500:
    print("O saldo médio é de: ",sm)
    print("Nenhum crédito")
else:
    if sm<1000:
        x=sm*0.30
        print("O saldo médio é de: ",sm)
        print("O percentual de crédito será de: ",x)
    else:
            if sm<3000:
                x=sm*0.40
                print("O saldo médio é de: ",sm)
                print("O percentual de crédito será de: ",x)
            else:
                x=sm*0.50
                print("O saldo médio é de: ",sm)
                print("O percentual de crédito será de: ",x)

