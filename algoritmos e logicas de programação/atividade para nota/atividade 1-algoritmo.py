x=0
soma=0
somasol=0
somai=0
div=0
media=0
z=0
porcentagem=0
idade=int(input("Digite sua idade: "))
while idade>0:
    print("Qual seu estado civil? 1=casado(a), 2=solteiro(a), 3=viuvo(a), 4=divorciado(a)")
    op=int(input("Digite a opção: "))
    x=x+1
    if op==1:
        soma=soma+1
    elif op==2:
        somasol=somasol+1
    elif op==3:
        somai=somai+idade
        div=div+1
        media=somai/div
    elif op==4:
        z=z+1
        porcentagem=z/x*100
    idade=int(input("Digite sua idade: "))
print("A quantidade de pessoas casadas é de: ",soma)
print("A quantidade de pessoas solteiras é de: ",somasol)
print("A media de idades de pessoas viuvas é de: ",media)
print("A porcentagem de pessoas divorciadas é de: ",porcentagem)
