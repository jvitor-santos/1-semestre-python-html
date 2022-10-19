s=int(input("Digite seu salário: "))
if s<500:
    x=s+(s*0.15)
else:
    if s<=1000:
        x=s+(s*0.10)
    else:
        x=s+(s*0.05)
print("O salario sera de: ",x)
