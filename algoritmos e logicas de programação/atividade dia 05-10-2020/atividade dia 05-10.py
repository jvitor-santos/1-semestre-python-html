municipio= input("Nome do minicipio: ")
eleitores= int(input("Quantidade de eleitores: "))
votos=int(input("Quantidade de votos do candidato: "))
if eleitores>=20000 and votos<eleitores/2:
    print("Tera segundo turno")
else:
    print("Não tera segundo turno")
