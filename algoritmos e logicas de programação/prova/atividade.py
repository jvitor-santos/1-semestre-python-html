a=0
b=0
c=0
d=0
e=0
x=0
percentual=0
print("Qual candidato você desaja votar: 1-candidato A, 2-candidato B, 3-candidato C, 4 -para votar nulo e 5- para votar branco.")
op=int(input("Digite uma opção: "))
while op>=0 and op <=5:
    x=x+1
    if op==1:
        a=a+1
    elif op==2:
        b=b+1
    elif op==3:
        c=c+1
    elif op==4:
        d=d+1
    elif op==5:
        e=e+1
    print("Qual candidato você desaja votar: 1-candidato A, 2-candidato B, 3-candidato C, 4 -para votar nulo e 5- para votar branco.")
    op=int(input("Digite uma opção: "))
percentual=(100/x)*(d+e)
print("O total de votos no candidato A é de: ",a)
print("O total de votos no candidato B é de: ",b)
print("O total de votos no candidato C é de: ",c)
print("O total de votos nulos é de: ",d)
print("O total de votos em branco é de: ",e)
print("O percentual dos votos em brancos e nulos é de: ",percentual)
    
