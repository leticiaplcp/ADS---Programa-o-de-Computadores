idade = int(input("Me diga a sua idade: "))


if ((idade >= 0) and (idade <= 12)):
    print ("Você é uma criança")
elif ((idade >= 13) and (idade <= 17)):
    print ("Você é um adolescente")
else:
    print ("Você é um adulto")
