print ("Seja bem-vindo(a) ao cinema Cruzeiro do sul!")
print ("Para verificar se você tem direito a meia-entrada, responda as perguntas a seguir")
print ("\n")

nome = str(input("Me diga o seu nome: "))
idade = int(input("Me diga a sua idade: "))
escolaridade = str(input("Você é estudante?(S/N) "))

print ("\n")

if ((idade <= 12) and (escolaridade == "S" or "s")):
    print(nome, ", você tem direito a meia-entrada")
else:
    print(nome, ", você não tem direito a meia-entrada, portanto terá que adquirir o inteira")

