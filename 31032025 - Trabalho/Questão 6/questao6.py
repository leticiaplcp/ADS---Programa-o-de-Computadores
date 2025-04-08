print("Bem-vindo(a) ao sistema de verificação de ano bissexto!")

ano = int(input("Informe um ano para verificar se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Bissexto")
else:
    print("Não bissexto")
