b=0
for i in range(5):
    aluno=str(input("Digite o nome do aluno: "))
    prova1=float(input("Digite a nota da prova: "))
    prova2=float(input("Digite a nota da segunda prova: "))
    media= (prova1+prova2)/2
    b=b+media
    mediageral=b/5
    print("A media do aluno é de: ",media)
print("A media da sala é de: ",mediageral)
