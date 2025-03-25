import math

valor = int(input("Digite um numero, pois irei calcular a raiz dele: "))


if valor >= 0:
    print("Numero positivo")
    valor_at = math.sqrt(valor)

    print("A raiz quadrada do seu numero é:", str(round(valor_at,2)))

else:
    print ("O numero digitado é negativo")
 
