nota = int(input("me diga a media da sua nota: "))
frequencia = int(input("Me diga o seu percentual de frequencia: "))

if frequencia < 75:
    print("Você foi reprovado por frequencia")
elif nota < 6:
    print("Reprovado por nota")
else:
    print("Aprovado")
                 
 
