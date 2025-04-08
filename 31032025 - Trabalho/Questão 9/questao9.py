print("Bem-vindo(a) ao sistema de cálculo de desconto!")

valor_produto = float(input("Me diga o valor original do produto (Utilize o ponto ao invés da vírgula): "))

if valor_produto > 100:
    valor_desconto = (valor_produto * 10) / 100
else:
    valor_desconto = (valor_produto * 5) / 100

valor_final = valor_produto - valor_desconto

print("O valor atualizado do seu produto é: R$ ", "%.2f" % valor_final)




