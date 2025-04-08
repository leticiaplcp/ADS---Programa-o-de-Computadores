num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

while num1 >= num2:
    num1 = int(input("Digite o primeiro numero novamente: "))
    num2 = int(input("Digite o segundo numero novamente: "))
    
soma = num1 + num2
print ("Resultado da soma dos dois numeros: " + str(soma))
