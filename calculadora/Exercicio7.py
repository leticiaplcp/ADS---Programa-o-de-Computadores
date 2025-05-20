#Calculadora

print("Calculadora")

print("\n")

print("[1] Soma")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
print("[0] Sair")

print("\n")



def operacaoSoma(num1,num2):
    return num1 + num2


def operacaoSubtracao(num1,num2):
    return num1 - num2

def operacaoMultiplicacao(num1,num2):
    return num1 * num2

def operacaoDivisao(num1,num2):
    return num1 / num2

def operacaoSair():
    return False

operacao = int(input("Escolha uma operação pelo indice: "))


if operacao == 0:
    total = operacaoSair()
    print("Até mais!")
    exit()

if operacao >= 5:
    print("Indice invalido, recomeçe o programa")
    exit()

    
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o primeiro numero: "))





if operacao == 1:
    total = operacaoSoma(num1,num2)
    print(total)

if operacao == 2:
    total = operacaoSubtracao(num1,num2)
    print(total)

if operacao == 3:
    total = operacaoMultiplicacao(num1,num2)
    print(total)

if operacao == 4:
    total = operacaoDivisao(num1,num2)
    print(total)


