soma = 0

for i in range (1, 11):
    num = int(input("Digite o " + str(i) + "º numero: "))

    if (num%2 == 0):
        soma = soma + num
    else:
        print ("Numero não corresponde para as regras da conta.")
    print ("Soma atualizada: " +(str(soma)))

