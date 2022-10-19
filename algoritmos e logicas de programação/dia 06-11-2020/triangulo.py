a=int(input("Valor de A: "))
b=int(input("Valor de B: "))
c=int(input("Valor de C: "))
if a>b+c or b>a+c or c>a+b:
    print("Isso não é um triângulo")
else:
    print("Este é um triângulo")
    if a==b and b==c:
        print("É um triângulo Equilátero")
    else:
        if a==b or b==c or a==c:
            print("É um triângulo Isósceles")
        else:
            print("É um triangulo escaleno")
