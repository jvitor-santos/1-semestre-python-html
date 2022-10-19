nome=str(input("Qual seu nome? : "))
cidade=str(input("Qual cidade? : "))
print("Opções de Estados: 1-RJ, 2-SP, 3-MG e 4-Outro Esatado")
opcao=int(input("Digite a opção: "))
if opcao==1:
    print("É carioca")
elif opcao==2:
    print("É paulista")
elif opcao==3:
    print("É mineiro")
elif opcao==4:
    print("Outro Estado")
else:
    print("Opção inválida")
