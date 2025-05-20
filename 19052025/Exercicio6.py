
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
