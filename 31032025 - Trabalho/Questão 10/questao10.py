print ("Seja bem-vindo(a) ao sistema de aprovação da Cruzeiro do sul!")
print("\n")

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if (media >= 7):
    print ("A média das suas notas foi", "%.1f" % media, "portanto você foi aprovado!")
else:
    print("A média das suas notas foi", "%.1f" % media, "portanto você foi reprovado...")
