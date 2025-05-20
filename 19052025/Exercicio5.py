#Criar uma função que solicita ao usuario 1 valor
#e verificar se esse valor tem mais de 3 digitos
#Caso tenha , retorna o valor, caso contraio retorna falso

def solicitaNumero():
    numero = input("Digite um valor que contenha mais de 3 digitos: ")
    if len(numero) >= 3:
        return numero
    else:
        return False

if solicitaNumero():
    print("Numero Valido")
else:
    print("Tamanho do numero invalido")


#Crie uma função que recebe um valor, o numero deve obedecer as regras abaixo
#se esse valor é par, se é positivo e se é maior que 100

def validaNumero(numero):
    #Verifica se o numero é par
    if numero %2 != 0:
        print("O numero é impar")
        return False
    #Verifica se o numero
    if numero < 0:
        print("O numero é negativo")
        return False
    #Verifica se é maior que 100
    if numero < 100:
        print("O numero é menor que 100!")
        return False
    return True
        
#Enquanto usuario não digitar um numero n=validp, peça outro numero
numero = int(input("Digite um numero: "))
numero_valido = validaNumero(numero)

while not numero_valido:
    numero = int(input("Digite um numero: "))
    numero_valido = validaNumero(numero)
