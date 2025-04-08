'''num = int(input("Digite um numero: "))
opcao = str(input("Deseja continuar com a soma? S/N "))
numero = 0

while opcao == 'S':
    numero = int(input("digite outro numero para ser somado: "))
    opcao = str(input("Deseja continuar com a soma? S/N "))

soma =  num + numero

print ("O resultado da soma é: " + str(soma))'''


resp = "S"
contador = 0
soma = 0

while resp == "S":
    numero = float(input("Digite um valor para calcular a media: "))
    contador = contador + 1
    soma = soma + numero
    resp = input("Para continuar digitando mais valores, escreva (S): ")

media = soma / contador

print ("A media dos numeros digitados é: " + str(round(media,2)))
