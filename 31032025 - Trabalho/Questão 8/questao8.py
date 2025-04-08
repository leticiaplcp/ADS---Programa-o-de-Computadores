print("Bem-vindo(a) ao sistema de classificação de triângulos!")

a = float(input("Informe o comprimento do lado A: "))
b = float(input("Informe o comprimento do lado B: "))
c = float(input("Informe o comprimento do lado C: "))

if a == b == c:
    print("O triângulo é Equilátero.")
elif a == b or b == c or a == c:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é Escaleno.")
