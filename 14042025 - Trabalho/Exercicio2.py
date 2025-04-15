print ("A senha do dragão")
print ("Um dragão guarda uma caverna, A senha é 'PyThOn3', mas ele só aceita se a senha estiver em maiúscula e tiver exatamente 7 caracteres.")
print ("Verifique se a senha é válida e exiba 'Acesso concedido' ou 'Acesso negado'")

senhaverdadeira = "PythOn3";
senha = str(input("Me fale qual é a senha para entrar na caverna do dragão: "))


if senha == senhaverdadeira.upper() and len(senha) == 7:
    print ("Acesso concedido")
else:
    print ("Acesso negado")
