tipo_diaria = str(input("Me diga o tipo d adiaria (S D T): "))
qtd_diaria = int(input("Me diga quantas diarias deseja se hospedar: "))

if tipo_diaria != S or D or T:
    print("Tipo de diaria errada, peço que reinicie o programa")
    
elif tipo_diaria == S:
    print("O valor da sua hospedagem é de R$ " + (255,50 * qtd_diaria))
