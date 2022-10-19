#Desenvolver o algoritmo: Ler um número e imprimir se ele é positivo, negativo ou nulo.
n= float(input("Informar o numero: "))
if n>0:
    print("O numero é positivo: ")
else:
    if n<0:
        print("O numero é negativo: ")
    else:
        print("O numero é nulo: ")
