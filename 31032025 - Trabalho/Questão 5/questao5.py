print("Bem-vindo(a) ao sistema de conversão de temperatura!")

escala_origem = input("Informe a escala de origem (C para Celsius ou F para Fahrenheit): ").upper()

temperatura = float(input("Informe o valor da temperatura: "))

if escala_origem == "C":
    temperatura_convertida = (temperatura * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {temperatura_convertida:.1f}°F")
elif escala_origem == "F":
    temperatura_convertida = (temperatura - 32) * 5/9
    print(f"A temperatura em Celsius é: {temperatura_convertida:.1f}°C")
else:
    print("Escala inválida! Por favor, insira 'C' para Celsius ou 'F' para Fahrenheit.")
