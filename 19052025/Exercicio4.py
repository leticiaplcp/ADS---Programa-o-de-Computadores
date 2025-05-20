#Criar uma função que solicita ao usuario 1 valor
#e verificar se essse valor é um numero

def solicitaValorNumerico():
    numero = input("Digite um numero: ")
    if type(numero) == int:
        return numero
    else:
        return False

print(solicitaValorNumerico())
